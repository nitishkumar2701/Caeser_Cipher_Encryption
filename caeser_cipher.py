import string
textLetterList = []
encodedList = []
decodedList = []
alphabet_list = list(string.ascii_lowercase)

def encrypt(text,shift):
    for letter in text:
        if letter in alphabet_list: 
            shift_index = (alphabet_list.index(letter) + shift) % len(alphabet_list)
            encodedList.append(alphabet_list[shift_index])
        else:
            encodedList.append(letter)
    print("Cipher message - " + ''.join(encodedList) + "\n")

def decrypt(text,shift):
    for letter in text:
        if letter in alphabet_list: 
            shift_index = (alphabet_list.index(letter) - shift) % len(alphabet_list)
            decodedList.append(alphabet_list[shift_index])
        else:
            decodedList.append(letter) 
    print("Cipher  message - " + ''.join(decodedList) + "\n")

while True:
    print("Caeser Cipher Encryption in Python")
    input_text = input("Type the message \n").lower()
    input_shift = int(input("Type the shift number \n"))
    direction = input("Do you want to encrypt or decrypt this message ? \n Type encode to encrypt/ decode to decrypt \n").lower()

    if(direction == "encode"):
        encrypt(input_text,input_shift)
    elif(direction == "decode"):
        decrypt(input_text,input_shift)
    else:
        print("Please enter a valid option \n")