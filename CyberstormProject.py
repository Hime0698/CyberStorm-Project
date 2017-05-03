###############################################################################
#Names: Jacob Sennett, Nolan Lofton, Cotton Richardson, Tyler Nelson
#Date:
#Description: A program for runniung a csc themed game show with a running leaderboard
##############################################################################
import random
import RPi.GPIO as GPIO
import pygame
from time import sleep

class game(object):
    def __init__(self):
        self.teams = {} # Holds team names and scores
        self.questions1 = {"pic.gif":27} # load the picture with the questions and answers and the right answer
        self.questions2 = {} # load the picture with the questions and answers and the right answer
        self.questions3 = {} # load the picture with the questions and answers and the right answer
        self.questions4 = {} # load the picture with the questions and answers and the right answer
        self.currentteam = "None" # variable for storing the current team
        self.wronganswers = 0 #counts the number of wrong answers the team has made
        self.buttons = [17, 27, 22, 5] # sets up the buttons A = 17 B = 27 C = 22 D = 5
        self.led = [24, 18] # sets up the LED pins red = 24 green = 18
        GPIO.setmode(GPIO.BCM) # sets up the GPIO pins
        GPIO.setup(self.buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#sets pin mode for the buttons
        GPIO.setup(self.led, GPIO.OUT) #sets pin mode for the leds
        self.CatScreen = "Catagory screen picture"
        self.intermission = "interission pic"
        self.Gameover = "end pic"
        

    def setupGUI(self):
        "set up the gui here"

    def ButtonPressed(self): #function for easily sensing what button is pressed and retuning it (adapted form simon game)
        pressed = False
            while (not pressed):
                for i in range(len(self.buttons)):#saves the input of the user for checking later
                    while (GPIO.input(self.buttons[i]) == True):
                        ButtonPressed = i
                        pressed = True
        return ButtonPressed

    def PlayGame(self):
        wronganswers = 0
        while ((wronganswers < 3) and (len(self.questions1) + len(self.questions2) + len(self.questions3) + len(self.questions4) > 0)): #continues to run through the catagories and selections as long as there are less than three wrong answers
            GPIO.output(self.led[1], False) # red led off
            GPIO.output(self.led[0], False) # Green Led Off
            "display the catagory screen" #sotred at self.CatScreen
            print "please select catagory"
            if ButtonPressed() == self.buttons[0]: #subrutine for checking catagory one
                if len(self.questions1) < 1): # Contingent for all questions in this catagory having been attempted
                    print "You have answered all questions in this catagory, please select another catagory"
                    PlayGame()
                    
                else:
                    currentquestion = random.choice(self.questions1.keys()) # Picks a random question in the catagory list
                    "display image stored in current question"
                    if ButtonPressed() == self.questions1[currentquestion]: # if the answer is right
                        del self.questions1[currentquestion] # deletes the question so it is not reused for this team
                        GPIO.output(self.led[1], True) # Green LED on
                        self.teams[self.currentteam] += 1 # adds points
                    else:
                        del self.questions1[currentquestion]
                        GPIO.output(self.led[0], True) # Red LED on
                        wronganswers += 1 # adds a wrong answer to the counter
                    
            elif ButtonPressed() == self.buttons[1]:#subrutine for checking catagory two
                if len(self.questions2) < 1): # Contingent for all questions in this catagory having been attempted
                    print "You have answered all questions in this catagory, please select another catagory"
                    PlayGame()
                    
                else:
                    currentquestion = random.choice(self.questions2.keys()) # Picks a random question in the catagory list
                    "display image stored in current question"
                    if ButtonPressed() == self.questions2[currentquestion]: # if the answer is right
                        del self.questions2[currentquestion] # deletes the question so it is not reused for this team
                        GPIO.output(self.led[1], True) # Green LED on
                        self.teams[self.currentteam] += 1 # adds points
                    else:
                        del self.questions2[currentquestion]
                        GPIO.output(self.led[0], True) # Red LED on
                        wronganswers += 1 # adds a wrong answer to the counter
                    
            elif GPIO.input(24):#subrutine for checking catagory three
                if len(self.questions3) < 1): # Contingent for all questions in this catagory having been attempted
                    print "You have answered all questions in this catagory, please select another catagory"
                    PlayGame()
                    
                else:
                    currentquestion = random.choice(self.questions3.keys()) # Picks a random question in the catagory list
                    "display image stored in current question"
                    if ButtonPressed() == self.questions3[currentquestion]: # if the answer is right
                        del self.questions3[currentquestion] # deletes the question so it is not reused for this team
                        GPIO.output(self.led[1], True) # Green LED on
                        self.teams[self.currentteam] += 1 # adds points
                    else:
                        del self.questions3[currentquestion]
                        GPIO.output(self.led[0], True) # Red LED on
                        wronganswers += 1 # adds a wrong answer to the counter

            elif GPIO.input(12):#subrutine for checking catagory four
                if len(self.questions4) < 1): # Contingent for all questions in this catagory having been attempted
                    print "You have answered all questions in this catagory, please select another catagory"
                    PlayGame()
                    
                else:
                    currentquestion = random.choice(self.questions4.keys()) # Picks a random question in the catagory list
                    "display image stored in current question"
                    if ButtonPressed() == self.questions4[currentquestion]: # if the answer is right
                        del self.questions4[currentquestion] # deletes the question so it is not reused for this team
                        GPIO.output(self.led[1], True) # Green LED on
                        self.teams[self.currentteam] += 1 # adds points
                    else:
                        del self.questions4[currentquestion]
                        GPIO.output(self.led[0], True) # Red LED on
                        wronganswers += 1 # adds a wrong answer to the counter

            else:
                GPIO.output(11, True) # Red LED on
                print "Invalid Selection"
        GPIO.output(self.led[1], False) # Green LED off
        GPIO.output(self.led[2], True) # Red LED off
        "display game over screen" #stored at self.Gameover
        print "Game Over!"
        sleep(5)
        intermission()
                
            
        #code for the game goes here

    def intermission(self):
        "display intermission screen" #stored at self.intermission
        for key, value in teams.items():
            print "{}: {}/80".format(key, value)
        print "type in team name in quotes"
        self.currentteam = input
        self.teams[self.currentteam] = 0 #allows for setup of teams and initial points
        #display the instructions picture

####################################################################################################################
  

