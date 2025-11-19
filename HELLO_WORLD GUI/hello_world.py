# hello_tkinter.py
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World")
root.geometry("400x300")
root.resizable(False, False)

# Optional: center the window on screen
root.eval('tk::PlaceWindow . center')

# Big centered label
label = tk.Label(
    root,
    text="Hello World!",
    font=("Segoe UI", 28, "bold"),
    foreground="#0066CC"
)
label.pack(expand=True)

# Run the app
root.mainloop()