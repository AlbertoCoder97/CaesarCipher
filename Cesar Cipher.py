#Simple Cesar Cipher made by AlbertoCoder97 while bored instead of studying for his exam lol
#This is a little array containing all lower case letters from the alphabet.
#This will be used in both functions to get the new/original letter.
letters = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#This method takes as input a string and an integer value as key
def code(message, key):
    newMessage = "" #Initialize a new string
    for letter in message.lower(): #For loop to cycle all the chars in the message
        if letter.isalpha():    #If the letter is an actual letter ,.isalpha(),
            newMessage += letters[(key + (letters.index(letter)))%26] #Code the new letter using the key in modulus 26
    return newMessage

#This method takes as input a string and an integer value as key
def decode(message, key):
    newMessage = "" #Initialize a new string
    for letter in message.lower():  #For loop to cycle all the chars in the message
        if letter.isalpha():    #if the letter is an actual letter, .isalpha(),
            newMessage += letters[((letters.index(letter) - key))%26]   #Decode the letter using the key in modulus 26
    return newMessage.upper()

#Example
message = "I lIkE ceSAR's SaLaDs"
codedMessage = code(message, 123456)
decodedMessage = decode(codedMessage, 123456)
print(codedMessage, decodedMessage)