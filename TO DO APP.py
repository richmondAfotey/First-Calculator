import tkinter as tk
from tkinter import messagebox
import os

# File name for saving tasks
DATA_FILE = "tasks.txt"
todo_list = []

# ==========================================
# 1. CORE ENGINE FUNCTIONS (WITH FILE SAVING)
# ==========================================

def load_tasks():
    """Loads tasks from a text file when the app starts."""
    global todo_list
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                # Read lines and strip out the newline characters (\n)
                todo_list = [line.strip() for line in file.readlines() if line.strip()]
            update_listbox()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load tasks: {e}")

def save_tasks():
    """Saves the current todo_list to a text file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            for task in todo_list:
                file.write(f"{task}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save tasks: {e}")

def add_task_gui():
    task_name = task_entry.get()
    if task_name.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        todo_list.append(task_name)
        update_listbox()
        save_tasks()  # Auto-save changes
        task_entry.delete(0, tk.END)

def delete_task_gui():
    try:
        selected_index = task_listbox.curselection()[0]
        todo_list.pop(selected_index)
        update_listbox()
        save_tasks()  # Auto-save changes
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def complete_task_gui():
    try:
        selected_index = task_listbox.curselection()[0]
        if not todo_list[selected_index].startswith("[✓]"):
            todo_list[selected_index] = f"[✓] {todo_list[selected_index]}"
            update_listbox()
            save_tasks()  # Auto-save changes
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in todo_list:
        task_listbox.insert(tk.END, task)

# ==========================================
# 2. ADDITIONAL FEATURE: DARK MODE TOGGLE
# ==========================================
is_dark_mode = False

def toggle_dark_mode():
    global is_dark_mode
    if not is_dark_mode:
        # Switch to Dark Mode colors
        root.configure(bg="#212121")
        title_label.configure(bg="#212121", fg="white")
        task_listbox.configure(bg="#424242", fg="white", selectbackground="#616161")
        dark_mode_btn.configure(text="☀️ Light Mode", bg="#FFC107", fg="black")
        is_dark_mode = True
    else:
        # Switch back to Light Mode colors
        root.configure(bg="#F5F5F5")
        title_label.configure(bg="#F5F5F5", fg="black")
        task_listbox.configure(bg="white", fg="black", selectbackground="#E0E0E0")
        dark_mode_btn.configure(text="🌙 Dark Mode", bg="#37474F", fg="white")
        is_dark_mode = False

# ==========================================
# 3. BUILDING THE DESKTOP WINDOW
# ==========================================
root = tk.Tk()
root.title("Professional To-Do Planner")
root.geometry("400x530")
root.configure(bg="#F5F5F5")

# Header Title
title_label = tk.Label(root, text="My Tasks", font=("Arial", 18, "bold"), bg="#F5F5F5")
title_label.pack(pady=10)

# Input Section
task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=20, command=add_task_gui)
add_button.pack(pady=5)

# Visual List Box
task_listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=12, relief="flat", highlightthickness=1)
task_listbox.pack(pady=10)

# Action Buttons Frame
btn_frame = tk.Frame(root, bg="#F5F5F5")
btn_frame.pack(pady=5)

complete_button = tk.Button(btn_frame, text="Complete Task", font=("Arial", 11), bg="#2196F3", fg="white", width=12, command=complete_task_gui)
complete_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(btn_frame, text="Delete Task", font=("Arial", 11), bg="#F44336", fg="white", width=12, command=delete_task_gui)
delete_button.pack(side=tk.RIGHT, padx=10)

# Utility Button (Dark Mode)
dark_mode_btn = tk.Button(root, text="🌙 Dark Mode", font=("Arial", 10), bg="#37474F", fg="white", command=toggle_dark_mode)
dark_mode_btn.pack(pady=15)

# Load existing data at startup
load_tasks()

# Keep window alive
root.mainloop()
