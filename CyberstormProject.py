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
        self.questions1 = {} # load the picture with the questions and answers and the right answer
        self.questions2 = {} # load the picture with the questions and answers and the right answer
        self.questions3 = {} # load the picture with the questions and answers and the right answer
        self.questions4 = {} # load the picture with the questions and answers and the right answer
        self.currentteam = "None"
        GPIO.setmode(GPIO.BCM) # sets up the GPIO pins
        GPIO.setup(23, GPIO.IN) # placeholder pin number for a
        GPIO.setup(16, GPIO.IN) # placeholder pin number for b
        GPIO.setup(24, GPIO.IN) # placeholder pin number for c
        GPIO.setup(12, GPIO.IN) # placeholder pin number for d
        GPIO.setup(10, GPIO.OUT) # GPIO pin for green LED
        GPIO.setup(11, GPIO.OUT)# GPIO pin for red LED

    def setupGUI(self):
        pass
        #set up the gui

    def PlayGame(self):
        wronganswers = 0
        while ((wronganswers < 3) and (len(self.questions1) + len(self.questions2) + len(self.questions3) + len(self.questions4) > 0)): #continues to run through the catagories and selections as long as there are less than three wrong answers
            GPIO.output(10, False)
            GPIO.output(11, True)
            "display the catagory screen"
            print "please select catagory"
            if GPIO.input(23): #subrutine for checking catagory one
                currentquestion = random.choice(self.questions1.keys())
                "display image stored in current question"
                if "GPIO input for answer" == self.questions1[currentquestion]:
                    del self.questions1[currentquestion]
                    GPIO.output(10, True) # Green LED on
                    self.teams[self.currentteam] += 1
                else:
                    del self.questions1[currentquestion]
                    GPIO.output(11, True) # Red LED on
                    wronganswers += 1
                    
            elif GPIO.input(16):#subrutine for checking catagory two
                currentquestion = random.choice(self.questions2.keys())
                "display image stored in current question"
                if "GPIO input for answer" == self.questions2[currentquestion]:
                    del self.questions2[currentquestion]
                    GPIO.output(10, True) # Green LED on
                    self.teams[self.currentteam] += 1
                else:
                    del self.questions2[currentquestion]
                    GPIO.output(11, True) # Red LED on
                    wronganswers += 1
                    
            elif GPIO.input(24):#subrutine for checking catagory three
                currentquestion = random.choice(self.questions3.keys())
                "display image stored in current question"
                if "GPIO input for answer" == self.questions3[currentquestion]:
                    del self.questions3[currentquestion]
                    GPIO.output(10, True) # Green LED on
                    self.teams[self.currentteam] += 1
                else:
                    del self.questions3[currentquestion]
                    GPIO.output(11, True) # Red LED on
                    wronganswers += 1

            elif GPIO.input(12):#subrutine for checking catagory four
                currentquestion = random.choice(self.questions4.keys())
                "display image stored in current question"
                if "GPIO input for answer" == self.questions4[currentquestion]:
                    del self.questions4[currentquestion]
                    GPIO.output(10, True) # Green LED on
                    self.teams[self.currentteam] += 1
                else:
                    del self.questions4[currentquestion]
                    GPIO.output(11, True) # Red LED on
                    wronganswers += 1

            else:
                GPIO.output(11, True) # Red LED on
                print "Invalid Selection"
        GPIO.output(10, False) # Green LED off
        GPIO.output(11, True) # Red LED off
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
  

