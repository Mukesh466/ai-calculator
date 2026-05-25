let display = document.getElementById("display");

function append(value) {
    if (display.innerText === "0") {
        display.innerText = value;
    } else {
        display.innerText += value;
    }
}

function clearDisplay() {
    display.innerText = "0";
}

function calculate() {
    fetch("http://127.0.0.1:5000/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            expression: display.innerText
        })
    })
    .then(res => res.json())
    .then(data => {
        display.innerText = data.result;
    });
}