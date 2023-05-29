def cypher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet *= 3
    import art
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(plain_text, shift_num, direction_code):
      if direction_code == "decode":
          shift_num *= -1
      textlist = list(plain_text)
      sum = ""
      for x in textlist:
          if x in alphabet:
          # print(x)
              alphindex = alphabet.index(x) + shift_num
              sum += alphabet[alphindex]
          else:
              sum += x
      print(f"The {direction_code}d message is:\n{sum}")

    caesar(plain_text=text, shift_num=shift, direction_code=direction)
cypher()

zero = 0
while zero==0:
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no:\n").lower()
    if repeat == "yes":
        cypher()
    else:
        print("Thank you for using this cipher. <3")
        zero += 1
    
        


#TO DO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TO DO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TO DO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

#TO DO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TO DO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TO DO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

#TO DO-7: Combine the encrypt() and decrypt() functions into a single function called caesar().

#TO DO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

#TO DO-9: Import and print the logo from art.py when the program starts.

#TO DO-10: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TO DO-11: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TO DO-12: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.