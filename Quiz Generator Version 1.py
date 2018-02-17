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
        sureExit = input("Are you sure you want to exit?")
        if sureExit.lower() == "no" or sureExit.lower() == "n":
            questionGenerator()
        if sureExit.lower() == "yes" or sureExit.lower() == "y":
            sys.exit()
    else:
        print("Sorry, your input was not understood.")
        questionGenerator()


questionGenerator()

# Minor things to add:
#       1. Warnings on punctuation issues. - Do not use ' in a question
# Major things to add:
#       1. Multiple Answer Function and change questionGenerator to be 1 answer function
#       2. Quiz Scorer with grades - give option for letter descriptors and number scale and both
#       3. Enable users to quit programs by saying "quit" or "exit" (simple solution is add another if statement
#       4. Give score report and tell users to type something when finished - will have to be specific to one keyword
#           - Will have to make practice quiz to test out features to program within this program.
