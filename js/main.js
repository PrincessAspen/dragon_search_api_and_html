document.addEventListener("DOMContentLoaded", function() {

    // Function to fetch a dragon by name
    function fetchByName(dragonName) {
        const url = `http://localhost:8000/dragons?name=${encodeURIComponent(dragonName)}`;  // Fetch by name
        const theInfoSpot = document.getElementById("infoSpot");
        theInfoSpot.innerHTML = '';  // Clear previous content

        fetch(url, { method: "GET" })
            .then(response => response.json())
            .then(giveResult => {
                console.log(giveResult);
                if (giveResult) {
                    displayDragon(giveResult);  // Display the found dragon
                } else {
                    displayMessage("Dragon not found.");
                }
            })
            .catch(error => {
                console.error("Fetch Error: ", error);
                displayMessage("An error occurred while fetching the data.");
            });
    }

    // Function to fetch a random dragon
    function fetchRandomDragon() {
        const url = 'http://localhost:8000/dragons';  // Fetch all dragons and pick a random one
        const theInfoSpot = document.getElementById("infoSpot");
        theInfoSpot.innerHTML = '';  // Clear previous content

        fetch(url, { method: "GET" })
            .then(response => response.json())
            .then(giveResult => {
                if (giveResult.length > 0) {
                    const randomIndex = Math.floor(Math.random() * giveResult.length);
                    const randomDragon = giveResult[randomIndex];
                    displayDragon(randomDragon);  // Display the random dragon
                } else {
                    displayMessage("No dragons available.");
                }
            })
            .catch(error => {
                console.error("Fetch Error: ", error);
                displayMessage("An error occurred while fetching the data.");
            });
    }

    // Function to display a dragon's information
    function displayDragon(dragon) {
        const theInfoSpot = document.getElementById("infoSpot");
        const newParagraph = document.createElement("p");
        const newH1 = document.createElement("h1");
        const newH2 = document.createElement("h2");
        const newFigure = document.createElement("figure");
        const dragonImage = document.createElement("img");

        dragonImage.src = dragon.image || "css/Media/placeholder.jpg";
        newH1.innerHTML = `${dragon.name}`;
        newH2.innerHTML = `Color: ${dragon.color} <br> Size: ${dragon.size} <br> Breath Weapon: ${dragon.breath_weapon}`;
        newParagraph.innerHTML = `${dragon.summary}`;

        // Append the dragon details to the page
        newFigure.appendChild(dragonImage);
        newFigure.appendChild(newH1);
        theInfoSpot.appendChild(newFigure);
        theInfoSpot.appendChild(newH2);
        theInfoSpot.appendChild(newParagraph);

        if (newParagraph.textContent) {
            theInfoSpot.classList.add("theInfo");
            console.log("added")
        } else {
            theInfoSpot.classList.remove("theInfo");
            console.log("removed")
        }
    }

    // Function to display a message
    function displayMessage(message) {
        const theInfoSpot = document.getElementById("infoSpot");
        const newParagraph = document.createElement("p");
        newParagraph.textContent = message;
        theInfoSpot.appendChild(newParagraph);
    }

    // Event listener for form submission
    const form = document.getElementById("dragonfinder");
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const inputField = document.getElementById("lookup").value.trim();  // Get the input field value

        // Check if the input is blank or contains a name
        if (inputField) {
            fetchByName(inputField);  // Call the fetchByName function if the input is not blank
        } else {
            fetchRandomDragon();  // Call the fetchRandomDragon function if the input is blank
        }
        
        form.reset();  // Reset the form after submission
    });
});
