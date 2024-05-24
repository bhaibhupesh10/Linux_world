import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import platform
import cv2
import pyttsx3
import pywhatkit
import paramiko
import tkinter as tk
from tkinter import messagebox
import subprocess as sp
import webbrowser
from hand_detection import detect_hand_landmarks
from email.message import EmailMessage
import ssl, smtplib
from twilio.rest import Client
from gtts import gTTS
import requests
from selenium import webdriver
import folium
import datetime
import time
import speech_recognition as sr
from PIL import Image
from transformers import AutoTokenizer
import matplotlib.pyplot as plt
import io
import uuid

def generate_image():
    # Create a blank image
    height, width = 600, 800
    beach_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Define colors
    sky_color = (255, 204, 153)
    ocean_color = (153, 204, 255)
    sand_color = (204, 204, 153)
    sun_color = (0, 255, 255)
    palm_trunk_color = (51, 25, 0)
    palm_leaf_color = (0, 153, 0)

    # Draw sky
    cv2.rectangle(beach_image, (0, 0), (width, int(height * 0.5)), sky_color, -1)

    # Draw ocean
    cv2.rectangle(beach_image, (0, int(height * 0.5)), (width, int(height * 0.75)), ocean_color, -1)

    # Draw sand
    cv2.rectangle(beach_image, (0, int(height * 0.75)), (width, height), sand_color, -1)

    # Draw sun
    cv2.circle(beach_image, (int(width * 0.8), int(height * 0.2)), 50, sun_color, -1)

    # Draw palm tree trunk
    trunk_bottom = (int(width * 0.2), int(height * 0.75))
    trunk_top = (int(width * 0.2), int(height * 0.5))
    cv2.line(beach_image, trunk_bottom, trunk_top, palm_trunk_color, 20)

    # Draw palm tree leaves
    leaf_length = 100
    for angle in range(0, 360, 45):
        angle_rad = np.radians(angle)
        leaf_end = (int(trunk_top[0] + leaf_length * np.cos(angle_rad)), int(trunk_top[1] + leaf_length * np.sin(angle_rad)))
        cv2.line(beach_image, trunk_top, leaf_end, palm_leaf_color, 10)

    # Display the beach image
    cv2.imshow('Beach Image', beach_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def start_notepad():
    result = sp.run("Notepad", shell=True)
    
    if result.returncode == 0:
        print("Notepad started successfully.")
    else:
        print(f"Failed to start Notepad. Return code: {result.returncode}")
    
    main()

def start_opera():
    result = sp.run(r'"C:\Users\BHUPESH CHOUDHARY\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Opera Browser.lnk"', shell=True)
  
    main()

def start_spotify():
    sp.run("Spotify", shell=True)
    main()

def open_url():
    url = input("-- Type the URL or website link to open in Web Browser -- \n")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    webbrowser.open(url)

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
    cap = cv2.VideoCapture(0)
    while True:
        status, photo = cap.read()
        cv2.imshow('My photo', photo[100:500, 100:500])  # Crop the video
        if cv2.waitKey(1) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()

def send_whatsapp_message():
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
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

def string_to_audio():
    text = input("Enter the text you want to convert to speech: ")
    if text.lower() == 'exit':
        return

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

def live_streaming():
    cap = cv2.VideoCapture(0)
    while True:
        status, photo = cap.read()
        cv2.imwrite("nikita.png", photo)
        cv2.imshow("meri photo", photo)
        if cv2.waitKey(100) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

def record_audio(duration, filename):
    fs = 44100  # Sample rate
    seconds = duration  # Duration of recording

    print("Recording...")
    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished

    print("Recording finished.")
    wav.write(filename, fs, my_recording)  # Save as WAV file

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def location_coordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except:
        print("Internet Not available")
        return False

def audio_to_text_image_generation():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
        
        HEADERS = {
            "Authorization": "",
            "Content-Type": "application/json",
        }

        tokenizer = AutoTokenizer.from_pretrained("gpt2")

        def generate_cover_art(input_text):
            try:
                input_text_with_suffix = f"Album Cover,Art,music album cover,{input_text}_{uuid.uuid4()}"
                tokenized_input = tokenizer(input_text_with_suffix, return_tensors="pt")
                input_str = tokenizer.decode(tokenized_input["input_ids"][0])
                payload = {"inputs": input_str}
                response = requests.post(API_URL, headers=HEADERS, json=payload, stream=True)
                response.raise_for_status()
                if response.content:
                    image = Image.open(io.BytesIO(response.content))
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                else:
                    print("Empty response from Hugging Face API")
            except requests.RequestException as e:
                print(f"Error in making request to Hugging Face API: {str(e)}")

        generate_cover_art(text)

def main():
    print("1: To Start Notepad")
    print("2: To Start Opera")
    print("3: To Start Spotify")
    print("4: Open a URL in Web Browser")
    print("5: Next options")
    print("6: Send SMS")
    print("7: Text to Speech")
    print("8: Open WhatsApp")
    print("9: Coordinates")
    print("10: Audio to Text Image Generation")
    print("\n")

    total_fingers = detect_hand_landmarks()
    total_fingers = str(total_fingers)
    
    if total_fingers == '1':
        start_notepad()
    elif total_fingers == '2':
        start_opera()
    elif total_fingers == '3':
        start_spotify()
    elif total_fingers == '4':
        open_url()
    elif total_fingers == '5':
        print("Welcome to the Next Options!")
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
            elif choice.lower() == "string to audio":
                string_to_audio()
            elif choice.lower() == "live streaming":
                live_streaming()
            elif choice.lower() == "record audio":
                duration = int(input("Enter duration of recording in seconds: "))
                filename = input("Enter filename to save recording: ")
                record_audio(duration, filename)
            elif choice.lower() == "print multiplication table":
                number = int(input("Enter number: "))
                print_multiplication_table(number)
            elif choice.lower() == "menu":
                print("Thank you for using the Application Launcher. Goodbye!")
                main()
            else:
                print("Invalid choice. Please enter a valid program name or 'exit'.")
    elif total_fingers == '6':
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='',
            to='',
            body='Your message here'
        )
        print(message.sid)
    elif total_fingers == '7':
        Text_to_convert = input("Text to convert: ")
        language = 'en'
        speech = gTTS(text=Text_to_convert, lang=language, slow=False)
        speech.save("output.mp3")
        os.system("start output.mp3")
    elif total_fingers == '8':
        pywhatkit.sendwhatmsg_instantly("Number", "Hi! This is an auto-generated message from pywhatkit", 10, tab_close=True)
    elif total_fingers == '9':
        lat, long, city, state = location_coordinates()
        if lat and long:
            print(f'The coordinates and location are: {lat}, {long}, {city}, {state}')
    elif total_fingers == '10':
        audio_to_text_image_generation()
    else:
        print("\t\tInvalid Choice!")

if __name__ == "__main__":
    main()
