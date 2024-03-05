let navLinks = document.getElementById("navLinks");
let openUploadSection = document.getElementById("upload-section")

function openDashboardNav(){
    navLinks.style.left = "0";
}
function closeDashboardNav(){
    navLinks.style.left = "-200px";
}
function openUpload() {
    openUploadSection.style.display = "flex";
}
function closeUpload() {
    openUploadSection.style.display = "none";
}

const navListLinks = document.querySelectorAll('ul li');

console.log(role)
if  (role == "client") {
    alert("Apologies " + username + "! As a " + role + ", you are not authorized to access any of the features. Please ")
    openDashboardNav()
}
if (role == "Manager") {
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance') {
            item.style.opacity = 0.5;
        }
    });
}
if (role == "Employee") {
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance' || text == 'Marketing') {
            item.style.opacity = 0.5;
        }
    });
}
if (role == "Client") {
    document.getElementById('chat-section').style.display= 'none';
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance' || text == 'Chat' || text == 'Operational') {
            item.style.opacity = 0.5;
        }
    });
}

// Data for chat groups
let chatGroups = [
    { avatar: "https://i.pravatar.cc/40?img=47", name: "Manager" },
    { avatar: "https://i.pravatar.cc/40?img=5", name: "Employee" },
    { avatar: "https://i.pravatar.cc/40?img=9", name: "Client" },
    { avatar: "https://i.pravatar.cc/40?img=32", name: "Guest" },
    { avatar: "https://cdn.pixabay.com/photo/2020/05/29/13/26/icons-5235125_1280.png", name: "Group"}
];


// Function to create chat groups dynamically
function createChatGroups() {
    let chat_container = document.getElementById("chat_room");

    chatGroups.forEach((group, index) => {
        let chat_group = document.createElement('div');
        chat_group.classList.add(`group-${index + 1}`, 'chat-mod');
        chat_group.id = (`group_${index+1}`);
        chat_group.setAttribute("onclick","getId(this)")

        let group_DP = document.createElement('div');
        group_DP.classList.add('grp-dp');

        let avatarImg = document.createElement('img');
        avatarImg.src = group.avatar;
        avatarImg.alt = 'Avatar';

        group_DP.appendChild(avatarImg);

        let groupName = document.createElement('div');
        groupName.classList.add('grp-name');

        let nameHeader = document.createElement('h4');
        nameHeader.textContent = group.name;

        groupName.appendChild(nameHeader);

        chat_group.appendChild(group_DP);
        chat_group.appendChild(groupName);

        chat_container.appendChild(chat_group);
    });
}

let group_id = [ 'group_1', 'group_2', 'group_3', 'group_4', 'group_5' ];

// Changing the HEADER ICON AND NAME in Message Container
function change_message_container_header(current_ID, i) {
    console.log(current_ID, chatGroups[i]);
    let current_person_ID = document.getElementById("current_person_DP");
    let current_person_name = document.getElementById("current_person_name");
    current_person_ID.src = chatGroups[i].avatar;
    current_person_name.innerText = chatGroups[i].name;
}

// Call the function to create chat groups
createChatGroups();

let selectedChatUser = null;

function getId(username) {
    // Changing Colors for the Container
    for (let i = 0; i < group_id.length; i++){
        let current_element = document.getElementById(group_id[i]);
        if (group_id[i] === username.id) {
            current_element.style.backgroundColor = "#45ADFF";
            current_element.style.color = "#ffffff";
            change_message_container_header(username.id, i);
        }
        else {
            current_element.style.backgroundColor = "#ffffff";
            current_element.style.color = "#000000";
        }
    }
    // CHAT FUNCTIONALITY
    selectedChatUser = username.id;
    console.log(selectedChatUser)
    if (selectedChatUser === 'group_5') {
        document.getElementById("sub-chat-input").style.display = 'none';
        document.getElementById("upload-grp-section").style.display = 'flex';
        loadUploadedDocuments();
        // alert("You are not allowed to send messages here.");
    }
    else {
        document.getElementById("sub-chat-input").style.display = 'grid';
        document.getElementById("upload-grp-section").style.display = 'none';
    }
    // Load chat history for the selected user
    loadChatHistory();
}

function loadChatHistory() {
    // Assume there is an element with the id 'chatting-section'
    let chatMessages = document.getElementById('chatting-section');
    chatMessages.innerHTML = ''; // Clear previous messages

    // Load chat history from JSON
    fetch(`/get_chat_history/${selectedChatUser}`)
        .then(response => response.json())
        .then(data => {
            data.forEach(message => {
                console.log(message)
                let messageDiv = document.createElement('div');
                messageDiv.classList.add('msg-container');
                // messageDiv.textContent = `${message.sender}: ${message.text}`;
                messageDiv.textContent = `${message.text}`;
                chatMessages.appendChild(messageDiv);
            });
        });
}

