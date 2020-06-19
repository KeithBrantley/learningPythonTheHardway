from sys import argv

script, filename = argv
# create a variable txt that opens filename
txt = open(filename)
# print a string with the filename
print(f"Here's your life {filename}:")
# calls txt variable you created and reads it
print(txt.read())
# prints a string that says to print filename txt_again
print("Type the filename again:")
# file_again variable is created its an input
file_again = input("> ")
# txt_again variable is created it calls the file_again variable which stores what the user inputs
txt_again = open(file_again)
# print fuction is called and prints/reads txt_again
print(txt_again.read())
