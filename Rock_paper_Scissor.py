import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    result_text = ""

    if user_choice == computer_choice:
        result_text = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text = "You Win!"
        user_score += 1
    else:
        result_text = "You Lose!"
        computer_score += 1

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result_text}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score - You: 0 | Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="lightblue")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)


button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)


user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12), bg="lightblue")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12), bg="lightblue")
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="lightblue")
result_label.pack(pady=10)


score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="lightblue")
score_label.pack()
reset_button = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_button.pack(pady=20)

root.mainloop()
