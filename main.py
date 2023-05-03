import tkinter as tk
import string
import random
import sqlite3


def generate_password():
    length = length_scale.get()
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    password_display.config(text=password)


def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_display.cget("text")
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, password))
    conn.commit()
    conn.close()
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_display.config(text="")


def delete_password():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE password=?", (password_display.cget("text"),))
    conn.commit()
    conn.close()
    password_display.config(text="")

root = tk.Tk()
root.title("Passwort Generator | By HazeMC.de")

entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=10)

website_label = tk.Label(entry_frame, text="Website:")
website_label.grid(row=0, column=0)

website_entry = tk.Entry(entry_frame)
website_entry.grid(row=0, column=1)

username_label = tk.Label(entry_frame, text="Benutzername/Email:")
username_label.grid(row=1, column=0)

username_entry = tk.Entry(entry_frame)
username_entry.grid(row=1, column=1)

password_frame = tk.Frame(root)
password_frame.pack(padx=10, pady=10)

length_label = tk.Label(password_frame, text="Länge:")
length_label.grid(row=0, column=0)

length_scale = tk.Scale(password_frame, from_=8, to=32, orient=tk.HORIZONTAL, length=200)
length_scale.grid(row=0, column=1)

generate_button = tk.Button(password_frame, text="Passwort generieren", command=generate_password)
generate_button.grid(row=1, column=0, pady=10)

password_display = tk.Label(password_frame, text="", font=("Courier", 20))
password_display.grid(row=1, column=1)

action_frame = tk.Frame(root)
action_frame.pack(padx=10, pady=10)

save_button = tk.Button(action_frame, text="Passwort speichern", command=save_password)
save_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(action_frame, text="Passwort löschen", command=delete_password)
delete_button.grid(row=0, column=1, padx=10)

conn = sqlite3.connect("passwords.db")
c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS passwords (website TEXT, username TEXT, password TEXT)")
#c.execute("ALTER TABLE passwords ADD COLUMN website TEXT")
#c.execute("ALTER TABLE passwords ADD COLUMN username TEXT")

conn.commit()
conn.close()

root.mainloop()
