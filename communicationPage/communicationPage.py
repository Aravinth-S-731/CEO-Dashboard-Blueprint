from flask import Flask, Blueprint, session, redirect, render_template, url_for, request, jsonify
from werkzeug.utils import secure_filename
import os, json

communicationPage = Blueprint('communicationPage', __name__, template_folder='templates', static_folder='static', static_url_path='/communicationPage/static')

CHAT_HISTORY_FILE = 'communicationPage\chat_history.json'
DOCUMENT_HISTORY_FILE = 'communicationPage\document_history.json'
# CHAT_HISTORY_FILE = 'chat_history.json'
# DOCUMENT_HISTORY_FILE = 'document_history.json'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# staticPath = 'static'
staticPath = 'communicationPage\static'
staticFolderPath = os.path.join(staticPath,UPLOAD_FOLDER)
# print(staticFolderPath)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(staticFolderPath):
    os.makedirs(staticFolderPath)

@communicationPage.route('/communication-module', methods=['GET', 'POST'])
def communicationModule():
    if session['role'] == "Guest":
        return redirect(url_for('auth.login', msg = f"As a {session['role']}, you do not have access to login."))
    elif session['role'] == "Client":
        return render_template('operationalPage.html',
                            username = session['username'],
                            email = session['email'],
                            role = session['role'],
                            msg=f"You are not authorized to view this page.")
    if 'loggedin' in session:
        if request.method == 'POST':
            # JSON structure {'sender': ..., 'receiver': ..., 'text': ...}
            new_message = request.json
            store_message(new_message)
            return jsonify({'success': True})
        return render_template('communicationPage.html',
                            username = session['username'],
                            email = session['email'],
                            role = session['role'])
    return redirect(url_for('login'))

@communicationPage.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        # JSON structure {'sender': ..., 'receiver': ..., 'text': ...}
        new_message = request.json
        store_message(new_message)

        return jsonify({'success': True})

def store_message(message):
    # Load existing chat history
    chat_history = load_chat_history()

    # Appending new message
    chat_history.append(message)

    # Save the updated chat history back to the file
    with open(CHAT_HISTORY_FILE, 'w') as file:
        json.dump(chat_history, file)

def load_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

@communicationPage.route('/get_chat_history/<username>', methods=['GET'])
def get_chat_history(username):
    # Load chat history from JSON file
    chat_history = load_chat_history()

    # Filter messages for the selected user
    user_chat_history = [message for message in chat_history if message['sender'] == username or message['receiver'] == username]
    # print(user_chat_history)
    return jsonify(user_chat_history)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@communicationPage.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'success': False, 'message': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # file.save(os.path.join(communicationPage.config['staticFolderPath'], filename))
        upload_folder_path = os.path.join(communicationPage.static_folder, 'uploads')
        file.save(os.path.join(upload_folder_path, filename))
        return jsonify({'success': True, 'message': 'File uploaded successfully', 'filePath': f'/communicationPage/static/uploads/{filename}'})

    return jsonify({'success': False, 'message': 'Invalid file format'})

# DOCUMENT UPLOAD AND RECEIVING
@communicationPage.route('/send_document', methods=['POST'])
def send_document():
    if request.method == 'POST':
        new_document = request.json
        store_document(new_document)
        return jsonify({'success': True})

def store_document(document):
    document_history = load_document_history()
    document_history.append(document)
    with open(DOCUMENT_HISTORY_FILE, 'w') as file:
        json.dump(document_history, file)

def load_document_history():
    try:
        with open(DOCUMENT_HISTORY_FILE, 'r') as file:
            # print(json.load(file))
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

@communicationPage.route('/get_document_history', methods=['GET'])
def get_document_history():
    document_history = load_document_history()

    user_document_history = [message for message in document_history if message['sender'] == 'YOU']
    # print(user_document_history)
    return jsonify(user_document_history)
