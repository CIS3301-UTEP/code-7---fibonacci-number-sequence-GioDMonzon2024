import re

file_object = open("social_media_users.csv")

text_from_file = file_object.read()
# print(text_from_file)

emails = re.findall('[a-z]+gmail\.com',text_from_file)
print(emails)
print(len(emails))

# are_emails = re.search('[a-z]+gmail\.com',text_from_file)
# print(are_emails)

def check_password_strength(password):
    if len(password) >= 8 and ' ' not in password:
        print("Level 0: Password has 8 characters without spaces.")
        
        if re.search(r'[A-Za-z]', password) and re.search(r'\d', password):
            print("Level 1: Password has letters and numbers.")
            
            if re.search(r'[@$!%*#?&]', password):
                print("Level 2: Password has a special character.")
                
                if re.search(r'[A-Z]', password):
                    print("Level 3: Password has an uppercase letter.")
                else:
                    print("Password does not have an uppercase letter.")
            else:
                print("Password does not have a special character.")
        else:
            print("Password does not contain both letters and numbers.")
    else:
        print("Password is too short or contains spaces.")

user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)

