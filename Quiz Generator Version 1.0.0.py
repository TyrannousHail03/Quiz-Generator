# Version 1 of this Quiz Generator will use text-based input and output.
import sys  # To exit later in program
# This block of code will create the .py file and name it based on user input
fileName = input("What would you like your file to be named?")  # Takes user input for file name
createFile = open(fileName + ".py", "w+")  # Creates a .py file in the directory this file is from

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
    elif startGen.lower() == "no" or startGen == "n":
        sys.exit()
    else:
        print("Sorry, your input was not understood.")
        questionGenerator()


questionGenerator()
