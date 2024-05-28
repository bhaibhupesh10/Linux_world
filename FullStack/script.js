document.getElementById('fetchDataBtn').addEventListener('click', fetchData);

function fetchData() {
    // Create a new XMLHttpRequest object
    const xhr = new XMLHttpRequest();

    // Configure it: GET-request for the URL
    xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts/1', true);

    // Set up the callback function for when the request is completed
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Parse the JSON response
            const data = JSON.parse(xhr.responseText);

            // Output the data to the HTML element
            document.getElementById('output').innerHTML = `
                <h2>${data.title}</h2>
                <p>${data.body}</p>
            `;
        } else {
            document.getElementById('output').innerHTML = 'Error fetching data';
        }
    };

    // Send the request
    xhr.send();
}
