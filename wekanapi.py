from flask import Flask, request, jsonify # type: ignore
import requests

app = Flask(__name__)

WEKAN_API_URL = "http://host:5000"
USERNAME = "ADMIN"
PASSWORD = "PASS"

def get_wekan_token():
    response = requests.post(f"{WEKAN_API_URL}/users/login", json={"username": USERNAME, "password": PASSWORD})
    return response.json().get('token') if response.status_code == 200 else None

@app.route('/addcard', methods=['POST'])
def add_card_to_wekan():
    data = request.json
    token = get_wekan_token()
    if token:
        url = f"{WEKAN_API_URL}/api/boards/{data['boardId']}/lists/{data['listId']}/cards"
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, json={
            'authorId': data['authorId'],
            'title': data['title'],
            'description': data['description'],
            'swimlaneId': data['swimlaneId']
        })
        return jsonify(response.json()), response.status_code
    return jsonify({"error": "Authentication failed"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
