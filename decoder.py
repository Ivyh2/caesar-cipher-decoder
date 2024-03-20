"""
author: Ivy Huang
Decodes a message that is encrypted using the Caesar Cipher
"""

#Input
#User enters a word to be deciphered and the shift number
encrypted_text = input("Enter text to be deciphered: ").lower()
shift = int(input("Enter a shift amount: "))


#Processing
#Decodes the message, removes the shift of each character by the shift amount

decoded_message = ""
for char in encrypted_text:
    #Converts the letter into its unicode number
    char_num = ord(char)
    
    #Subtracts the shift amount from the unicode number
    char_num = char_num - shift
    
    #The space character does not change
    if char_num == 32 - shift:
        char_num = char_num + shift
    
    #Checks for overflow if removing the shift causes the letters to move 
    #before "a". Also makes sure that the changes do not affect the space
    if 32 < char_num < ord('a'):
        overflow = char_num - ord('a') + 1
        char_num = ord('z') + overflow
    
    
    #Converts the shifted unicode number back into a letter
    #and adds it to the encrypted message
    decoded_message = decoded_message + chr(char_num)



#Output
#Prints out the decoded message
print(decoded_message)
