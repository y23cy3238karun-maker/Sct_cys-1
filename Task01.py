# Caesar Cipher Program

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    print("\n--- Results ---")
    print("Original Message: ", message)
    print("Encrypted Message: ", encrypted_message)
    print("Decrypted Message: ", decrypted_message)