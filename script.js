const submitButton = document.querySelector(".sendButton")

submitButton.addEventListener("click" , () => {
    sendMessage()
})
function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();
    if (message === "") return;

    let chatBox = document.getElementById("chat-box");
    let userMessage = `<p><strong>You:</strong> ${message}</p>`;
    chatBox.innerHTML += userMessage;
    input.value = "";
    
    setTimeout(() => {
        let botMessage = `<p><strong>Bot:</strong> Hello! How can I help?</p>`;
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000);
}