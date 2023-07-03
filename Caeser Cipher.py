import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  
def caesar(plain_text,shift_amount,cipher_direction):
        cipher_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                if cipher_direction == "encode":
                    new_position = position + shift_amount
                elif cipher_direction == "decode":
                    new_position = position - shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char    
        print(cipher_text)
        
        

end_loop = False
while not end_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26    
    caesar(plain_text=text,shift_amount=shift,cipher_direction=direction)
    cont = input("Would you like to run the cipher again?\n").lower()
    if cont == "no":
         end_loop = True
         print("Goodbye")