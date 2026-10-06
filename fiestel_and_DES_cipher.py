IP_TABLE = (
	58, 50, 42, 34, 26, 18, 10, 2,
	60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6,
	64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17, 9, 1,
	59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5,
	63, 55, 47, 39, 31, 23, 15, 7,
)

PC1_TABLE = (
	57, 49, 41, 33, 25, 17, 9,
	1, 58, 50, 42, 34, 26, 18,
	10, 2, 59, 51, 43, 35, 27,
	19, 11, 3, 60, 52, 44, 36,
	63, 55, 47, 39, 31, 23, 15,
	7, 62, 54, 46, 38, 30, 22,
	14, 6, 61, 53, 45, 37, 29,
	21, 13, 5, 28, 20, 12, 4,
)

PC2_TABLE = (
	14, 17, 11, 24, 1, 5,
	3, 28, 15, 6, 21, 10,
	23, 19, 12, 4, 26, 8,
	16, 7, 27, 20, 13, 2,
	41, 52, 31, 37, 47, 55,
	30, 40, 51, 45, 33, 48,
	44, 49, 39, 56, 34, 53,
	46, 42, 50, 36, 29, 32,
)

LEFT_SHIFTS = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)



def _validate_bits(block, expected_length):
	if not isinstance(block, str) or len(block) != expected_length:
		raise ValueError(f"block must be a {expected_length}-bit string")
	if any(bit not in "01" for bit in block):
		raise ValueError("block may contain only '0' and '1'")


def _permute(block, table):
	return "".join(block[position - 1] for position in table)


def desInitialPermutation(block):
	"""Apply the DES initial permutation to a 64-bit binary block."""
	_validate_bits(block, 64)
	return _permute(block, IP_TABLE)


def desPermutedChoice1(block):
	"""Apply DES PC-1 to a 64-bit binary key, returning 56 bits."""
	_validate_bits(block, 64)
	return _permute(block, PC1_TABLE)


def desLeftShift(block, round_number):
	"""Rotate a 28-bit key half left by the DES amount for this round."""
	_validate_bits(block, 28)
	if not isinstance(round_number, int) or not 1 <= round_number <= 16:
		raise ValueError("round_number must be an integer from 1 to 16")
	shift = LEFT_SHIFTS[round_number - 1]
	return block[shift:] + block[:shift]


def desPermutedChoice2(block):
	"""Apply DES PC-2 to a 56-bit joined key, returning 48 bits."""
	_validate_bits(block, 56)
	return _permute(block, PC2_TABLE)


def _to_bits(value):
	return "".join(f"{byte:08b}" for byte in value.encode("ascii"))


def _to_hex(bits):
	return f"{int(bits, 2):0{len(bits) // 4}X}"


if __name__ == "__main__":
	plaintext = "ABCDEFGH"
	key = "133457799BBCDFF1"
	plaintext_bits = _to_bits(plaintext)
	key_bits = f"{int(key, 16):064b}"
	initial_permutation = desInitialPermutation(plaintext_bits)
	permuted_key = desPermutedChoice1(key_bits)
	left_half = permuted_key[:28]
	right_half = permuted_key[28:]
	shifted_left = desLeftShift(left_half, 1)
	shifted_right = desLeftShift(right_half, 1)
	round_key = desPermutedChoice2(shifted_left + shifted_right)

	print(f"Plaintext: {plaintext}")
	print(f"Plaintext bits: {plaintext_bits}")
	print(f"Initial permutation (IP): {_to_hex(initial_permutation)}")
	print(f"Key: {key}")
	print(f"PC-1 key (56 bits): {permuted_key}")
	print(f"Round 1 shifted C: {shifted_left}")
	print(f"Round 1 shifted D: {shifted_right}")
	print(f"Round 1 subkey (PC-2): {_to_hex(round_key)}")
