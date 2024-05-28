// DOM calling
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureButton = document.getElementById('capture');
const context = canvas.getContext('2d');
//  rendering context and its drawing functions

// Access the user's webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        video.play();
    })
    .catch(err => { 
        console.error("Error accessing the camera: ", err);
    });

// Capture the photo when the button is clicked
captureButton.addEventListener('click', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
});
