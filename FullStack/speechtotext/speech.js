document.addEventListener('DOMContentLoaded', (event) => {
    const startButton = document.getElementById('start-button');
    const resultDisplay = document.getElementById('result');

    // Check for browser support
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert('Your browser does not support the Web Speech API');
        return;
    }

    // Initialize speech recognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = false; // Set to true for continuous recognition
    recognition.interimResults = false; // Set to true for interim results

    recognition.onstart = function() {
        resultDisplay.innerHTML = 'Listening...';
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        resultDisplay.innerHTML = 'Result: ' + transcript;
    };

    recognition.onerror = function(event) {
        resultDisplay.innerHTML = 'Error: ' + event.error;
    };

    recognition.onend = function() {
        resultDisplay.innerHTML += ' (Recognition ended)';
    };

    // Start recognition on button click
    startButton.addEventListener('click', () => {
        recognition.start();
    });
});
