import customtkinter 
import mysql.connector
from mysql.connector import errorcode
from win10toast import ToastNotifier
from tkinter import messagebox

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  # به درستی تنظیم کنید
    'port': '3306',       # به درستی تنظیم کنید
    'database': 'phone_book',
    'raise_on_warnings': True,
}

toaster = ToastNotifier()

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    print('connected successfully')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password🤔")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

def Add_Contact(name, number):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contacts (name, number) VALUES (%s, %s)", (name, number))
        connection.commit()
        print(f"Contact '{name}' added successfully!😉")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Wrapper function for adding a contact
def add_contact_ui():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:  # Check if both fields are filled
        Add_Contact(name, number)
    else:
        print("Please enter both name and number.")

# Function to remove a contact
def Remove_Contact(name_or_number):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE name = %s OR number = %s", (name_or_number, name_or_number))
        if cursor.rowcount > 0:
            connection.commit()
            print(f"Contact '{name_or_number}' removed successfully!😉")
        else:
            print("Contact not found!☹️")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


# Wrapper function for removing a contact
def remove_contact_ui():
    name_or_number = name_entry.get() or number_entry.get()
    if name_or_number:  # Check if the field is filled
        Remove_Contact(name_or_number)
    else:
        print("Please enter a name or number to remove.")

def Show_All_Contacts():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, number FROM contacts")
            results = cursor.fetchall()
            return results
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        toaster.show_toast("Error", f"Error: {err}")
        return []

def Search_Contact(name_or_number):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, number FROM contacts WHERE name = %s OR number = %s", (name_or_number, name_or_number))
            result = cursor.fetchone()
            return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        toaster.show_toast("Error", f"Error: {err}")
        return None

# User Interface
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
root = customtkinter.CTk()
root.geometry("500x750")
root.resizable(False, False)
root.iconbitmap("E:/My python projects/PhoneBook/PhoneBook ico.ico")
root.title("Phone Book")

def open_results_window(results):
    results_window = customtkinter.CTkToplevel(root)
    results_window.title('Results')
    results_window.geometry("400x400")

    results_text = customtkinter.CTkTextbox(master=results_window, width=380, height=360)
    results_text.pack(padx=10, pady=10)

    if results:
        for row in results:
            results_text.insert("end", f"Name: {row[0]}, Number: {row[1]}\n")
    else:
        results_text.insert("end", "No results found!☹️")

def open_search_window():
    name_or_number = name_entry.get() or number_entry.get()
    result = Search_Contact(name_or_number)
    if result:
        open_results_window([result])
    else:
        open_results_window([])

def open_show_all_window():
    results = Show_All_Contacts()
    open_results_window(results)

frame = customtkinter.CTkFrame(master =root)
frame.pack(padx=20, pady=60, fill='both', expand=True)

search_bar_label = customtkinter.CTkLabel(master=frame, text='My Phone Book', font=('calibri', 24))
search_bar_label.pack(padx=20, pady=60)

name_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Name', width=300)
name_entry.pack(padx=137, pady=10)

number_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Number', width=300)
number_entry.pack(padx=137, pady=10)

add_button = customtkinter.CTkButton(master=frame, text='Add', command=add_contact_ui)
add_button.pack(padx=137, pady=20)

remove_button = customtkinter.CTkButton(master=frame, text='Remove', command=remove_contact_ui)
remove_button.pack(padx=60, pady=20)

show_all_button = customtkinter.CTkButton(master=frame, text='Show All', command=open_show_all_window)
show_all_button.pack(padx=60, pady=20)

search_button = customtkinter.CTkButton(master=frame, text='Search', command=open_search_window)
search_button.pack(padx=60, pady=20)

def on_closing():
    connection.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()















