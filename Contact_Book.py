import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")
    
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        messagebox.showinfo("Contacts", "No contacts found.")
        return
    contact_list = ""
    for name, details in contacts.items():
        contact_list += f"{name} - {details['Phone']}\n"
    messagebox.showinfo("Contact List", contact_list)


def search_contact():
    search_term = simpledialog.askstring("Search", "Enter Name or Phone Number:")
    if not search_term:
        return
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term == details["Phone"]:
            info = f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}"
            messagebox.showinfo("Contact Found", info)
            found = True
            break
    if not found:
        messagebox.showerror("Not Found", "Contact not found!")


def update_contact():
    name = simpledialog.askstring("Update", "Enter the Name of the contact to update:")
    if name in contacts:
        phone = simpledialog.askstring("Input", "Enter New Phone Number:")
        email = simpledialog.askstring("Input", "Enter New Email:")
        address = simpledialog.askstring("Input", "Enter New Address:")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", f"Contact {name} updated successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the Name of the contact to delete:")
    if name in contacts:
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?")
        if confirm:
            del contacts[name]
            messagebox.showinfo("Deleted", f"Contact {name} deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")


root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

tk.Label(root, text="📒 Contact Book", font=("Arial", 18, "bold")).pack(pady=20)

tk.Button(root, text="➕ Add Contact", width=20, command=add_contact).pack(pady=5)
tk.Button(root, text="📋 View Contacts", width=20, command=view_contacts).pack(pady=5)
tk.Button(root, text="🔍 Search Contact", width=20, command=search_contact).pack(pady=5)
tk.Button(root, text="✏ Update Contact", width=20, command=update_contact).pack(pady=5)
tk.Button(root, text="🗑 Delete Contact", width=20, command=delete_contact).pack(pady=5)
tk.Button(root, text="❌ Exit", width=20, command=root.quit).pack(pady=20)

root.mainloop()
