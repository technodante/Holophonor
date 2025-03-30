const reader = new FileReader()
reader.addEventListener('load', () => {

});
reader.readAsDataURL();
const submitButton = document.querySelector(".sendButton")

submitButton.addEventListener("click" , () => {
    sendMessage()
})

document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".sendButton").addEventListener("click", function () {
        window.location.href = "/get_image"; // Redirects to the Flask route that serves the image
    });
});

async function sendMessage() {
    const input = document.getElementById("audio-upload");
    const chatBox = document.getElementById("chat-box");
    const audio_file = input.files[0];
    const formData = new FormData();
    formData.append("audio", audio_file);

    const image_json = await fetch("http://127.0.0.1:5500/upload", {
        method: "POST",
        body: formData,
    });
    
    
    let userMessage = `<p><strong>You:</strong> ${audio_file}</p>`;
    chatBox.innerHTML += userMessage;
    input.value = "";
    
    setTimeout(() => {
        let botMessage = `<p><strong>Bot:</strong> Hello! How can I help?</p>`;
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000);
}
