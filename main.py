import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully.")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found.")

# Setting up the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Creating a frame for the task entry and buttons
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Creating an entry widget for task input
task_entry = tk.Entry(input_frame, width=50)
task_entry.pack(side=tk.LEFT, padx=10)

# Creating a button to add a task
add_task_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

# Creating a listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Creating buttons for task management
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

remove_task_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_task_button.pack(side=tk.LEFT, padx=10)

save_tasks_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
save_tasks_button.pack(side=tk.LEFT, padx=10)

load_tasks_button = tk.Button(button_frame, text="Load Tasks", command=load_tasks)
load_tasks_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
