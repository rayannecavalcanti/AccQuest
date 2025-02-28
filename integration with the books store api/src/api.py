import requests

BASE_URL = "https://demoqa.com"

def create_user(username, password):
    url = f"{BASE_URL}/Account/v1/User"
    payload = {
        "userName": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def generate_token(username, password):
    url = f"{BASE_URL}/Account/v1/GenerateToken"
    payload = {
        "userName": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def is_user_authorized(username, password):
    url = f"{BASE_URL}/Account/v1/Authorized"
    payload = {
        "userName": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.status_code == 200

def get_all_books():
    url = f"{BASE_URL}/BookStore/v1/Books"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def rent_books(user_id, token, isbns):
    url = f"{BASE_URL}/BookStore/v1/Books"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": isbn} for isbn in isbns]
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def get_user_details(user_id, token):
    url = f"{BASE_URL}/Account/v1/User/{user_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
