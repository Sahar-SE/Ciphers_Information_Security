"""Demonstrate a dictionary attack using a local newline-separated word list."""

import argparse
from pathlib import Path


def load_dictionary(path):
	"""Index each non-empty dictionary entry by its first attempt number."""
	words = {}
	attempt = 0
	with path.open("r", encoding="utf-8", errors="replace") as word_file:
		for line in word_file:
			word = line.strip()
			if word:
				attempt += 1
				words.setdefault(word, attempt)
	return words


def main():
	parser = argparse.ArgumentParser(
		description="Check a password against a newline-separated password list."
	)
	parser.add_argument(
		"wordlist",
		nargs="?",
		default="2025-199_most_used_passwords.txt",
		help="path to the password list (default: 2025-199_most_used_passwords.txt)",
	)
	args = parser.parse_args()
	wordlist_path = Path(args.wordlist)

	try:
		words = load_dictionary(wordlist_path)
	except OSError as error:
		print(f"Could not read password list '{wordlist_path}': {error}")
		print("Download the provided password list and pass its path as an argument.")
		return 1

	password = input("Enter the password to check: ")
	attempt = words.get(password)
	if attempt is None:
		print("UNSUCCESSFUL: password was not found in the dictionary.")
	else:
		print(f"PASSWORD SUCCESSFULLY CRACKED ({attempt} attempts).")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())