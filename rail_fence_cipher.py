def rail_fence_encrypt(text, key):
	if key < 1:
		raise ValueError("key must be at least 1")

	text = text.replace(" ", "")

	if key == 1:
		return text

	pattern = list(range(key)) + list(range(key - 2, 0, -1))
	length = len(text)

	while sum(pattern[index % len(pattern)] == 0 for index in range(length)) != sum(
		pattern[index % len(pattern)] == key - 1 for index in range(length)
	):
		length += 1

	padded_text = text + "X" * (length - len(text))
	rails = ["" for _ in range(key)]

	for index, character in enumerate(padded_text):
		rails[pattern[index % len(pattern)]] += character

	return "".join(rails)

def rail_fence_decrypt(ciphertext, key):
	if key < 1:
		raise ValueError("key must be at least 1")

	ciphertext = ciphertext.replace(" ", "")

	if key == 1:
		return ciphertext

	pattern = list(range(key)) + list(range(key - 2, 0, -1))
	positions = [pattern[index % len(pattern)] for index in range(len(ciphertext))]
	counters = [positions.count(rail) for rail in range(key)]

	rails = []
	start = 0
	for count in counters:
		rails.append(list(ciphertext[start:start + count]))
		start += count

	plaintext = "".join(rails[rail].pop(0) for rail in positions)
	return plaintext.rstrip("X")

def rail_fence_brute_force(ciphertext):
	ciphertext = ciphertext.replace(" ", "")
	return [
		(key, rail_fence_decrypt(ciphertext, key))
		for key in range(1, len(ciphertext) + 1)
	]

print(rail_fence_encrypt("HELLO WORLD", 3))
print(rail_fence_decrypt("HOLELWRDLOX", 3))
print(rail_fence_brute_force("HOLELWRDLOX"))


