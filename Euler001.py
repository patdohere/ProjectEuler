"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
TIME COMPLEXITY ANALYSIS ~ O(9000)
solve() ?
	range(1, 1000) => O(1000)
	enumerate(numbers) => O(1000)
	for loop => O(1000) * O(6) => O(6000)
		if statement => O(5)
			assignment => O(1)
	sum(numbers) => O(1000)

fac3() => O(1)

fac5() => O(1)
"""

class Eular1():
	def __init__(self):
		print solve()

	def solve():
		numbers = range(1, 1000)
		for idx, number in enumerate(numbers):
			if not fac3(number) and not fac5(number):
				numbers[idx] = 0
		return sum(numbers)
	
	def fac3(number):
		return number % 3 == 0
	
	def fac5(number):
		return number % 5 == 0
