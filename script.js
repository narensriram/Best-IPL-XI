const bestXI = [
    "Travis Head", "Sunil Narine", "Virat Kohli", "Riyan Parag", "Venkatesh Iyer",
    "Andre Russell", "Heinrich Klaasen", "Mitchell Starc", "Thangarasu Natarajan",
    "Varun Chakravarthy", "Jasprit Bumrah"
];

let userTeam = [];

function addPlayer() {
    let input = document.getElementById("playerInput").value.trim();
    let feedback = document.getElementById("feedback");
    let teamList = document.getElementById("teamList");
    let countDisplay = document.getElementById("count");
    let ratingDisplay = document.getElementById("rating");

    if (!input) {
        feedback.textContent = "Please enter a player's name.";
        return;
    }

    if (userTeam.includes(input)) {
        feedback.textContent = `${input} is already in your team!`;
        return;
    }

    if (bestXI.includes(input)) {
        userTeam.push(input);
        let listItem = document.createElement("li");
        listItem.textContent = input;
        teamList.appendChild(listItem);
        feedback.textContent = `${input} added to your team!`;

        let matchingPlayers = userTeam.length;
        countDisplay.textContent = matchingPlayers;
        ratingDisplay.textContent = rateTeam(matchingPlayers);
    } else {
        feedback.textContent = `${input} is not in the Best XI. Try again!`;
    }

    if (userTeam.length === 10) {
        feedback.textContent = "🎉 Congratulations! You built the Best XI!";
    }

    document.getElementById("playerInput").value = "";
}


function resetGame() {
    userTeam = [];
    document.getElementById("teamList").innerHTML = "";
    document.getElementById("feedback").textContent = "Start adding players!";
    document.getElementById("count").textContent = "0";
    document.getElementById("rating").textContent = "-";
}
