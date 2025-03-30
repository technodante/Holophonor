const submitButton = document.querySelector(".sendButton")

submitButton.addEventListener("click" , () => {
    sendMessage()
})

document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.querySelector(".sendButton");
    const imgElement = document.getElementById("generated-image");

    sendButton.addEventListener("click", function () {
        fetch("/get_image")
            .then(response => response.json())
            .then(data => {
                console.log("Image URL received:", data.image_url);
                imgElement.style.display = "none"; // Hide image initially
                imgElement.src = data.image_url;

                imgElement.onload = function () {
                    console.log("Image loaded successfully");
                    imgElement.style.display = "block"; // Show when loaded
                };

                imgElement.onerror = function () {
                    console.error("Error loading image:", imgElement.src);
                    imgElement.style.display = "none";
                };
            })
            .catch(error => console.error("Error fetching image:", error));
    });
});

async function sendMessage() {
    const input = document.getElementById("audio-upload");
    const chatBox = document.getElementById("chat-box");
    const audio_file = input.files[0];
    const formData = new FormData()
    formData.append(audio_file)

    const image_json = await fetch("http://127.0.0.1:5500/", {
        method: "POST",
        body: JSON.stringify({ File: input.file[0] }),
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
