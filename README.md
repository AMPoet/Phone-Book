# Phone Book Application with Python and MySQL

This project is a powerful and user-friendly **Phone Book Application** developed using **Python**, **CustomTkinter**, and **MySQL**. It enables you to add, remove, search, and display contacts seamlessly, making it an ideal tool for learning and applying modern desktop application development techniques.

## Features

- **Add Contacts**: Insert a new contact with a name and phone number into the MySQL database.
- **Remove Contacts**: Delete contacts by name or phone number.
- **Search Contacts**: Quickly find a contact using either the name or phone number.
- **Display All Contacts**: View a complete list of contacts in a modern graphical interface.
- **Modern User Interface**: Built with CustomTkinter featuring dark mode and a sleek design.
- **Desktop Notifications**: Utilizes Win10Toast to display system notifications on Windows.

## Technologies and Libraries

- **Python 3.x**: The core programming language.
- **CustomTkinter**: For creating an attractive and modern graphical user interface.
- **MySQL**: The database system used to store contact information.
- **mysql-connector-python**: To connect and interact with the MySQL database.
- **Win10Toast**: For displaying Windows toast notifications.

## Installation and Setup

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/)
- pip package manager for Python

### Install Required Libraries

Run the following commands in your terminal or command prompt:

```bash
pip install customtkinter mysql-connector-python win10toast
```

```bash
pip install win10toast
```

### Database Configuration

Ensure that your database configuration in the code is set correctly. For example:

```python
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  # Adjust as needed
    'port': 'your port',       # Adjust as needed
    'database': 'phone_book',
    'raise_on_warnings': True,
}
```

> **Note:** Before running the application, make sure to create the `phone_book` database and the `contacts` table in MySQL.

### Running the Application

To run the application, execute the main Python file (e.g., `main.py`):

```bash
python main.py
```

## How to Use

1. **Add a Contact**: Enter the contact's name and phone number in the respective fields, then click the **Add** button.
2. **Remove a Contact**: Input the name or phone number of the contact you wish to remove and click the **Remove** button.
3. **Search a Contact**: Type in the name or phone number and click the **Search** button to find the desired contact.
4. **Show All Contacts**: Click the **Show All** button to view all contacts in a new window.

## Important Notes

- Ensure that your MySQL connection is active and configured correctly.
- Any errors during execution will be displayed in the terminal and through Windows toast notifications.
- Verify that the `contacts` table exists in your `phone_book` database before running the application.

## SEO Keywords

**Python**, **Phone Book Application**, **MySQL**, **CustomTkinter**, **Desktop Application**, **Contact Management**, **Python Project**, **HiTech**, **GUI Development**, **Python Tutorial**, **Desktop Notifications**

## Conclusion

This project is an excellent example of how Python can be used to build modern desktop applications with a sleek user interface and robust database management using MySQL. It is perfect for developers looking to enhance their programming, UI design, and data management skills. Customize the application to suit your needs and enjoy building innovative solutions with Python!


```
