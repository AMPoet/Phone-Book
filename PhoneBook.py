import customtkinter 
import mysql.connector
from mysql.connector import errorcode
from win10toast import ToastNotifier

config = {
    'user': 'root',
    'password': 'root',
    'host': 'your host',
    'port': 'your port',
    'database': 'phone_book',
    'raise_on_warnings': True,
}

toaster=ToastNotifier

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

def Show_All_Contacts():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, number FROM contacts")
        results = cursor.fetchall()
        if not results:
            print("No contacts available☹️")
        else:
            for row in results:
                print(f"Name: {row[0]}, Number: {row[1]}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def Search_Contact(name_or_number):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, number FROM contacts WHERE name = %s OR number = %s", (name_or_number, name_or_number))
        result = cursor.fetchone()
        if result:
            print(f"Name: {result[0]}, Number: {result[1]}")
        else:
            print("Contact Not Found!☹️")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# User Interface
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
root = customtkinter.CTk()
root.geometry("500x750")
root.resizable(False, False)
root.title("Phone Book")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=60, fill='both', expand=True)

search_bar_label = customtkinter.CTkLabel(master=frame, text='My Phone Book', font=('calibri', 24))
search_bar_label.pack(padx=20, pady=60)

name_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Name', width=300)
name_entry.pack(padx=137, pady=10)

number_entry = customtkinter.CTkEntry(master=frame, placeholder_text='Number', width=300)
number_entry.pack(padx=137, pady=10)

def add_contact_ui():
    name = name_entry.get()
    number = number_entry.get()
    Add_Contact(name, number)

def remove_contact_ui():
    name_or_number = name_entry.get() or number_entry.get()
    Remove_Contact(name_or_number)

def show_all_contacts_ui():
    Show_All_Contacts()

def search_contact_ui():
    name_or_number = name_entry.get() or number_entry.get()
    Search_Contact(name_or_number)

add_button = customtkinter.CTkButton(master=frame, text='Add', command=add_contact_ui)
add_button.pack(padx=137, pady=20)

remove_button = customtkinter.CTkButton(master=frame, text='Remove', command=remove_contact_ui)
remove_button.pack(padx=60, pady=20)

show_all_button = customtkinter.CTkButton(master=frame, text='Show All', command=show_all_contacts_ui)
show_all_button.pack(padx=60, pady=20)

search_button = customtkinter.CTkButton(master=frame, text='Search', command=search_contact_ui)
search_button.pack(padx=60, pady=20)

root.mainloop()

connection.close()



















