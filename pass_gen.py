#Password Generator Script
#Pre-CEH Python Project
#Author - Confidence Antwi (Carlvinchi)

import string  
import secrets



class Cypher:
    user_name = input("Enter username : ") # take user name
    user_len = input("Enter password length, it must be an integer greater than 11 : ") #take password length from user
    try:
            
            val = int(user_len) # Convert password length into  an integer
            if val >= 12:
                print("Generating Password ................") 
                res = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for x in range(val))
                print("Generated password is : ", str(res)) 
            else:
                print("Password length must be greater than 11, default password length 12, will be used!")
                print("Generating Password ................") 
                res = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for x in range(12))
                print("Generated password is : ", str(res)) 
            
    except ValueError: #Will handle situations where user does not enter digits as the password length
        print("Invalid input, default password length 12, will be used!")
        print("Generating Password ................") 
        res = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for x in range(12))
        print("Generated password is : ", str(res)) 
        
        
   

cyph = Cypher()


