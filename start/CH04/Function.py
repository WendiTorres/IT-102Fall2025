#Create a function

#def creates a function

#by Wendi

def send_message():
    if question == 'Y':
     print("Yes today is a good day")
    elif question == 'N':
     print("Its okay, Tommorrow is another day ")
    elif question == 'idk':
     print("That's okay")
    else:
     print("Please enter a valid input of Y or N for yes or no")
        

question = input("Is today a good day? Please answer with Y or N: ").upper()   
send_message()