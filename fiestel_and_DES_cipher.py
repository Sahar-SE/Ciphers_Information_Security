# DES / Feistel-related permutation tables
# ------------------------------------------------------------
# DES is a block cipher. It works on 64-bit blocks and uses a 64-bit key,
# but the key is reduced to 56 bits and then expanded into 16 different
# round subkeys for the 16 rounds of encryption.
#
# The arrays below are fixed DES bit-permutation tables.
# Each number tells Python which bit position to take from the original
# block when building the permuted output.
# ------------------------------------------------------------

# Initial Permutation (IP)
# This is the first step applied to the 64-bit plaintext block.
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

# PC-1: Permuted Choice 1
# Takes the 64-bit key and selects 56 bits in a particular order.
# This is the first key-schedule operation.
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

# PC-2: Permuted Choice 2
# Takes the 56-bit key and generates the 48-bit round key for a round.
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

# DES key-schedule rotation amounts
# Each round uses a different left rotation amount.
# For example, rounds 1 and 2 shift by 1, rounds 3 to 8 shift by 2.
LEFT_SHIFTS = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)


# ------------------------------------------------------------
# Function to validate that a binary block is the correct size and format.
# It ensures the input is a binary string like "01010101".
# ------------------------------------------------------------
def _validate_bits(block, expected_length):
	# block must be a string with exactly expected_length characters
	if not isinstance(block, str) or len(block) != expected_length:
		raise ValueError(f"block must be a {expected_length}-bit string")

	# every character must be either '0' or '1'
	if any(bit not in "01" for bit in block):
		raise ValueError("block may contain only '0' and '1'")


# ------------------------------------------------------------
# Generic permutation function
# This function reorders bits according to a table.
# Example: if table = (3, 1, 2), it outputs the 3rd, 1st, and 2nd bits.
# ------------------------------------------------------------
def _permute(block, table):
	# For each position number in the table, take that bit from the block.
	# Because Python indices start at 0, we subtract 1 from each value.
	return "".join(block[position - 1] for position in table)


# ------------------------------------------------------------
# Initial permutation of plaintext.
# DES begins by permuting the 64-bit plaintext block.
# ------------------------------------------------------------
def desInitialPermutation(block):
	"""Apply the DES initial permutation to a 64-bit binary block."""
	_validate_bits(block, 64)
	return _permute(block, IP_TABLE)


# ------------------------------------------------------------
# Permuted Choice 1 for key schedule.
# This reduces the 64-bit key to 56 bits.
# ------------------------------------------------------------
def desPermutedChoice1(block):
	"""Apply DES PC-1 to a 64-bit binary key, returning 56 bits."""
	_validate_bits(block, 64)
	return _permute(block, PC1_TABLE)


# ------------------------------------------------------------
# Left shift of a 28-bit half of the key.
# DES splits the 56-bit key into two 28-bit halves: C and D.
# Each round shifts one or both halves left by a fixed amount.
# ------------------------------------------------------------
def desLeftShift(block, round_number):
	"""Rotate a 28-bit key half left by the DES amount for this round."""
	_validate_bits(block, 28)

	# round_number must be between 1 and 16 inclusive
	if not isinstance(round_number, int) or not 1 <= round_number <= 16:
		raise ValueError("round_number must be an integer from 1 to 16")

	shift = LEFT_SHIFTS[round_number - 1]
	# rotate left: move first 'shift' bits to the end
	return block[shift:] + block[:shift]


# ------------------------------------------------------------
# Permuted Choice 2 for key schedule.
# After rotating the key halves, PC-2 chooses 48 bits for the round key.
# ------------------------------------------------------------
def desPermutedChoice2(block):
	"""Apply DES PC-2 to a 56-bit joined key, returning 48 bits."""
	_validate_bits(block, 56)
	return _permute(block, PC2_TABLE)


# ------------------------------------------------------------
# Convert text to bits.
# Example: 'A' -> 01000001
# So "ABCDEFGH" becomes 8 bytes * 8 bits = 64 bits.
# ------------------------------------------------------------
def _to_bits(value):
	return "".join(f"{byte:08b}" for byte in value.encode("ascii"))


# ------------------------------------------------------------
# Convert binary bits into hexadecimal for a readable printout.
# ------------------------------------------------------------
def _to_hex(bits):
	return f"{int(bits, 2):0{len(bits) // 4}X}"


# ------------------------------------------------------------
# Main program: demonstration of DES initial permutation and key schedule.
# ------------------------------------------------------------
if __name__ == "__main__":
	# Example plaintext: 8 characters = 64 bits
	plaintext = "ABCDEFGH"

	# Example 64-bit key in hexadecimal
	key = "133457799BBCDFF1"

	# Convert plaintext to 64-bit binary string
	plaintext_bits = _to_bits(plaintext)

	# Convert hex key to 64-bit binary string
	# Example: int(key, 16) converts hex to integer, then :064b converts to binary
	# with exactly 64 bits.
	key_bits = f"{int(key, 16):064b}"

	# 1. Apply DES Initial Permutation (IP) to plaintext
	initial_permutation = desInitialPermutation(plaintext_bits)

	# 2. Apply PC-1 to key: 64 bits -> 56 bits
	permuted_key = desPermutedChoice1(key_bits)

	# 3. Split the 56-bit key into left and right halves (28 bits each)
	left_half = permuted_key[:28]
	right_half = permuted_key[28:]

	# 4. Shift each half left for round 1
	shifted_left = desLeftShift(left_half, 1)
	shifted_right = desLeftShift(right_half, 1)

	# 5. Concatenate shifted halves and apply PC-2: 56 bits -> 48-bit round key
	round_key = desPermutedChoice2(shifted_left + shifted_right)

	# Print results for understanding
	print(f"Plaintext: {plaintext}")
	print(f"Plaintext bits: {plaintext_bits}")
	print(f"Initial permutation (IP): {_to_hex(initial_permutation)}")
	print(f"Key: {key}")
	print(f"PC-1 key (56 bits): {permuted_key}")
	print(f"Round 1 shifted C: {shifted_left}")
	print(f"Round 1 shifted D: {shifted_right}")
	print(f"Round 1 subkey (PC-2): {_to_hex(round_key)}")
