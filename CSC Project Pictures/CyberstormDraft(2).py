###############################################################################
#Names: Jacob Sennett, Nolan Lofton, Cotton Richardson, Tyler Nelson
#Date:
#Description: A program for runniung a csc themed game show with a running leaderboard
##############################################################################
import random
import RPi.GPIO as GPIO
import pygame
from time import sleep
from Tkinter import *

class Game(Frame):
    def __init__(self, parent):
    # call the constructor in the superclass
        Frame.__init__(self, parent)
        self.teams = {} # Holds team names and scores
        self.questions1 = {"C1Q1.gif": 23, "C1Q2.gif": 18 , "C1Q3.gif": 25 , "C1Q4.gif": 18 , "C1Q5.gif": 24, \
                           "C1Q6.gif": 24 , "C1Q7.gif": 18 , "C1Q8.gif": 23 , "C1Q9.gif": 23, "C1Q10.gif":23 ,\
                           "C1Q11.gif" : 18 ,"C1Q12.gif": 18 , "C1Q13.gif": 24 , "C1Q14.gif": 18, "C1Q15.gif": 25, \
                           "C1Q16.gif": 18, "C1Q17.gif": 25,"C1Q18.gif": 24, "C1Q19.gif":24, "C1Q20.gif":24}# load the picture with the questions and answers and the right answer
        self.questions2 = {"C2Q1.gif": 18,"C2Q2.gif": 18 , "C2Q3.gif": 25 , "C2Q4.gif": 24 , "C2Q5.gif": 25, \
                           "C2Q6.gif": 23 , "C2Q7.gif": 25 , "C2Q8.gif": 18 , "C2Q9.gif": 25, "C2Q10.gif": 18 ,\
                           "C2Q11.gif" : 23 ,"C2Q12.gif": 23 , "C2Q13.gif": 23 , "C2Q14.gif": 18, "C2Q15.gif": 23, \
                           "C2Q16.gif": 18, "C2Q17.gif": 18,"C2Q18.gif": 25, "C2Q19.gif":24, "C2Q20.gif": 18} # load the picture with the questions and answers and the right answer
        self.questions3 = {"C3Q1.gif": 18, "C3Q2.gif": 24 , "C3Q3.gif": 25 , "C3Q4.gif": 24 , "C3Q5.gif": 18, \
                           "C3Q6.gif": 25 , "C3Q7.gif": 25 , "C3Q8.gif": 25 , "C3Q9.gif": 23, "C3Q10.gif":23 ,\
                           "C3Q11.gif" : 24 ,"C3Q12.gif": 23 , "C3Q13.gif": 25 , "C3Q14.gif": 25, "C3Q15.gif": 25, \
                           "C3Q16.gif": 18, "C3Q17.gif": 24,"C3Q18.gif": 23, "C3Q19.gif": 25, "C3Q20.gif": 24} # load the picture with the questions and answers and the right answer
        self.questions4 = {"C4Q1.gif": 18, "C4Q2.gif": 23 , "C4Q3.gif": 24 , "C4Q4.gif": 25 , "C4Q5.gif": 18, \
                           "C4Q6.gif": 24 , "C4Q7.gif": 24 , "C4Q8.gif": 18 , "C4Q9.gif": 25, "C4Q10.gif": 18 ,\
                           "C4Q11.gif" : 24 ,"C4Q12.gif": 25 , "C4Q13.gif": 23 , "C4Q14.gif": 18, "C4Q15.gif": 24, \
                           "C4Q16.gif": 23, "C4Q17.gif": 25,"C4Q18.gif": 24, "C4Q19.gif": 18, "C4Q20.gif": 25} # load the picture with the questions and answers and the right answer
        self.currentteam = "None" # variable for storing the current team
        self.wronganswers = 0 #counts the number of wrong answers the team has made
        self.buttons = [23, 18, 24, 25] # sets up the buttons A = 25 B = 24 C = 18 D = 23
        self.led = [4, 17] # sets up the LED pins red = 24 green = 18
        GPIO.setmode(GPIO.BCM) # sets up the GPIO pins
        GPIO.setup(self.buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#sets pin mode for the buttons
        GPIO.setup(self.led, GPIO.OUT) #sets pin mode for the leds
        self.CatScreen = "Categories.gif"
        self.Gameover = None


    def setupGUI(self):
        # organize the GUI
        self.pack()
        Game.player_input = Entry(self, bg="white")

        Game.player_input.bind("<Return>", self.intermission)

        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)


        Game.text_frame = Frame(self, width=WIDTH / 2)


        Game.text = Text(Game.text_frame, bg="Red", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        Game.text_frame.pack(side=RIGHT, fill=Y)
        Game.text_frame.pack_propagate(True)

    def Text(self, text):
        Game.text.config(state=NORMAL)

        Game.text.delete("1.0", END)
        Game.text.insert(END, "Read this: " + text)
        Game.text.config(state=DISABLED)

    def screen(self, x):
        Game.img = PhotoImage(file = x)
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    def go(self):
        self.setupGUI()
        self.Text("")
        self.screen(self.CatScreen)



    def ButtonPressed(self): #function for easily sensing what button is pressed and retuning it (adapted form simon game)
        pressed = False
        while (not pressed):
                for i in range(len(self.buttons)):#saves the input of the user for checking later
                    while (GPIO.input(self.buttons[i]) == True):
                        pressed = True
                        ButtonPressed = self.buttons[i]

        return ButtonPressed

    def PlayGame(self):
        self.Text("Please select Category, uwu")
        self.update()
        wronganswers = 0
        #continues to run through the catagories and selections as long as there are less than three wrong answers
        GPIO.output(self.led[1], False) # red led off
        GPIO.output(self.led[0], False) # Green Led Off
        "display the catagory screen" #sotred at self.CatScreen
        currentCat = 0
        currentCat = self.ButtonPressed()

        if currentCat == self.buttons[0]: #subrutine for checking catagory one
            if (len(self.questions1) < 1): # Contingent for all questions in this catagory having been attempted
                self.Text("You've answered them all, guy. uwu")
                self.update()
                self.PlayGame()

            else:
                currentquestion = random.choice(self.questions1.keys()) # Picks a random question in the catagory list
                "display image stored in current question"
                self.screen(currentquestion)
                self.update()
                if self.ButtonPressed() == self.questions1[currentquestion]: # if the answer is right
                    del self.questions1[currentquestion] # deletes the question so it is not reused for this team
                    GPIO.output(self.led[1], True) # Green LED on
                    self.teams[self.currentteam] += 1 # adds points
                else:
                    del self.questions1[currentquestion]
                    self.Text("WROOONNNNGG! n\n\n\n\n\n\n\, uwu")
                    self.update()
                    GPIO.output(self.led[0], True) # Red LED on
                    wronganswers += 1 # adds a wrong answer to the counter

        elif currentCat == self.buttons[1]:#subrutine for checking catagory two
            if len(self.questions2) < 1: # Contingent for all questions in this catagory having been attempted
                print "You have answered all questions in this catagory, please select another catagory"
                self.update()
                self.PlayGame()

            else:
                currentquestion = random.choice(self.questions2.keys()) # Picks a random question in the catagory list
                "display image stored in current question"
                self.screen(currentquestion)
                self.update()
                if self.ButtonPressed() == self.questions2[currentquestion]: # if the answer is right
                    del self.questions2[currentquestion] # deletes the question so it is not reused for this team
                    GPIO.output(self.led[1], True) # Green LED on
                    self.teams[self.currentteam] += 1 # adds points
                else:
                    self.update()
                    del self.questions2[currentquestion]
                    GPIO.output(self.led[0], True) # Red LED on
                    wronganswers += 1 # adds a wrong answer to the counter

        elif currentCat == self.buttons[2]:#subrutine for checking catagory three
            if (len(self.questions3) < 1): # Contingent for all questions in this catagory having been attempted
                print "You have answered all questions in this catagory, please select another catagory"
                self.update()
                self.PlayGame()

            else:
                currentquestion = random.choice(self.questions3.keys()) # Picks a random question in the catagory list
                "display image stored in current question"
                self.screen(currentquestion)
                self.update()
                if self.ButtonPressed() == self.questions3[currentquestion]: # if the answer is right
                    del self.questions3[currentquestion] # deletes the question so it is not reused for this team
                    GPIO.output(self.led[1], True) # Green LED on
                    self.teams[self.currentteam] += 1 # adds points
                else:
                    self.update()
                    del self.questions3[currentquestion]
                    GPIO.output(self.led[0], True) # Red LED on
                    wronganswers += 1 # adds a wrong answer to the counter

        elif currentCat == self.buttons[3]:#subrutine for checking catagory four
            if (len(self.questions4) < 1): # Contingent for all questions in this catagory having been attempted
                print "You have answered all questions in this catagory, please select another catagory"
                self.update()
                self.PlayGame()

            else:
                currentquestion = random.choice(self.questions4.keys()) # Picks a random question in the catagory list
                "display image stored in current question"
                self.screen(currentquestion)
                self.update()
                if self.ButtonPressed() == self.questions4[currentquestion]: # if the answer is right
                    del self.questions4[currentquestion] # deletes the question so it is not reused for this team
                    GPIO.output(self.led[1], True) # Green LED on
                    self.teams[self.currentteam] += 1 # adds points
                    self.Text("CORRECCCTTT!")
                    self.update()
                else:
                    self.update()
                    del self.questions4[currentquestion]
                    GPIO.output(self.led[0], True) # Red LED on
                    wronganswers += 1 # adds a wrong answer to the counter

        else:
            GPIO.output(17, True) # Red LED on
            self.Text("Invalid Selection")
            self.update()
        GPIO.output(self.led[0], False) # Green LED off
        GPIO.output(self.led[1], True) # Red LED off
        "display game over screen" #stored at self.Gameover
        self.Text("Game Over!")
        self.update()
        sleep(5)
        Game.image.destroy()
        Game.text_frame.destroy()
        
        #GPIO.cleanup()

        self.go()

    #code for the game goes here

    def intermission(self, event):
        self.Text("Teem? ")
        self.update()
        self.currentteam = Game.player_input.get()
        self.teams[self.currentteam] = 0
    #allows for setup of teams and initial points
        Game.player_input.delete(0, END)
        Game.player_input.destroy()
        self.PlayGame()
####################################################################################################################
WIDTH = 800
HEIGHT = 600
window = Tk()
window.title("Wassup")
g = Game(window)
g.go()
window.mainloop()
