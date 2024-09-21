import tkinter as tk
from tkinter import messagebox

# Contact storage (in-memory dictionary)
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['Phone']:
            contact_list.delete(0, tk.END)
            contact_list.insert(tk.END, f"{name} - {details['Phone']}")
            found = True
    if not found:
        messagebox.showinfo("No Results", "No contact found.")
    contact_list.pack(fill="both", padx=10, pady=10)

# Function to update a contact
def update_contact():
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected[0]).split(" - ")[0]
        if name in contacts:
            contacts[name] = {'Phone': phone_entry.get(), 'Email': email_entry.get(), 'Address': address_entry.get()}
            messagebox.showinfo("Success", "Contact updated successfully!")
            display_contacts()
            clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")
    else:
        messagebox.showerror("Error", "Select a contact to update.")

# Function to delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected[0]).split(" - ")[0]
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            display_contacts()
            clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")
    else:
        messagebox.showerror("Error", "Select a contact to delete.")

# Function to clear the input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to fill contact details for editing
def fill_fields(event):
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected[0]).split(" - ")[0]
        details = contacts[name]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, details['Phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, details['Email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, details['Address'])

# Function to display all contacts (used after update or delete)
def display_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Center the window
def center_window(root, width=600, height=500):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (width / 2))
    y_cordinate = int((screen_height / 2) - (height / 2))
    root.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

# UI setup
root = tk.Tk()
root.title("Contact Manager")
root.config(bg="#F5F5F5")

# Center the window
center_window(root, 600, 500)

# Styles for labels, buttons, and entries
label_style = {"bg": "#333333", "fg": "white", "font": ("Helvetica", 12)}
button_style = {"bg": "#1976D2", "fg": "white", "font": ("Helvetica", 10, "bold"), "bd": 2, "relief": "raised"}
entry_style = {"font": ("Helvetica", 12), "bd": 2, "relief": "solid"}

# Labels for input fields
input_frame = tk.Frame(root, bg="#F5F5F5")
input_frame.pack(pady=20)

tk.Label(input_frame, text="Name", **label_style).grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Label(input_frame, text="Phone", **label_style).grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Label(input_frame, text="Email", **label_style).grid(row=2, column=0, padx=10, pady=10, sticky="w")
tk.Label(input_frame, text="Address", **label_style).grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Entry fields for input
name_entry = tk.Entry(input_frame, **entry_style)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

phone_entry = tk.Entry(input_frame, **entry_style)
phone_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

email_entry = tk.Entry(input_frame, **entry_style)
email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

address_entry = tk.Entry(input_frame, **entry_style)
address_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Buttons for actions
button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Contact", **button_style, command=add_contact).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Update Contact", **button_style, command=update_contact).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Delete Contact", **button_style, command=delete_contact).grid(row=0, column=2, padx=10, pady=10)
tk.Button(button_frame, text="Clear Fields", **button_style, command=clear_entries).grid(row=0, column=3, padx=10, pady=10)

# Search functionality
search_frame = tk.Frame(root, bg="#F5F5F5")
search_frame.pack(pady=20)

tk.Label(search_frame, text="Search", **label_style).grid(row=0, column=0, padx=10, pady=10, sticky="w")
search_entry = tk.Entry(search_frame, **entry_style)
search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
tk.Button(search_frame, text="Search", **button_style, command=search_contact).grid(row=0, column=2, padx=10, pady=10)

# Contact list display (hidden by default)
contact_list = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12), bg="#E3F2FD", bd=2, relief="solid")
contact_list.bind('<<ListboxSelect>>', fill_fields)

# Hide contact list until searched
contact_list.pack_forget()

# Start the Tkinter loop
root.mainloop()
