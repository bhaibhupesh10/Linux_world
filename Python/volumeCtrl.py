from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(percent):
    # Ensure the input is within the valid range (0 to 100)
    if percent < 0 or percent > 100:
        print("Volume percentage must be between 0 and 100.")
        return

    # Convert the percentage to a scalar value (0.0 to 1.0)
    target_volume = percent / 100.0

    # Get the default audio endpoint (speaker)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

    # Create an instance of the audio endpoint volume interface
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Set the volume
    volume.SetMasterVolumeLevelScalar(target_volume, None)
    print(f"Volume set to {percent}%")

# Take user input for the desired volume percentage
try:
    user_input = float(input("Enter the desired volume percentage (0-100): "))
    set_volume(user_input)
except ValueError:
    print("Invalid input. Please enter a number between 0 and 100.")
