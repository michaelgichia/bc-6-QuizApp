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

# For time functionality
import time

# Helper to download json file
import requests




class QuizApp(cmd.Cmd):
    # Cmd class provides a simple framework for writing line-oriented command interpreters

    # Change the default font to slant 
    f = Figlet()

    # Banner

    intro = "\n\n"

    intro = Fore.CYAN + f.renderText(' '*15 + 'Q u i z App')

    # Reset the colour and and style
    intro += Style.RESET_ALL

    intro += "-+-"*30+"\n"

    intro += "-+-"*30+"\n"

    # Below is a menu that appear first on the console
    intro += Fore.YELLOW + Style.BRIGHT + "\nUsage:\n"

    intro += "\n\t<command> [<args>] [<options]                   --Show this screen and exit.\n"    

    intro += "\nCommands: \n"

    intro += "\n\tlistquizzes                      --List of all the available quizzes in your library\n"

    intro += "\n\timportquiz <path_to_quiz_JSON>   --Import a new quiz from a JSON file\n"

    intro += "\n\ttakequiz <quiz_name>             --Start a new quiz\n"

    intro += "\n\tonlinequizzes                    --List online quizzes\n"

    intro += "\n\tdownloadquiz                     --Download quiz from online library\n"

    intro += "\n\tuploadquiz                       --Upload a quiz to online library\n"

    intro += "\n\ttakeonline                       --Take an online quiz\n"

    doc_header = "Documented commands (type help <topic>):"

    undoc_header = "Undocumented commands:"


    # Firebase db url to upload and download samplequiz
    db_url = 'https://cmdquizapp.firebaseio.com/'

    # API to update(PATCH, PUT), create(POST), or remove(DELETE) stored data
    firebase = firebase.FirebaseApplication('https://cmdquizapp.firebaseio.com', None)


    def list_questions(self, samplequiz):

        """
            This function prints questions to the console.

            Also return the result of question user didn't get right.

            This function is call from do_takequiz function so that it 

            can excute after a quiz is choosen by the user.

        """

        # Empty list to store question answered wrongly and user answers
        wrong_questions = []

        # Store the score of the user
        score = 0
        

        # Get the number of questions on the json quiz file
        questions_num = len(samplequiz["questions"])

        # Store starting time
        start_time = time.time()

        # Defined time on the quiz
        quiz_time = int(samplequiz["time"])

        # Stop the timer if tame taken is longer than required time
        time_out = False

        # Print the question and options to the console
        for counter, i in enumerate(samplequiz["questions"], 1):

            # Break if the user runs out of time
            if (time.time() - start_time > quiz_time):
                time_out = True
                break

            # Get difference of starting time and current time
            elapsed_time = (time.time() - start_time)

            # Get remaining time
            remaining = int(quiz_time - elapsed_time)

            # Pretify the console with 50*'='
            print "\n" + "-+-"*10

            # Display remaing time in user friendly formatting
            print Back.BLACK + Fore.YELLOW + "\nRemaining Time in Seconds: " + str(remaining) + " \n"

            # Pretify the console with 50*'='
            print "-+-"*10

            # Print the question to the console. Counter dictate the position of the question
            print Back.CYAN + Fore.BLACK + "\nQn" + str(counter)+" : " + i["Qn"]+ "\n"

            # Pretify the console with 50*'='
            print "="*70

            # Print option A to console as an answer potion    
            print Fore.GREEN +"A : " + i["A"]

            # Print option B to console as an answer potion 
            print Fore.GREEN + "B : " + i["B"]

            # Print option C to console as an answer potion 
            print Fore.GREEN + "C : " + i["C"]

            # Print option D to console as an answer potion 
            print Fore.GREEN + "D : " + i["D"] + "\n"
            
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
                print Fore.MAGENTA + "\nQn: "+ wrong_qn["Qn"] + "\n"

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
                print Fore.RED + "answer : " + wrong_qn["answer"]


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
                
                print "\n\t" + str(num)+'. ' + file[:len(file) - 5] + "\n"

        print "Options: "
        print "\tTo take a quiz type 'takequiz <quiz_name>' or \n"
        print "\tTo import a quiz  type 'importquiz' "


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

            try:
                samplequiz = json.load(f)


                # Call the function list_questions to print question to the console
                # This function also displays results and question are wrongly answered
                self.list_questions(samplequiz)
            except:

                print "Enter a valid option"


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


    def do_onlinequizzes(self, samplequiz):
        """
Description: 

    Console command for listing online quizzes on firebase.

Usage:

    onlinequizzes

    """
     
        # Call a get request and store the root file in the samplequizzes
        quizzes = self.firebase.get('/', None)

        # Loop over the samplequizzes to list them 
        # Call enumerate method to arrange the quizzes starting from 1
        for num, samplequiz in enumerate(quizzes, 1):

            # Print quiz from firebase db
            print num, samplequiz

        # Ask user to take online quiz
        print "\nTo take the online quiz type: takequiz <quiz_name>\n"


    def do_downloadquiz(self, samplequiz):

        """
Description: 

    Console command for downloading quiz from online firebase library.

Usage:

    downloadquiz

        """

        # Check if the command is passed with the argument
        if samplequiz:

            # Url for the selected json file
            quiz_url = self.db_url + samplequiz + ".json"

            # File to store downloaded samplequiz
            dest_folder = "./sample_quizzes/" + samplequiz + ".json"

            # Create the file json
            dest = os.mknod(dest_folder)

            try:
                # requests.gets downloads the json file
                requests.get(quiz_url) 

                # Pretify print statement
                print "\n" + "*" * 30
                print "Quiz downloaded successfully!"
                print "\n" + "*" * 30

            # Handle error and print
            except:

                print "\nQuiz failed to downoad!\n"

        else:

            # Print options
            print "To download again please type:\n  downloadquiz <quiz_name>"


    def do_uploadquiz(self, samplequiz):
        """
Description: 

    Console command for uploading quiz to online firebase library.

Usage:

    uploadquiz

        """
        # Check if argument is given
        if samplequiz:

            # Current directory and name of the json file
            quiz_name = "./sample_quizzes/" + samplequiz + ".json"

            # Write the dict to json file
            with open(quiz_name, 'r') as txtfile:

                try:

                    # This is dict    
                    json_text = json.load(txtfile)

                    # Call a post request and post to firebase db
                    self.firebase.put("/", samplequiz, json_text)

                    print "\nQuiz successfully uploaded!\n"

                except:

                    print "\nFile didn't upload!"

        else:

            print "To upload again please type:\n  upload <quiz_name>"

    def do_takeonline(self, samplequiz):

        # Check if argument is given
        if samplequiz:

            # Variable that reference the dict on firebase db
            var_path ='/' + samplequiz

            # Download the quiz
            # Call a get request to download the quiz dict
            quiz = self.firebase.get(var_path, None)

            # Call list_questions to display the json file
            self.list_questions(quiz)



# Seload the game over and over with Cmdloop
if __name__ == '__main__':
    QuizApp().cmdloop()
