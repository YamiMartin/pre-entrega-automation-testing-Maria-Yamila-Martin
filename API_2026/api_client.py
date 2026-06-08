import requests

URL_BASE = "https://reqres.in/api/users"

HEADERS = {
    "x-api-key" : "free_user_3EouvbgL6ZFXMATaBLukuXfTGNL"
}

def get_users():
    response = requests.get(URL_BASE, headers=HEADERS)
    print(response.json())# si solo pongo response sale codigo de error( o .status_code), si pongo .json() sale info 

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error")

get_users()