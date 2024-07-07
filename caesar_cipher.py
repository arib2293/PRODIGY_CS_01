def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            elif char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message: ").strip().lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice, please try again.")
        return

    text = input("Enter the message: ").strip()
    try:
        shift = int(input("Enter the shift value (integer): ").strip())
    except ValueError:
        print("Invalid shift value, please enter an integer.")
        return

    if choice == 'encrypt':
        encrypted_message = caesar_cipher_encrypt(text, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'decrypt':
        decrypted_message = caesar_cipher_decrypt(text, shift)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
