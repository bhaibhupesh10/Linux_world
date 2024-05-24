import os
import platform
import cv2
import pyttsx3
import pywhatkit
import paramiko
import tkinter as tk
from tkinter import messagebox

def open_web_browser():
    os_platform = platform.system()
    if os_platform == "Windows":
        os.system("start chrome")
    elif os_platform == "Darwin":
        os.system("open -a Safari")
    else:
        os.system("xdg-open http://www.google.com")

def open_text_editor():
    os_platform = platform.system()
    if os_platform == "Windows":
        os.system("start notepad")
    elif os_platform == "Darwin":
        os.system("open -a TextEdit")
    else:
        os.system("gedit")

def open_terminal():
    os_platform = platform.system()
    if os_platform == "Windows":
        os.system("start cmd")
    elif os_platform == "Darwin":
        os.system("open -a Terminal")
    else:
        os.system("gnome-terminal")

def open_file_manager():
    os_platform = platform.system()
    if os_platform == "Windows":
        os.system("explorer")
    elif os_platform == "Darwin":
        os.system("open .")
    else:
        os.system("nautilus")

def capture_photo():
    cap = cv2.VideoCapture(2)
    while True:
        status, photo = cap.read()
        cv2.imshow('My photo', photo[100:500, 100:500]) # to crop the video
        if cv2.waitKey(1 )== 13:
            break
    cv2.destroyAllWindows()
    cap.release()

def send_whatsapp_message():
    hour = int(input("Enter hour"))
    minute = int(input("Enter minute"))
    pywhatkit.sendwhatmsg("+917489356891", "Hi this is Bhupesh", hour, minute)

def execute_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    return output if not error else error

def connect_to_linux():
    hostname = '192.168.56.102'
    port = 22
    username = 'root'
    password = '7750'

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, port, username, password)
        commands = [
            'ls -l',
            'uname -a',
            'whoami',
        ]

        for command in commands:
            print(f"Executing command: {command}")
            result = execute_command(ssh_client, command)
            print("Result:")
            print(result)

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as ssh_exc:
        print(f"SSH error: {ssh_exc}")
    finally:
        ssh_client.close()

def generate_image():
    # Your code to generate an image
    pass

def open_python_form():
    def submit_form():
        name = name_entry.get()
        contact_no = contact_no_entry.get()
        email_id = email_id_entry.get()
        whatsapp_no = whatsapp_no_entry.get()

        if not name or not contact_no or not email_id or not whatsapp_no:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        print(f"Name: {name}")
        print(f"Contact No: {contact_no}")
        print(f"Email ID: {email_id}")
        print(f"WhatsApp No: {whatsapp_no}")

        name_entry.delete(0, tk.END)
        contact_no_entry.delete(0, tk.END)
        email_id_entry.delete(0, tk.END)
        whatsapp_no_entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Inquiry Form")

    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Contact No:").grid(row=1, column=0, padx=10, pady=5)
    contact_no_entry = tk.Entry(root)
    contact_no_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Email ID:").grid(row=2, column=0, padx=10, pady=5)
    email_id_entry = tk.Entry(root)
    email_id_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="WhatsApp No:").grid(row=3, column=0, padx=10, pady=5)
    whatsapp_no_entry = tk.Entry(root)
    whatsapp_no_entry.grid(row=3, column=1, padx=10, pady=5)

    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.grid(row=4, columnspan=2, pady=10)

    root.mainloop()

def main():
    print("Welcome to the Application Launcher!")
    print("Enter the name of the program you want to open or 'exit' to quit.")

    while True:
        choice = input("Enter your choice: ")

        if choice.lower() == "web browser":
            open_web_browser()
        elif choice.lower() == "text editor":
            open_text_editor()
        elif choice.lower() == "terminal":
            open_terminal()
        elif choice.lower() == "file manager":
            open_file_manager()
        elif choice.lower() == "capture photo":
            capture_photo()
        elif choice.lower() == "send whatsapp message":
            send_whatsapp_message()
        elif choice.lower() == "connect to linux":
            connect_to_linux()
        elif choice.lower() == "generate image":
            generate_image()
        elif choice.lower() == "open python form":
            open_python_form()
        elif choice.lower() == "exit":
            print("Thank you for using the Application Launcher. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid program name or 'exit'.")

if __name__ == "__main__":
    main()
