import tkinter as tk
from tkinter import ttk
import re
import pyperclip  # Module for copying text to clipboard

def extract_credit_card_info(text):
    # Regular expressions to match credit card information
    card_number_regex = r'\b(?:\d[ -]*?){13,16}\b'
    date_regex = r'\b\d{2}/\d{2}\b'  # Updated regex for date format MM/YY
    cvv_regex = r'\b\d{3}\b'

    card_numbers = re.findall(card_number_regex, text)
    dates = re.findall(date_regex, text)
    cvvs = re.findall(cvv_regex, text)

    return card_numbers, dates, cvvs

def separate_info(event=None):
    text = text_entry.get("1.0", "end-1c")
    card_numbers, dates, cvvs = extract_credit_card_info(text)

    card_number_text.delete("1.0", "end")
    date_text.delete("1.0", "end")
    cvv_text.delete("1.0", "end")

    for card_number in card_numbers:
        card_number_text.insert("end", card_number + "\n")
    for date in dates:
        date_text.insert("end", date + "\n")
    for cvv in cvvs:
        cvv_text.insert("end", cvv + "\n")
    
    status_label.config(text="Data extracted successfully!", foreground="green")

def copy_text(text_widget):
    text = text_widget.get("1.0", "end-1c")
    pyperclip.copy(text)

# Create the main window
root = tk.Tk()
root.title("CardSplitter: Credit Card Info Extractor")
root.geometry("700x400")

# Style
style = ttk.Style()
style.theme_use("clam")  # Change the theme if needed

# Text entry for user input
text_entry_frame = ttk.Frame(root, padding=10)
text_entry_frame.pack(fill="both", expand=True)
text_entry_label = ttk.Label(text_entry_frame, text="Paste or type text here:")
text_entry_label.pack(anchor="w")
text_entry = tk.Text(text_entry_frame, height=5, width=50)
text_entry.pack(fill="both", expand=True)

# Bind paste event to the text entry
text_entry.bind("<Control-v>", separate_info)

# Button to trigger extraction
extract_button = ttk.Button(root, text="Extract Info", command=separate_info)
extract_button.pack(pady=5)

# Display areas for separated information with copy buttons
info_frame = ttk.Frame(root)
info_frame.pack(fill="both", expand=True, pady=5)

card_number_frame = ttk.Frame(info_frame)
card_number_frame.pack(side="left", padx=5)
card_number_label = ttk.Label(card_number_frame, text="Card Numbers:")
card_number_label.pack(anchor="w")
card_number_text = tk.Text(card_number_frame, height=5, width=25)
card_number_text.pack(side="left", fill="both", expand=True)
card_number_copy_button = ttk.Button(card_number_frame, text="Copy", command=lambda: copy_text(card_number_text))
card_number_copy_button.pack(pady=5)

date_frame = ttk.Frame(info_frame)
date_frame.pack(side="left", padx=5)
date_label = ttk.Label(date_frame, text="Dates:")
date_label.pack(anchor="w")
date_text = tk.Text(date_frame, height=5, width=15)
date_text.pack(side="left", fill="both", expand=True)
date_copy_button = ttk.Button(date_frame, text="Copy", command=lambda: copy_text(date_text))
date_copy_button.pack(pady=5)

cvv_frame = ttk.Frame(info_frame)
cvv_frame.pack(side="left", padx=5)
cvv_label = ttk.Label(cvv_frame, text="CVVs:")
cvv_label.pack(anchor="w")
cvv_text = tk.Text(cvv_frame, height=5, width=10)
cvv_text.pack(side="left", fill="both", expand=True)
cvv_copy_button = ttk.Button(cvv_frame, text="Copy", command=lambda: copy_text(cvv_text))
cvv_copy_button.pack(pady=5)

# Status label
status_label = ttk.Label(root, text="", foreground="green")
status_label.pack(pady=5)

root.mainloop()
