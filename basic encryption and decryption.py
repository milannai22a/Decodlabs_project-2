"""
Decodlabs - cyber secuirty project-2
Basic encryption and decryption (caesar cipher)
language: python

"""

#encryption funtion
#formula: E_n(x) = (x+n) mod 26

def encrypt(plaintext: str, shift: int) -> str:
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
         ciphertext += char
    return ciphertext


#decryptin function
#formula: D_n(x) = (x-n)mod 26

def decrypt(ciphertext: str, shift: int) -> str:
    return encrypt(ciphertext, -shift)



    #display function

def display_results(plaintext: str,ciphertext: str, decrypted: str, shift: int):
        print("\n" + "=" * 55)
        print("     decodlabs - caesar cipher result")
        print("=" * 55)
        print(f" shift key    : {shift}")
        print(f"  original text    : {plaintext}")
        print(f" encrypted text    : {ciphertext}")
        print(f"  decrypted text    : {decrypted}")
        print("=" * 55)


        #brute-force attack demonstartion

def brute_force(ciphertext: str):
        print("\n" + "=" * 55)
        print("  brute-force attack demonstartion")
        print("-" * 55)
        for key in range(1, 26):
            attempt = encrypt(ciphertext, -key)
            print(f"  shift {key:2d} -> {attempt}")
        print("-" * 55 + "\n")


        # user interface 
def main():
     print("\n" + "╔" + "═" * 53 + "╗")
     print("║   DecodeLabs — Cyber Security Project 2          ║")
     print("║   Basic Encryption & Decryption (Caesar Cipher)  ║")
     print("╚" + "═" * 53 + "╝\n")




     while True:
        print("options:")
        print("   1-> encrypte a message")
        print("  2 -> decrypt a message")
        print("  3 -> brute-force attack demo")
        print(" 4 -> exit")


        choice = input("enter your choice:  ").strip()


        if choice == '1':
            message = input("enter plaintext message: ")
            while True:
                try: 
                    shift = int(input("enter shift key(1-25): "))
                    if 1 <= shift <= 25:
                        break
                    print(" shift must be between 1 and 25. ")
                except ValueError:
                        print(" please enter a valid intiger")


            cipher = encrypt(message, shift)
            decrypted = decrypt(cipher, shift)
            display_results(message, cipher, decrypted, shift)

        elif choice =="2":
            cipher = input("enter ciphertext to decrypt: ")
            while True:
                try:
                    shift = int(input("enter shift key:"))    
                    if 1 <= shift <= 25:
                      break 
                    print(" shift must be between 1 and 25. ")
                except ValueError:
                     print(" please enter a valid intiger. ")


            result = decrypt(cipher, shift)
            print(f" decrypted text: {result}\n")
                                      
        elif choice== "3":
            cipher = input("enter ciphertext for brute-force attack: ")
            brute_force(cipher)

        elif choice == "4":
             print("Exiting program, thank you.\n")
            
             break 



        else:
            print(" invalid choice,please try again.\n")

if __name__ == "__main__":
    main()

                                    
            



