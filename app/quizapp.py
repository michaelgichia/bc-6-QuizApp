import cmd

import os

import shutil

import json

import time

class QuizApp(cmd.Cmd):


	# Introductionory message to the console
    intro = "\n+++++++++++++++++++++++++++++++++++\n"

    intro += "\nWelcome to the quiz shell.\n"

    intro += "\n+++++++++++++++++++++++++++++++++++\n"

    intro += "\nAvailable commands please type:\n"

    intro += "\n\thelp or ? to list commands\n"

    intro += "\n\tlistquizzes - List of all the available quizzes in your library\n"

    intro += "\n\timportquiz <path_to_quiz_JSON> - Import a new quiz from a JSON file\n"

    intro += "\n\ttakequiz <quiz_name> - Start taking a new quiz\n"


    def do_listquizzes(self, samplequiz):

        # loop over the folder with sample quizzes
        for num, file in enumerate(os.listdir("./sample_quizzes"), 1):

            if file.endswith("json"):
                print " "
                print "\t" + str(num)+'. ' + file[:len(file) - 5]
        print " "
        print ">>> To take a quiz type 'takequiz <quiz_name>' or \n"
        print ">>> To import a quiz  type 'importquiz' "


# Seload the game over and over with cmdloop
if __name__ == '__main__':
    QuizApp().cmdloop()