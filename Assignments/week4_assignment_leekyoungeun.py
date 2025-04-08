import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Step-Based Progress")
root.geometry("400x500")

steps = ["Step1/5", "Step2/5", "Step3/5", "Step4/5", "Step5/5"]
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

status_label=tk.Label(root, text="Waiting...")
status_label.pack()

progress["maximum"]=10

def run_steps():
    for i in range(10):
        if i % 2==0:
            status_label.config(text=steps[i//2])
        progress.step(1)
        root.update()
        time.sleep(1)


start_button = tk.Button(root, text="Start", command=run_steps)
start_button.pack(pady=20)

root.mainloop()