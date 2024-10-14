text = input("Enter the text:")
shift = 3

# Using list comprehension for encryption
encrypted_text = ''.join(
    chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a')) if char.isalpha() else char
    for char in text
)

print(encrypted_text)