# number_guessing_game_works_now.py
import random
import tkinter as tk
from tkinter import messagebox

# Game setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x650")
root.configure(bg="#2c3e50")
root.resizable(False, False)

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

# Title
tk.Label(
    root,
    text="Guess the Number!",
    font=("Helvetica", 32, "bold"),
    bg="#2c3e50",
    fg="#ecf0f1"
).pack(pady=40)

tk.Label(
    root,
    text="I picked a number between 1 and 100\nYou have 10 attempts!",
    font=("Helvetica", 16),
    bg="#2c3e50",
    fg="#bdc3c7"
).pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Helvetica", 24), justify="center", width=10)
entry.pack(pady=30)
entry.focus()

# Hint label
hint = tk.Label(root, text="Make your first guess!", font=("Helvetica", 18), bg="#2c3e50", fg="#f1c40f")
hint.pack(pady=20)

# Attempts
attempts_label = tk.Label(root, text="Attempts: 0/10", font=("Helvetica", 16), bg="#2c3e50", fg="#e74c3c")
attempts_label.pack(pady=10)

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}/10")

        if guess < secret_number:
            hint.config(text="Too low! Try higher", fg="#e67e22")
        elif guess > secret_number:
            hint.config(text="Too high! Try lower", fg="#e67e22")
        else:
            messagebox.showinfo("Winner!", f"You got it! The number was {secret_number}\nAttempts used: {attempts}")
            reset_game()
            return

        if attempts >= max_attempts:
            messagebox.showwarning("Game Over", f"No attempts left!\nThe number was {secret_number}")
            reset_game()

    except ValueError:
        hint.config(text="Please enter a valid number!", fg="#e74c3c")
        
    entry.delete(0, tk.END)

def reset_game():
    global secret_number, attempts
    if messagebox.askyesno("Play Again?", "Want to play again?"):
        secret_number = random.randint(1, 100)
        attempts = 0
        attempts_label.config(text="Attempts: 0/10")
        hint.config(text="New game started! Good luck!", fg="#2ecc71")
        entry.delete(0, tk.END)
    else:
        root.quit()

# Buttons & Enter key
tk.Button(
    root,
    text="GUESS",
    font=("Helvetica", 20, "bold"),
    bg="#27ae60",
    fg="white",
    activebackground="#2ecc71",
    command=check_guess
).pack(pady=20)

root.bind("<Return>", lambda event: check_guess())
root.mainloop()