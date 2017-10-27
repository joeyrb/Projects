#!/usr/bin/python
from math import *

def GET_PRIMES( n ):
	primes = []
	for i in range(1,n):
		isPrime = True
		for j in range(2, ceil(sqrt(i))):
			if i % j == 0:
				isPrime = False
		if isPrime:
			primes.append(i)

	return primes


def main():
	n = int(input("Get primes for: "))
	print(GET_PRIMES(n))

main()