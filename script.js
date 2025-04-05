const ws = new WebSocket("ws://127.0.0.1:12345");

ws.onopen = () => {
  document.getElementById("result").textContent = "Connected to the server!";
};

ws.onmessage = (event) => {
  document.getElementById("result").textContent = event.data;
};

ws.onerror = () => {
  document.getElementById("result").textContent = "Error connecting to the server!";
};

document.getElementById("submit").addEventListener("click", () => {
  const guess = document.getElementById("guess").value;
  if (!guess) {
    document.getElementById("result").textContent = "Please enter a number!";
    return;
  }
  ws.send(guess);
});
