        
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
import ssl,smtplib
from twilio.rest import Client
from gtts import gTTS
import os 

import requests
from selenium import webdriver
import folium
import datetime
import time
from twilio.rest import Client
import speech_recognition as sr

import pywhatkit
        

import requests
from PIL import Image
from transformers import AutoTokenizer
import matplotlib.pyplot as plt
import io
import uuid

def start_notepad():
    sp.run("Notepad", shell=True)

def start_opera():
    sp.run(r'"C:\Users\arpit\AppData\Local\Programs\Opera GX\launcher.exe"', shell=True)

def start_spotify():
    sp.run("Spotify", shell=True)

def open_url():
    url = input("-- Type the URL or website link to open in Web Browser -- \n")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    webbrowser.open(url)

def main():
    print(" 1: To Start Notepad")
    print(" 2: To Start opera")
    print(" 3: To Start Spotify")
    print(" 4: If ask input which url to open in browser, and when we give url, it open that website in browser")
    print(" 5: To next ")
    print(" 6: To SMS")
    print(" 7: To Text to Speech")
    print(" 8: To open WhatsApp")
    print(" 9: Coordinates")
    print("10: audio_to_text_image_generation")
    print("\n")
    
    total_fingers = detect_hand_landmarks()
    total_fingers=str(total_fingers)
    if total_fingers == '1':
        start_notepad()
    elif total_fingers == '2':
        start_opera()
    elif total_fingers == '3':
        start_spotify()
    elif total_fingers == '4':
        open_url()
    elif total_fingers == '5':
        

def to_next():
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
    #-------------------------------------------------

    def calculate_bmi(weight, height):
        """
        Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
        Return the BMI value and the corresponding category.
        """
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

    def calculate_bmi(weight, height):
        """
        Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
        Return the BMI value and the corresponding category.
        """
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

    def main():
    # Predefined weight and height
        weight = 70  # Weight in kilograms
        height = 1.75  # Height in meters

    # Calculate BMI
        bmi, category = calculate_bmi(weight, height)

    # Print the results
        print("BMI Calculator")
        print(f"Weight: {weight} kg")
        print(f"Height: {height} m")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")



    def record_audio(duration, filename):
        """
        Records audio for a given duration and saves it to a specified file.
    
        Args:
        duration (int): Duration of the recording in seconds.
        filename (str): The name of the file to save the recording to.
        """
        fs = 44100  # Sample rate
        seconds = duration  # Duration of recording

        print("Recording...")
        my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished

        print("Recording finished.")
        wav.write(filename, fs, my_recording)  # Save as WAV file

    def main():
        duration = int(input("Enter duration of recording in seconds: "))
        filename = input("Enter filename to save recording: ")
        record_audio(duration, filename)







    def print_multiplication_table(n):
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")


   


    #---------------------------------

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
            elif choice.lower() == "string to audio":
                string_to_audio()
            elif choice.lower() == "live streaming":
                live_streaming()
       
            elif choice.lower() == "record audio":
                record_audio(5, 'test_recording.wav')
            elif choice.lower() == "2":
            print_multiplication_table(2)

            elif choice.lower() == "exit":
                print("Thank you for using the Application Launcher. Goodbye!")
            #----------------------------
                break
            else:
                print("Invalid choice. Please enter a valid program name or 'exit'.")


    elif total_fingers == '6':

        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='',
        to=''
        )

        print(message.sid)
    elif total_fingers == '7':
        Text_to_convert = input("Text to convert:")

        language = 'en'

        speech = gTTS(text=Text_to_convert, lang= language,slow=False)

        speech.save("sagemaker.mp3")

        os.system("start sagemaker.mp3")

    elif total_fingers == '8':
        pywhatkit.sendwhatmsg_instantly("Number","Hi ! arpit this is a auto generated msg from pywhatkit",10,tab_close=True)

    elif total_fingers == '9':
        
        def locationCoordinates():
            try:
                response = requests.get('https://ipinfo.io')
                data = response.json()
                loc = data['loc'].split(',')
                lat, long = float(loc[0]), float(loc[1])
                city = data.get('city', 'Unknown')
                state = data.get('region', 'Unknown')
                return lat, long, city, state
                
            except:
                print("Internet Not avialable")
                exit()
                return False


        print("---------------GPS Using Python---------------\n")

        lat, long, city, state = locationCoordinates()
        print(f'the coordinates and location is: {lat}, {long}, {city}, {state}')

    elif total_fingers == '10':
        recognizer = sr.Recognizer()

        # Capture audio from the microphone
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

            # Load tokenizer
            tokenizer = AutoTokenizer.from_pretrained("gpt2")

            def generate_cover_art(input_text):
                try:
                    # Introduce variability in input text
                    input_text_with_suffix = f"Album Cover,Art,music album cover,{input_text}_{uuid.uuid4()}"

                    # Tokenize the input text
                    tokenized_input = tokenizer(input_text_with_suffix, return_tensors="pt")

                    # Convert the tokenized values back to string
                    input_str = tokenizer.decode(tokenized_input["input_ids"][0])

                    payload = {"inputs": input_str}
                    response = requests.post(API_URL, headers=HEADERS, json=payload, stream=True)
                    response.raise_for_status()

                    if response.content:
                        # Display the image
                        image = Image.open(io.BytesIO(response.content))
                        plt.imshow(image)
                        plt.axis('off')
                        plt.show()
                    else:
                        print("Empty response from Hugging Face API")
                except requests.RequestException as e:
                    print(f"Error in making request to Hugging Face API: {str(e)}")
            # Example usage
            input_text = text
            generate_cover_art(input_text)


    else:
        print("\t\tInvalid Choice!")

if __name__ == "__main__":
    main()