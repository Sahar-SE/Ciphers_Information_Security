"""Demonstrate a brute-force search for lowercase passwords of 1-4 letters."""

from itertools import product
from string import ascii_lowercase
from time import perf_counter


def crack_password(password):
	"""Return the number of guesses and elapsed seconds, or None if invalid."""
	if not 1 <= len(password) <= 4 or any(letter not in ascii_lowercase for letter in password):
		return None

	iterations = 0
	started = perf_counter()
	for length in range(1, 5):
		for letters in product(ascii_lowercase, repeat=length):
			candidate = "".join(letters)
			iterations += 1
			if candidate == password:
				return iterations, perf_counter() - started

	return iterations, perf_counter() - started


def main():
	password = input("Enter a lowercase password (1-4 letters): ")
	result = crack_password(password)
	if result is None:
		print("Invalid input: use 1-4 lowercase English letters only.")
		return

	iterations, elapsed = result
	print(f"Password successfully cracked: {password}")
	print(f"Iterations: {iterations}")
	print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
	main()