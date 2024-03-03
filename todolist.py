import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Please enter a task.")

def remove_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Please select a task to remove.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def main():
    global entry_task, listbox_tasks

    root = tk.Tk()
    root.title("To-Do List")

    frame_tasks = tk.Frame(root)
    frame_tasks.pack(pady=10)

    listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, border=0)
    listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar_tasks = tk.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    entry_task = tk.Entry(root, width=50)
    entry_task.pack()

    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=5)

    button_add_task = tk.Button(frame_buttons, text="Add Task", width=20, command=add_task)
    button_add_task.pack(side=tk.LEFT)

    button_remove_task = tk.Button(frame_buttons, text="Remove Task", width=20, command=remove_task)
    button_remove_task.pack(side=tk.LEFT)

    button_clear_tasks = tk.Button(frame_buttons, text="Clear Tasks", width=20, command=clear_tasks)
    button_clear_tasks.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
