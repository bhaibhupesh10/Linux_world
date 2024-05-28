import cv2
import numpy as np
import socket
import sys
import pickle
import struct

# Initialize video capture from the default webcam
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server on the specified host and port
clientsocket.connect(('localhost', 8089))

data = b''
payload_size = struct.calcsize("L")  # unsigned long integer

while True:
    try:
        # Send client stream
        ret, frame = video.read()
        if not ret:
            break

        clientdata = pickle.dumps(frame)
        message_size = struct.pack("L", len(clientdata))
        clientsocket.sendall(message_size + clientdata)

        # Receive server stream
        while len(data) < payload_size:
            data += clientsocket.recv(4096)
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += clientsocket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        cv2.imshow('receiver_frame', frame)

        # Exit if 'ESC' key is pressed
        if cv2.waitKey(1) == 27:
            print("You closed the window.")
            clientsocket.shutdown(socket.SHUT_RDWR)
            clientsocket.close()
            cv2.destroyAllWindows()
            break
    except Exception as e:
        cv2.destroyAllWindows()
        print(f"An error occurred: {e}")
        break

video.release()
