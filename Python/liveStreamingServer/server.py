import cv2
import pickle
import socket
import struct

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8089))
server_socket.listen(10)  # Listen for incoming connections

print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connection from: {addr}")

data = b''
payload_size = struct.calcsize("L")

# Capture video from the webcam
video = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    try:
        # Read a frame from the webcam
        ret, frame = video.read()
        if not ret:
            break

        # Serialize the frame
        frame_data = pickle.dumps(frame)
        # Pack the frame size
        message_size = struct.pack("L", len(frame_data))
        # Send the frame size followed by the frame data
        conn.sendall(message_size + frame_data)

        # Receive data from the client
        while len(data) < payload_size:
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += conn.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Deserialize the frame
        frame = pickle.loads(frame_data)
        # Display the frame
        cv2.imshow('receiver_frame', frame)

        # Exit if 'Enter' key is pressed
        if cv2.waitKey(1) == 13:
            print("You closed the window.")
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            cv2.destroyAllWindows()
            break
    except Exception as e:
        cv2.destroyAllWindows()
        print(f"An error occurred: {e}")
        break

video.release()
