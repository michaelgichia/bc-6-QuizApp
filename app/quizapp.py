# cmd is a framework for command-line applications
import cmd

# Help in listing directories
import os

# This module helps in import a file to a specific folder
import shutil

# Encoding and decoding string
import json

# To change font size and also create a banner
from pyfiglet import Figlet

# Libary for color and font formatting
from colorama import Fore, Back, Style, init
# Assist the colorama to run on windows
init(autoreset=True)

# Firebase db for downloading and uploading quizzes
from firebase import firebase




class QuizApp(cmd.Cmd):
    # Cmd class provides a simple framework for writing line-oriented command interpreters

    # Change the default font to slant 
    f = Figlet(font='slant')

    # Banner

    intro = "\n\n"

    intro = Fore.CYAN + f.renderText('  QuizApp')

    intro += "-+-"*20+"\n"

    intro += "-+-"*20+"\n"

    # Reset the colour and and style
    intro += Style.RESET_ALL


    # Below is a menu that appear first on the console
    intro += Style.BRIGHT + "\nUsage:\n"

    intro += "="*100

    intro += "\n\t-help <command>                    --Show this screen and exit.\n"    

    intro += "\nOptions: \n"

    intro += "="*100

    intro += "\n\t-listquizzes                       --List of all the available quizzes in your library\n\n"

    intro += "\n\t-importquiz <path_to_quiz_JSON>   --Import a new quiz from a JSON file\n"

    intro += "\n\t-takequiz <quiz_name>             --Start taking a new quiz\n"

    intro += "="*100 + "\n\n"

    doc_header = "Documented commands (type help <topic>):"

    undoc_header = "Undocumented commands:"


    def list_questions(self, samplequiz):

        """
            This function prints questions to the console.

            Also return the result of question user didn't get right.

            This function is call from do_takequiz function so that it 

            can excute after a quiz is choosen by the user.

        """

        # Empty list to store question answered wrongly and user answers
        wrong_questions = []

        score = 0

        # # Load the json file and read it as dictionary
        # with open("./sample_quizzes/"samplequiz) as f:
        #     json_text = json.load(f)

            # Print the question and options to the console
        for counter, i in enumerate(samplequiz["questions"], 1) :

            # Print the question to the console. Counter dictate the position of the question
            print "\nQn" + str(counter)+":" + i["Qn"]+ "\n"

            # Pretify the console with 50*'='
            print "="*70

            # Print option A to console as an aswer potion    
            print "A : " + i["A"]

            # Print option B to console as an aswer potion 
            print "B : " + i["B"]

            # Print option C to console as an aswer potion 
            print "C : " + i["C"]

            # Print option D to console as an aswer potion 
            print "D : " + i["D"] + "\n"
            
            # Prompt the user for the answer
            answer = raw_input("Your answer? ").upper()

            # Check is answer is a valid option    
            while answer not in ["A", "B", "C", "D"]:

                # Promt the user for a valid option
                answer = raw_input("Invalid entry!, please enter a valid option: ").upper()

            # Compare user answer and right answer to append to wrong_questions list
            if answer != i["answer"]:

                # Append the whole question to wrong_question list
                wrong_questions.append(i)

            # Pretify the console with 70*'='    
            print "="*70 + "\n"

        score =  len(samplequiz["questions"]) - len(wrong_questions)

        print "="*30+"\n"
        print "Score: " + str(score) + " out of " + str(len(samplequiz["questions"])) + " questions" + "\n"
        print "="*30+"\n" 

        # Prompt the user if they would want to see answers to questions they didn't get right               
        answer2 = raw_input("\nDo you want to see question you answered wrongly? [Y/n] ")

        print "\n"

        # If user answer is y then print the wrong_question list that contain wrong question
        if answer2.lower() == "y":

            # Pretify the console with 70*'='
            print "="*70

            # Pretify the console 
            print " "*20 + " Questions You Got Wrong " + " "*20 + "\n"

            # Pretify the console with 70*'='
            print "="*70

            # For loop to iterate over the wrong_question list

            # Print the wrong questions and answers
            for wrong_qn in wrong_questions:

                # Print the question to console
                print "\nQn: "+ wrong_qn["Qn"] + "\n"

                # Pretify the console with 70*'_'
                print "_"*70

                # Print option B to console as an aswer potion
                print "A : " + wrong_qn["A"]

                # Print option B to console as an aswer potion
                print "B : " + wrong_qn["B"]

                # Print option B to console as an aswer potion
                print "C : " + wrong_qn["C"]

                # Print option B to console as an aswer potion
                print "D : " + wrong_qn["D"]

                # Print option B to console as an aswer potion
                print "answer : " + wrong_qn["answer"]


            # Pretify the console with 70*'_'
                print "_"*70 + "\n"


    def do_listquizzes(self, samplequiz):
        """
Description: 

    Console command for listing sample quizzes.

Usage:

    'listquizzes'
    """
        # We don't call the function because the cmd2 module calls 
        # every function that starts with "do_"

        # loop over the folder with sample quizzes
        for num, file in enumerate(os.listdir("./sample_quizzes/"), 1):

            if file.endswith("json"):
                
                print "\n\t" + str(num)+'. ' + file[:len(file) - 5]
        print " "
        print ">>> To take a quiz type 'takequiz <quiz_name>' or \n"
        print ">>> To import a quiz  type 'importquiz' "


    def do_takequiz(self, samplequiz):

        """
Description: 

    Console command for taking sample quizzes.

Usage:

    takequiz <quiz_name>
    """
        # We don't call the function because the cmd2 module calls 
        # every function that starts with "do_"


        # Equate samplequiz argument to respective json file
        samplequiz = "./sample_quizzes/" + samplequiz + ".json"

        # Load and read the json file as a dictionary
        with open(samplequiz) as f:

            samplequiz = json.load(f)


        # Call the function list_questions to print question to the console
        # This function also displays results and question are wrongly answered
        self.list_questions(samplequiz)


    def do_importquiz(self, src):
        """
Description: 

    Console command for importing a quiz.

Usage:

    importquiz <path_to_quiz_JSON>
    """
        # dest is the destination path where to store imported quiz
        dest = "./sample_quizzes/"

        # Move the json file from src(source) to dest(destination)
        try:
            shutil.move(src, dest)
            print "\nQuiz successfully imported to sample_quizzes folder "

        # Print an Error message indicating source and destination are the same file
        except shutil.Error as e:
            print('Error: source path and destination path are the same!')

        # Print Error message indicating source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)


    def do_onlinequizzes():
        """
Description: 

    Console command for listing online quizzes on firebase.

Usage:

    do_onlinequizzes

    """



# Seload the game over and over with Cmdloop
if __name__ == '__main__':
    QuizApp().cmdloop()