function sendMSG() {
    let messageText = document.getElementById('msg_input').value;
    if (messageText.trim() === '' || !selectedChatUser) return;

    // Save message to JSON
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            sender: 'You',
            receiver: selectedChatUser,
            text: messageText,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadChatHistory();
            document.getElementById('msg_input').value = '';
        } else {
            alert('Failed to send message');
        }
    });
}

// Update the previewFile function in your existing JavaScript code
function previewFile() {
    let fileInput = document.getElementById('file-input');
    let filePreview = document.getElementById('file-preview');
    
    let selectedFile = fileInput.files[0];

    if (selectedFile) {
        let reader = new FileReader();

        reader.onload = function (e) {
            let fileType = selectedFile.type.split('/')[0]; // Get the file type (e.g., 'image', 'video', 'audio')

            if (fileType === 'image') {
            // if (0 === 0) {
                console.log("Success")
                document.getElementById("before-upload").style.display = "none";
                filePreview.src = e.target.result;
            } else {
                filePreview.src = ''; // Clear the preview for non-image files
            }
        };

        reader.readAsDataURL(selectedFile);
    } else {
        filePreview.src = ''; // Clear the preview if no file selected
    }
}

// Modify the existing uploadFile function
function uploadFile() {
    let fileInput = document.getElementById('file-input');
    let selectedFile = fileInput.files[0];
    console.log(selectedFile)
    if (selectedFile) {
        let formData = new FormData();
        formData.append('file', selectedFile);

        fetch('/upload_file', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Handle success, e.g., display a message or update the UI
                console.log('File uploaded successfully');

                // Log the file path to the console
                console.log('File Path:', data.filePath);
                fileName = extractNameofFile(data.filePath);
                buildDocumentinChat(data.filePath, fileName);

                sendUploadedDocuments(data.filePath,fileName);

                document.getElementById("before-upload").style.display = "flex";
                // Optionally clear the preview after successful upload
                document.getElementById('file-preview').src = '';
            } else {
                // Handle failure, e.g., display an error message
                console.error('File upload failed');
            }
        });
    }
}

function extractNameofFile(path) {
    let temp = path.split('/');
    let file_name = temp[temp.length - 1];
    return file_name
}

function buildDocumentinChat(path, file_name) {
    let parentContainer = document.getElementById('chatting-section');
    // Create the document container
    var documentContainer = document.createElement('div');
    documentContainer.className = 'document-container';

    // Create the image container
    var imageContainer = document.createElement('div');
    imageContainer.className = 'image-container';

    // Create the image element
    var imgElement = document.createElement('img');
    imgElement.src = `${path}`; // Set the path dynamically
    imgElement.alt = 'Test';

    // Append the image element to the image container
    imageContainer.appendChild(imgElement);

    // Create the image name container
    var imageNameContainer = document.createElement('div');
    imageNameContainer.className = 'image-name-container';

    // Create the span element for the image name
    var spanElement = document.createElement('span');
    spanElement.textContent = file_name;

    // Append the span element to the image name container
    imageNameContainer.appendChild(spanElement);

    // Append the image container and image name container to the document container
    documentContainer.appendChild(imageContainer);
    documentContainer.appendChild(imageNameContainer);

    // Append the document container to the body
    parentContainer.appendChild(documentContainer);

}

function sendUploadedDocuments(path, file_name) {
    fetch(`/send_document`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            sender: 'YOU',
            fileName: path,
            filePath: file_name,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadUploadedDocuments();
        }
    })
}

function loadUploadedDocuments() {
    // Assume there is an element with the id 'chatting-section'
    let chatMessages = document.getElementById('chatting-section');
    chatMessages.innerHTML = ''; // Clear previous messages

    fetch(`/get_document_history`)
        .then(response => response.json())
        .then(data => {
            data.forEach(message => {
                console.log(message);
                buildDocumentinChat(message.fileName, message.filePath);
            })
        })
}


let chat_room = document.getElementById("chat_room");
let chat_room_toggle = document.getElementById("chat-room-toggle");
let chat_room_close = document.getElementById("chat-room-close");
let blur_div = document.getElementById("blur-div");

function openChatRoom() {
    blur_div.style.display = "block";
    chat_room_toggle.style.display = "none";
    chat_room_close.style.display = "block";
    chat_room_close.style.top = "0px";
    chat_room.style.display = "block";
}
function closeChatRoom() {
    blur_div.style.display = "none";
    chat_room_toggle.style.display = "block";
    chat_room_close.style.display = "none";
    chat_room_close.style.top = "-50px";
    chat_room.style.display = "none";
}


// buildDocumentinChat()
