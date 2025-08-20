import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def update_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new task!")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to update!")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.resizable(False, False)

title_label = tk.Label(root, text="✅ My To-Do List", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Task", width=12, command=update_task)
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_button.grid(row=1, column=0, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear All", width=12, command=clear_tasks)
clear_button.grid(row=1, column=1, padx=5, pady=5)

tasks_listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 12), selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)
root.mainloop()
