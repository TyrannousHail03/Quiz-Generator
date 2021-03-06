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
        questionType()
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


def multiAnswerGen():
    amountOfAnswers = int(input("How many answers does your question have? (Enter a number) "))
    if amountOfAnswers != "default" or amountOfAnswers != 3:
        question = input("What is your question? ")
        fileEdit.write("question" + str(questionNumber) + " = " + 'input(' + "'" + question + "')\n")
        answerCount = 0
        answerNumber = -1
        fileEdit.write("answers" + str(questionNumber) + " = [")
        while answerCount < amountOfAnswers:
            question = input("Answer #" + str(answerCount + 1) + " ")
            fileEdit.write("'" + question + "'")
            if answerCount + 1 != amountOfAnswers:
                fileEdit.write(", ")
            elif answerCount + 1 == amountOfAnswers:
                fileEdit.write("]\n")
            answerCount = answerCount + 1
            answerNumber = answerNumber + 1
        fileEdit.write("if ")
        while answerNumber != -1:
            fileEdit.write("question" + str(questionNumber) + ".lower()" + " == " + "answers" + str(questionNumber)
                           + "[" + str(answerNumber) + "]")
            if answerNumber != 0:
                fileEdit.write(" or ")
            answerNumber = answerNumber - 1
        fileEdit.write(":\n")
        fileEdit.write("    print('Correct')\n" + "else:\n" + "    print('Incorrect')\n")
        questionNumberPlus()
    againCall()


def questionType():
    type = input("\nHow many answers would you like per question? Enter: Single or Multiple ")
    if type.lower() == "one" or type.lower() == "single":
        singleAnswerGen()
    if type.lower() == "multi" or type.lower() == "multiple":
        multiAnswerGen()
    else:
        print("\nSorry, your input was not understood. Please enter 'Single', 'One', 'Multi', or 'Multiple'. ")
        questionType()

questionType()

# 1.2.2 Release Notes:
# Removed startGen() and rewrote the starting code so that it confirms the user wants
# to use the program before creating a quiz
