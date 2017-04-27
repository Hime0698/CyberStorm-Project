###############################################################################
#Names: Jacob Sennett, Nolan Lofton, Cotton Richardson, Tyler Nelson
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
        self.currentteam = "None"
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.IN) #placeholder pin number for a
        GPIO.setup(16, GPIO.IN) #placeholder pin number for b
        GPIO.setup(24, GPIO.IN) #placeholder pin number for c
        GPIO.setup(12, GPIO.IN) #placeholder pin number for d

    def setupGUI(self):
        pass
        #set up the gui

    def PlayGame(self):
        wronganswers = 0
        while (wronganswers < 3):
            "display the catagory screen"
            print "please select catagory"
            if GPIO.input(23): #subrutine for checking catagory one
                currentquestion = random.choice(questions1.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions1[currentquestion]:
                    "green led on"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    wronganswers += 1
                    
            elif GPIO.input(16):#subrutine for checking catagory two
                currentquestion = random.choice(questions2.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions3[currentquestion]:
                    "green led on"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    wronganswers += 1
                    
            elif GPIO.input(24):#subrutine for checking catagory three
                currentquestion = random.choice(questions3.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions3[currentquestion]:
                    "green led on"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    wronganswers += 1

            elif GPIO.input(12):#subrutine for checking catagory four
                currentquestion = random.choice(questions4.keys())
                "display image stored in current question"
                if "GPIO input for answer" == questions4[currentquestion]:
                    "green led on"
                    self.teams[self.currentteam] += 1
                else:
                    "red LED on"
                    wronganswers += 1

            else:
                print "Invalid Selection"
        print "Game Over!"
        intermission()
                
            
        #code for the game goes here

    def intermission(self):
        for key, value in teams.items():
            print "{}: {}/80".format(key, value)
        print "type in team name in quotes"
        self.currentteam = input
        self.teams[self.currentteam] = 0 #allows for setup of teams and initial points
        #display the instructions picture

####################################################################################################################


