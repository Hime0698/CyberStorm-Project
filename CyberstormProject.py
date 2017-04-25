###############################################################################
#Names: Jacob Sennett, Nolan Lofton,
#Date:
#Description:
##############################################################################
import random
import RPi.GPIO as GPIO
import pygame

class game(object):
    def __init__(self):
        self.teams = {} # Holds team names and scores
        self.questions1 = {} # load the picture with the questions and answers and the right answers
        self.questions2 = {} # load the picture with the questions and answers and the right answers
        self.questions3 = {} # load the picture with the questions and answers and the right answers
        self.questions4 = {} # load the picture with the questions and answers and the right answers
        self.sounds = []
        self.wronganswers = 3
        self.currentteam = "None"
        self.a = "pin for a"
        self.b = "pin for b"
        self.c = "pin for c"
        self.d = "pin for d"

    def setupGUI(self):
        #set up the gui

    def PlayGame(self):
        while (self.wronganswers > 0)
            "display the catagory screen"
            print "please select catagory"
            if "gpio for catagory one" == self.a:
                currentquestion = random.choice(questions1.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions1[currentquestion]
                    "green led on"
                    "play sound for right answer"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    "play wrong sound"
                    self.wronganswers = self.wronganswers - 1
                    
            elif "gpio for catagory one" == self.b:
                currentquestion = random.choice(questions2.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions3[currentquestion]
                    "green led on"
                    "play sound for right answer"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    "play wrong sound"
                    self.wronganswers = self.wronganswers - 1
                    
            elif "gpio for catagory one" == self.c:
                currentquestion = random.choice(questions3.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions3[currentquestion]
                    "green led on"
                    "play sound for right answer"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    "play wrong sound"
                    self.wronganswers = self.wronganswers - 1

            elif "gpio for catagory one" == self.d:
                currentquestion = random.choice(questions4.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions4[currentquestion]
                    "green led on"
                    "play sound for right answer"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    "play wrong sound"
                    self.wronganswers = self.wronganswers - 1

            else:
                print "Invalid Selection"
                
            
        #code for the game goes here

    def intermission(self, teamname):
        for key, value in teams.items():
            print "{}: {}".format(key, value)
        self.currentteam = input
        self.teams[self.currentteam] = 0 #allows for setup of teams and initial points
        #display the instructions picture
        
