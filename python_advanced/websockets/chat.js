const statusEl = document.getElementById('status');
const messagesEl = document.getElementById('messages');
const formEl = document.getElementById('chat-form');
const inputEl = document.getElementById('message-input');

const socket = new WebSocket('ws://localhost:8000/ws');

function addMessage(text, selfMessage = false) {
    const messageEl = document.createElement('div');
    messageEl.className = `message${selfMessage ? ' self' : ''}`;
    messageEl.textContent = text;
    messagesEl.appendChild(messageEl);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

socket.addEventListener('open', () => {
    statusEl.textContent = 'Connected';
    addMessage('Connected to the server');
});

socket.addEventListener('message', (event) => {
    addMessage(event.data);
});

socket.addEventListener('close', () => {
    statusEl.textContent = 'Disconnected';
    addMessage('Connection closed');
});

socket.addEventListener('error', () => {
    statusEl.textContent = 'Connection error';
});

formEl.addEventListener('submit', (event) => {
    event.preventDefault();
    const message = inputEl.value.trim();
    if (!message) {
        return;
    }
    socket.send(message);
    addMessage(message, true);
    inputEl.value = '';
});
