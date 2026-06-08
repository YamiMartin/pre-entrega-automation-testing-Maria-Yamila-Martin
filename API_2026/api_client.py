import requests

URL_BASE = "https://reqres.in/api/users"

HEADERS = {
    "x-api-key" : "free_user_3EouvbgL6ZFXMATaBLukuXfTGNL"
}

def get_users():
    response = requests.get(URL_BASE, headers=HEADERS)
    print(response.json())

get_users()