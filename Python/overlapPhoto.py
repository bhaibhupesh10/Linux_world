#cut photo from image and show on the top of the image
import cv2
from PIL import Image, ImageOps
import numpy as np

# Step 1: Capture a Photo Using OpenCV
def capture_image():
    cap = cv2.VideoCapture(0)  # Open the webcam
    ret, frame = cap.read()    # Capture a single frame
    cap.release()              # Release the webcam
    if ret:
        cv2.imwrite('captured_image.jpg', frame)  # Save the captured image
    return ret, frame

# Step 2: Crop a Part of the Image Using Pillow
def crop_image(image_path, left, top, right, bottom):
    image = Image.open(image_path)  # Open the image file
    cropped_image = image.crop((left, top, right, bottom))  # Crop the image
    cropped_image.save('cropped_image.png')  # Save the cropped image
    return cropped_image

# Step 3: Overlay the Cropped Image on the Original Using OpenCV
def overlay_images(original_img_path, cropped_img_path, x_offset, y_offset):
    original_img = cv2.imread(original_img_path)  # Load the original image
    cropped_img = Image.open(cropped_img_path).convert("RGBA")  # Load the cropped image with alpha channel
    original_img_pil = Image.fromarray(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)).convert("RGBA")

    # Overlay the cropped image on the original image
    original_img_pil.paste(cropped_img, (x_offset, y_offset), cropped_img)
    combined = cv2.cvtColor(np.array(original_img_pil), cv2.COLOR_RGBA2BGRA)

    # Save and return the combined image
    cv2.imwrite('overlayed_image.png', combined)
    return combined

# Main Function
def main():
    # Capture image
    ret, frame = capture_image()
    if not ret:
        print("Failed to capture image")
        return

    # Define crop coordinates (example: central 200x200 area)
    height, width, _ = frame.shape
    left = width // 4
    top = height // 4
    right = left + 200
    bottom = top + 200

    # Crop the image
    cropped_image = crop_image('captured_image.jpg', left, top, right, bottom)

    # Define the position to overlay the cropped image
    x_offset = 50
    y_offset = 50

    # Overlay the cropped image on the original image
    result_image = overlay_images('captured_image.jpg', 'cropped_image.png', x_offset, y_offset)

    # Display the result
    cv2.imshow('Overlayed Image', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()