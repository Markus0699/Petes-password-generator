# Pete's Password Generator
#### Video Demo: https://youtu.be/f0PeFmYvibA
#### Description:
Pete's Password Generator is a program that generatores random passwords. First the user gets asked a few questions, based on the answers to those questions the program will generate a password which matches the users input. After generating the password the program presents the user the password. The user then gets asked if he is satisfied with the result. If the user isnt satisfied a new password will get generatored. After the user is satisfied the usere gets asked if he wants a tip to improve his passwords in the future. If he says yes a tip will be presented to him, the choice of the tip is based on a few set parameters. After that the program exits.

### Coming up the idea
I had some troubles with ideas on what to make. So I started looking in the gallery of CS50x for ideas, after looking for a while I saw that someone made a password generator. I remembered that I'm not very happy with the buildin password generator of my password manager. The buildin password generator only allows a few selected characters (!@#$%^&*), no way to add the rest. I was kinda frustrated, I wanted my passwords to be as strong as possible. Also I dont really trust the buildin solution because I cant verify how the password generator works and if its truly random. So I decided to make my own easy to use and fast password generator that uses all punctuations.

### DISCLAIMER
This program is for educational purposes only. The program is not designed to safely generate passwords.

### Design
I designed my code in a way that makes it easy to read, atleast in my opinion. I split the program in many smaller functions to make it more readable.

### Robustness
Rubbish input of the user results in a reprompt until the program is satisfied.

### Testing
Only 3 of the 6 functions are tested in test_project.py. I couldnt come up with a way to test the functions that ouput truly random values. This is one the things that can be improved, more on that later.

### Improvements
One thing that could be improved is replacing the "random" module with the "secrets" module for security purposes. That would make it a viable option for a password. generator

Redesigning of the function to better suite them for testing with Pytest. Also a way to test the truly random functions would be beneficial.

### Future
I still want to actually use this program in the future, so when I have more spare time I will redesign the program with the secrets module to make it a viable option to use. I might change a few things to make the program less terminal input depended, so I can generate passwords even faster (so no typing of all kinds of input)