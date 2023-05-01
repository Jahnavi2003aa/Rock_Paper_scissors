#first save pictures of paper,rock,scissors from last slide
#copy the path of the pictures in your laptop/pc
#paste it at rock_img,paper_img,scissor_img and importantly replace'\'with '/'
#enjoy the game
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="lightsalmon")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="lightsalmon")
comp_label = Label(root, image=scissor_img_comp, bg="lightsalmon")
comp_label.grid(row=1, column=4)
user_label.grid(row=1, column=0)


# scores
playerScore = Label(root, text=0, font=100, bg="lightsalmon", fg="black")
computerScore = Label(root, text=0, font=100, bg="lightsalmon", fg="black")
computerScore.grid(row=1, column=3)
playerScore.grid(row=1, column=1)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="lightsalmon", fg="black")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="lightsalmon", fg="black")
user_indicator.grid(row=0, column=1)
comp_indicator.grid(row=0, column=3)

# messages
msg = Label(root, font=50, bg="lightsalmon", fg="black")
msg.grid(row=4, column=2)

# update message


def updateMessage(x):
    msg['text'] = x

# update user score


def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score


def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner


def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


# update choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


# buttons
rocks = Label(root, image=rock_img, bg="lightsalmon")
rocks.grid(row=2, column=1)
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="black", command=lambda: updateChoice("rock")).grid(row=3, column=1)
papers = Label(root, image=paper_img, bg="lightsalmon")
papers.grid(row=2, column=2)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="black", command=lambda: updateChoice("paper")).grid(row=3, column=2)
scs = Label(root, image=scissor_img_comp, bg="lightsalmon")
scs.grid(row=2, column=3)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="black", command=lambda: updateChoice("scissor")).grid(row=3, column=3)

root.mainloop()
