# Version 1 of this Quiz Generator will use text-based input and output.
import sys  # To exit later in program

def startGen():
    startQuestion = input("Welcome to the Python 3.6 Quiz Generator. Do you want to create a quiz? ")
    if startQuestion.lower() == "yes" or startQuestion.lower() == "y":
        # Warns the user of using " or ' punctuation in their answers
        print("\nWarning: This program will not function correctly if you use the ' symbol, use \ before the symbol.")
    elif startQuestion.lower() == "no" or startQuestion.lower() == "n":
        sys.exit()
    else:
        print("Sorry, that was not understood")
        startGen()

startGen()

# This block of code will create the .py file and name it based on user input
fileName = input("What would you like your file to be named?")  # Takes user input for file name
createFile = open(fileName + ".py", "w+")  # Creates a .py file in the directory this file is from

# The following will write the base code for a quiz
fileEdit = open(fileName + ".py", "w+")
questionNumber = 1  # Starts off the question number at 1


def questionNumberPlus():
    global questionNumber
    questionNumber += 1


def againCall():
    again = input("Would you like to add another question?")
    if again.lower() == "yes" or again.lower() == "y":
        singleAnswerGen()
    elif again.lower() == "no" or again.lower() == "n":
        print("The program will now exit.")
        sys.exit()
    else:
        print("Sorry, that was not understood.")
        againCall()


def singleAnswerGen(): # Generates Questions
        question = input("What is the question you would like to ask? ")
        fileEdit.write("question" + str(questionNumber) + " = " + 'input(' + "'" + question + "')\n")
        answer = input("What is the answer to your question? ")
        fileEdit.write("if " + "question" + str(questionNumber) + " == " + "'" + answer + "':\n" +
                       "    print('Correct')\n" + "else:\n" + "    print('Incorrect')\n")
        questionNumberPlus()
        againCall()

singleAnswerGen()


# 1.0.0 Release Notes:
# This is an adaptation of the Standard Quiz Generator
# Removed questionType() and multiAnswerGen()
# Fixed Code Accordingly
# Called singleAnswerGen() at the bottom so that the program passes through the other parameters first.
