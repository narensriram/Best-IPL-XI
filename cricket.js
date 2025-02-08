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
    } else {
        feedback.textContent = `${input} is not in the Best XI. Try again!`;
    }

    if (userTeam.length === 11) {
        let rating = rateTeam(userTeam.length);
        feedback.textContent = `Congratulations! You completed your team. Rating: ${rating}`;
    }

    document.getElementById("playerInput").value = "";
}

function rateTeam(count) {
    if (count === 11) return "Best";
    if (count >= 9) return "Great";
    if (count >= 6) return "Good";
    if (count >= 3) return "Average";
    return "Worst";
}
