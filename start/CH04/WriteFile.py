#!/usr/bin/env python3
# Sample script that writes to a file
# By Wendi

#Once information is done save to file called (hackme.txt)

with open("hackme.txt", "r") as hackme:
    content = hackme.read()
    print(content)


#create a list of questions and responses to ask the user
questions = [
"What is your name?",
"What is your favorite color?",
"What was your first pet's name?",
"What is your mother's maiden name?",
"What elementary school did you attend?"
]

answers = []

#loop through each question and save outcome to answers
for q in questions:
    ans = input(q)
    answers.append(ans)
print(answers)

#write all answers to file safely
with open ("hackme.txt", "w") as file:
    for line in answers:
        file.write(line + "\n")


