const bestXI = [
    "Travis Head", "Sunil Narine", "Virat Kohli", "Riyan Parag", "Venkatesh Iyer",
    "Andre Russell", "Heinrich Klaasen", "Mitchell Starc", "Thangarasu Natarajan",
    "Varun Chakravarthy", "Jasprit Bumrah"
];

let userTeam = [];
let score = 0;

function addPlayer() {
    let input = document.getElementById("playerInput").value.trim();
    let feedback = document.getElementById("feedback");
    let teamList = document.getElementById("teamList");
    let countDisplay = document.getElementById("count");
    let ratingDisplay = document.getElementById("rating");

    // Clear previous feedback classes
    feedback.className = "";

    if (!input) {
        feedback.textContent = "Please enter a player's name.";
        feedback.classList.add("warning");
        return;
    }

    if (userTeam.includes(input)) {
        feedback.textContent = `${input} is already in your team!`;
        feedback.classList.add("warning");
        return;
    }

    if (bestXI.includes(input)) {
        userTeam.push(input);
        score++; // Increase score for correct entries
        let listItem = document.createElement("li");
        listItem.textContent = input;
        teamList.appendChild(listItem);
        feedback.textContent = `${input} is correct! They are now added to your team!`;
        feedback.classList.add("success");

        let matchingPlayers = userTeam.length;
        countDisplay.textContent = matchingPlayers;
        ratingDisplay.textContent = rateTeam(matchingPlayers);
    } else {
        feedback.textContent = `${input} is not in the Best XI. Try again!`;
        feedback.classList.add("error");
    }

    if (userTeam.length === 11) {
        feedback.textContent = "🎉 Congratulations! You built the Best XI!";
        feedback.classList.add("success");
    }

    document.getElementById("playerInput").value = "";
}

// Function to rate the team based on number of correct players
function rateTeam(matchingPlayers) {
    if (matchingPlayers === 11) return "🏆 Best";
    if (matchingPlayers >= 9) return "🔥 Great";
    if (matchingPlayers >= 6) return "✅ Good";
    if (matchingPlayers >= 3) return "⚠️ Average";
    return "❌ Worst";
}

// Reset the game
function resetGame() {
    userTeam = [];
    score = 0;
    document.getElementById("teamList").innerHTML = "";
    document.getElementById("feedback").textContent = "Start adding players!";
    document.getElementById("feedback").className = "";
    document.getElementById("count").textContent = "0";
    document.getElementById("rating").textContent = "-";
}
