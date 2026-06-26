def load_tasks():
    """Loads tasks from a text file when the app starts."""
    global todo_list
    if os.path.exists(DATA_FILE):
        try:
            # ADDED: encoding="utf-8"
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                todo_list = [line.strip() for line in file.readlines() if line.strip()]
            update_listbox()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load tasks: {e}")

def save_tasks():
    """Saves the current todo_list to a text file."""
    try:
        # ADDED: encoding="utf-8"
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            for task in todo_list:
                file.write(f"{task}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save tasks: {e}")