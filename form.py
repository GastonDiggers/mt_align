import tkinter as tk
from tkinter import filedialog, ttk

from target_to_source import translate_files

def select_input_folder():
    input_folder.set(filedialog.askdirectory())

def select_output_folder():
    output_folder.set(filedialog.askdirectory())

root = tk.Tk()
root.geometry('400x200')  # Set the size of the window

input_folder = tk.StringVar()
output_folder = tk.StringVar()

# Assume these are the languages you support
languages = ['en', 'zh', 'es', 'ar', 'hi', 'bn', 'pt', 'ru', 'ja', 'pa', 'de', 'jv', 'mr', 'fr', 'ta', 'vi', 'te', 'ko', 'mr', 'it']

input_language = tk.StringVar(value=languages[0])
output_language = tk.StringVar(value=languages[0])

tk.Label(root, text="Select Input Folder:").grid(row=0, column=0, sticky='w')
input_button = tk.Button(root, text="Browse", command=select_input_folder)
input_button.grid(row=0, column=1)

input_label = tk.Label(root, textvariable=input_folder)
input_label.grid(row=1, column=0, columnspan=2)

output_label = tk.Label(root, textvariable=output_folder)
output_label.grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Select Input Language:").grid(row=4, column=0, sticky='w')
input_language_menu = ttk.Combobox(root, textvariable=input_language, values=languages)
input_language_menu.grid(row=4, column=1)

tk.Label(root, text="Select Output Language:").grid(row=5, column=0, sticky='w')
output_language_menu = ttk.Combobox(root, textvariable=output_language, values=languages)
output_language_menu.grid(row=5, column=1)

run_button = tk.Button(root, text="Run Script", command=lambda: translate_files(input_folder.get(), input_language.get(), output_language.get()))
run_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
