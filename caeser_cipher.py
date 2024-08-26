import string

alphabet_list = list(string.ascii_lowercase)

def caeser_cipher(text,shift,operation):
    cipher_text = ""
    for letter in text:
        if letter in alphabet_list: 
            if(operation == "encode"):
                shift_index = (alphabet_list.index(letter) + shift) % len(alphabet_list)
            else:
                shift_index = (alphabet_list.index(letter) - shift) % len(alphabet_list)
            cipher_text += alphabet_list[shift_index]
        else:
            cipher_text += letter
    print("Cipher message - " + cipher_text + "\n")

while True:
    print("Caeser Cipher Encryption in Python")
    input_text = input("Type the message \n").lower()
    input_shift = int(input("Type the shift number \n"))
    direction = input("Do you want to encrypt or decrypt this message ? \n Type encode to encrypt/ decode to decrypt \n").lower()

    if(direction == "encode"):
        caeser_cipher(input_text,input_shift,"encode")
    elif(direction == "decode"):
        caeser_cipher(input_text,input_shift,"decode")
    else:
        print("Please enter a valid option \n")