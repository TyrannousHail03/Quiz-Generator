# Version 1 of this Quiz Generator will use text-based input and output.
import sys  # To exit later in program
# This block of code will create the .py file and name it based on user input
fileName = input("What would you like your file to be named?")  # Takes user input for file name
createFile = open(fileName + ".py", "w+")  # Creates a .py file in the directory this file is from

# Warns the user of using " or ' punctuation in their answers
print("Warning: This program will not function correctly if you use the ' symbol, use \ before the symbol. or ")

# The following will write the base code for a quiz
fileEdit = createFile
questionNumber = 1  # Starts off the question number at 1

def questionNumberPlus():
    global questionNumber
    questionNumber += 1


def questionGenerator(): # Generates Questions
    startGen = input("Add question to quiz?")
    if startGen.lower == "yes" or startGen.lower() == "y":
        question = input("What is the question you would like to ask?")
        fileEdit.write("question" + str(questionNumber) + " = " + 'input(' + "'" + question + "')\n")
        answer = input("What is the answer to your question?")
        fileEdit.write("if " + "question" + str(questionNumber) + " == " + "'" + answer + "':\n" + "    print('Correct')\n"
                       + "else:\n" + "    print('Wrong')\n")
        questionNumberPlus()
        questionGenerator()
    elif startGen.lower() == "no" or startGen.lower() == "n":
        sureExit = input("Are you sure you want to exit?")
        if sureExit.lower() == "no" or sureExit.lower() == "n":
            questionGenerator()
        if sureExit.lower() == "yes" or sureExit.lower() == "y":
            sys.exit()
    else:
        print("Sorry, your input was not understood.")
        questionGenerator()

questionGenerator()

# 1.1.0 Release Notes: Added print("The program will now exit.") when user inputs  no  for adding another question.
# Added a quick check to see if users actually want to exit
# Added a warning about using ' in the questions
# Fixed bug where N as input for the exit warning would not be valid input
