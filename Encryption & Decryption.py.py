"""
Project 2: Basic Encryption & Decryption
DecodeLabs - Cyber Security Industrial Training Kit

This program implements a Caesar Cipher to demonstrate fundamental
encryption and decryption logic, including:
- ASCII-based character shifting
- Modular arithmetic for wrap-around
- Edge case handling (spaces, punctuation, numbers, case)
- A user-selectable shift key
"""


def encrypt(text: str, shift: int) -> str:
    """
    Encrypts the input text using a Caesar Cipher shift.
    Formula: E(x) = (x + shift) % 26
    """
    result = []

    for char in text:
        if char.isupper():
            # Shift within uppercase A-Z range (ASCII 65-90)
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result.append(chr(shifted))
        elif char.islower():
            # Shift within lowercase a-z range (ASCII 97-122)
            shifted = (ord(char) - 97 + shift) % 26 + 97
            result.append(chr(shifted))
        else:
            # Leave spaces, numbers, and punctuation unchanged
            result.append(char)

    return "".join(result)


def decrypt(cipher_text: str, shift: int) -> str:
    """
    Decrypts Caesar Cipher text by reversing the shift.
    Formula: D(x) = (x - shift) % 26
    This works simply by re-running encrypt() with a negative shift.
    """
    return encrypt(cipher_text, -shift)


def get_valid_shift() -> int:
    """Prompts the user for a shift key and validates the input."""
    while True:
        try:
            shift = int(input("Enter your shift key (e.g., 3): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def main():
    print("=" * 50)
    print("   DECODELABS - CAESAR CIPHER TOOL")
    print("=" * 50)

    # Step 1: Get user input
    message = input("\nEnter the text you want to encrypt: ")
    shift_key = get_valid_shift()

    # Step 2: Encrypt the message
    encrypted_message = encrypt(message, shift_key)

    # Step 3: Decrypt it back to verify correctness
    decrypted_message = decrypt(encrypted_message, shift_key)

    # Step 4: Display all results
    print("\n" + "-" * 50)
    print(f"Original Text   : {message}")
    print(f"Shift Key       : {shift_key}")
    print(f"Encrypted Text  : {encrypted_message}")
    print(f"Decrypted Text  : {decrypted_message}")
    print("-" * 50)

    # Step 5: Validate that decryption matches the original
    if decrypted_message == message:
        print("✅ Validation Passed: Decrypted text matches the original.")
    else:
        print("❌ Validation Failed: Something went wrong in the logic.")


if __name__ == "__main__":
    main()