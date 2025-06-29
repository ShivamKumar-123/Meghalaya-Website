// script.js
let text = "";

function sendData() {
    const listItem = document.getElementById("button").innerText;
    text = listItem;
}

function getText() {
    return text;
}

export { getText };
