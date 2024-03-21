#Task No 1 Prajwal Kunjekar
def analyze_message(message):
    num_letters = sum(c.isalpha() for c in message)
    num_digits = sum(c.isdigit() for c in message)
    num_special = len(message) - num_letters - num_digits

    print("Message Analysis:")
    print("-----------------")
    print(f"First character: {message[:1]}")
    print(f"Last character: {message[-1]}")
    print(f"Total characters: {len(message)}")
    print(f"Alphabetic characters: {num_letters}")
    print(f"Digits: {num_digits}")
    
    if num_special > 0:
        print(f"Special characters: {num_special}")
    else:
        print("No special characters")

def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if action == 'E':
                result_char = chr((ord(char) - start + shift) % 26 + start)
            elif action == 'D':
                result_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Invalid action. Use 'E' to encrypt or 'D' to decrypt")
            result += result_char
        else:
            result += char
    return result

def main():
    print("-------------------------------------------- Caesar Cipher Tool --------------------------------------------------")
    print("")

    while True:
        action = input("Do you want to encrypt or decrypt a message? ('E' for encryption, 'D' for decryption, 'Q' to quit): ").upper()
        if action == 'Q':
            print("Exiting the program. Goodbye!")
            return
        elif action in ['E', 'D']:
            break
        else:
            print("Invalid action. Please choose 'E', 'D', or 'Q' to quit.")

    # Get the message from the user
    message = input("Enter the message: ")

    if action != 'Q':
        analyze_message(message)

        # Get the shift value from the user
        shift = int(input("Enter the shift value: "))

        if action == 'E':
            result = caesar_cipher(message, shift, 'E')
            print("\nEncrypted Message:", result)
        elif action == 'D':
            result = caesar_cipher(message, shift, 'D')
            print("\nDecrypted Message:", result)

if __name__ == "__main__":
    main()
