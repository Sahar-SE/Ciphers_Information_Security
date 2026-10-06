# DES lab solution written in a simple student-style way.
# This file is separate from the original project files.
# No imports, no modules, just plain Python logic.

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

E_TABLE = (
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1,
)

P_TABLE = (
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 2, 8,
    24, 14, 32, 27, 3, 9, 19, 13,
    30, 6, 22, 11, 4, 25, 10, 31,
)

LEFT_SHIFTS = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

S_BOXES = (
    (
        (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13),
    ),
    (
        (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
        (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
        (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
        (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),
    ),
    (
        (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
        (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
        (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
        (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12),
    ),
    (
        (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
        (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),
        (10, 3, 13, 4, 9, 0, 11, 1, 2, 8, 5, 14, 12, 15, 7, 6),
        (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14),
    ),
    (
        (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
        (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
        (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
        (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 3, 4, 10, 5, 9),
    ),
    (
        (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
        (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 3, 11, 8),
        (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
        (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13),
    ),
    (
        (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
        (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
        (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
        (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12),
    ),
    (
        (13, 2, 11, 12, 4, 1, 7, 10, 14, 8, 5, 9, 6, 3, 15, 0),
        (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
        (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
        (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11),
    ),
)


def validate_bits(block, length):
    if type(block) != str or len(block) != length:
        raise ValueError("Block must be a string of length " + str(length))
    for bit in block:
        if bit not in "01":
            raise ValueError("Block must contain only '0' and '1'")


def permute(block, table):
    result = ""
    for pos in table:
        result += block[pos - 1]
    return result


def text_to_bits(text):
    bits = ""
    for ch in text:
        bits += format(ord(ch), '08b')
    return bits


def bits_to_hex(bits):
    value = int(bits, 2)
    return hex(value)[2:].upper().zfill(len(bits) // 4)


def hex_to_bits(hex_value):
    return format(int(hex_value, 16), '064b')


def xor_strings(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


def left_rotate(block, shift_amount):
    return block[shift_amount:] + block[:shift_amount]

def desInitialPermutation(block):
    validate_bits(block, 64)
    return permute(block, IP_TABLE)


def desPermutedChoice1(block):
    validate_bits(block, 64)
    return permute(block, PC1_TABLE)


def desLeftShift(block, round_number):
    validate_bits(block, 28)
    if round_number < 1 or round_number > 16:
        raise ValueError("Round number must be between 1 and 16")
    shift = LEFT_SHIFTS[round_number - 1]
    return left_rotate(block, shift)


def desPermutedChoice2(block):
    validate_bits(block, 56)
    return permute(block, PC2_TABLE)


def desExpansionPermutation(block):
    validate_bits(block, 32)
    return permute(block, E_TABLE)


def getSubBoxes(block):
    validate_bits(block, 48)
    result = ""
    for i in range(8):
        chunk = block[i * 6:(i + 1) * 6]
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)
        value = S_BOXES[i][row][col]
        result += format(value, '04b')
    return result


def desRoundPermutation(block):
    validate_bits(block, 32)
    return permute(block, P_TABLE)


def desFinalPermutation(block):
    validate_bits(block, 64)
    fp_table = []
    for i in range(1, 65):
        fp_table.append(IP_TABLE.index(i) + 1)
    return permute(block, fp_table)


# ---------- lab task 2 ----------
def generate_subkeys(key):
    # key can be 64-bit binary string or 16-digit hex string
    if type(key) == str and len(key) == 16:
        key = hex_to_bits(key)
    elif type(key) != str or len(key) != 64:
        raise ValueError("Key must be 64-bit binary string or 16-digit hex string")
    validate_bits(key, 64)

    permuted_key = desPermutedChoice1(key)
    left = permuted_key[:28]
    right = permuted_key[28:]

    subkeys = []
    for round_number in range(1, 17):
        left = desLeftShift(left, round_number)
        right = desLeftShift(right, round_number)
        subkeys.append(desPermutedChoice2(left + right))
    return subkeys


def feistel_round(right_half, subkey):
    expanded = desExpansionPermutation(right_half)
    xored = xor_strings(expanded, subkey)
    substituted = getSubBoxes(xored)
    return desRoundPermutation(substituted)


def desEncryption(plaintext, key):
    if type(plaintext) == str and len(plaintext) == 8:
        plaintext = text_to_bits(plaintext)
    elif type(plaintext) == str and len(plaintext) == 16:
        plaintext = hex_to_bits(plaintext)
    elif type(plaintext) != str or len(plaintext) != 64:
        raise ValueError("Plaintext must be an 8-character text block, 16-hex block, or 64-bit binary block")

    validate_bits(plaintext, 64)
    subkeys = generate_subkeys(key)
    initial = desInitialPermutation(plaintext)

    left = initial[:32]
    right = initial[32:]

    for key_part in subkeys:
        new_left = right
        new_right = xor_strings(left, feistel_round(right, key_part))
        left = new_left
        right = new_right

    final_block = right + left
    cipher_bits = desFinalPermutation(final_block)
    return bits_to_hex(cipher_bits)


def desDecryption(ciphertext, key):
    if type(ciphertext) == str and len(ciphertext) == 16:
        ciphertext = hex_to_bits(ciphertext)
    elif type(ciphertext) != str or len(ciphertext) != 64:
        raise ValueError("Ciphertext must be a 64-bit binary block or 16-digit hex block")

    validate_bits(ciphertext, 64)
    subkeys = generate_subkeys(key)
    subkeys = list(reversed(subkeys))
    initial = desInitialPermutation(ciphertext)

    left = initial[:32]
    right = initial[32:]

    for key_part in subkeys:
        new_left = right
        new_right = xor_strings(left, feistel_round(right, key_part))
        left = new_left
        right = new_right

    final_block = right + left
    plain_bits = desFinalPermutation(final_block)
    return bits_to_hex(plain_bits)




if __name__ == "__main__":
    plain = "ABCDEFGH"
    key = "133457799BBCDFF1"

    print("Plain text:", plain)
    print("Key:", key)

    p_bits = text_to_bits(plain)
    ip_value = desInitialPermutation(p_bits)
    print("IP:", bits_to_hex(ip_value))

    k_bits = hex_to_bits(key)
    pc1 = desPermutedChoice1(k_bits)
    print("PC-1:", pc1)

    left_half = pc1[:28]
    right_half = pc1[28:]
    shift_left = desLeftShift(left_half, 1)
    shift_right = desLeftShift(right_half, 1)
    print("Round 1 shifted C:", shift_left)
    print("Round 1 shifted D:", shift_right)

    round_key = desPermutedChoice2(shift_left + shift_right)
    print("Round 1 subkey (PC-2):", bits_to_hex(round_key))

    expand = desExpansionPermutation("00000000000000000000000000000000")
    print("Expansion Permutation:", expand)

    sbox_out = getSubBoxes("000000000000000000000000000000000000000000000000")
    print("S-boxes output:", sbox_out)

    round_per = desRoundPermutation("00000000000000000000000000000000")
    print("Round permutation:", round_per)

    cipher = desEncryption(plain, key)
    print("Cipher text:", cipher)
    print("Decrypted text:", desDecryption(cipher, key))
