import requests

URL_BASE = "https://reqres.in/api/login"

HEADERS = {
    "x-api-key" : "free_user_3EouvbgL6ZFXMATaBLukuXfTGNL"
}

creds = {
    'email': 'eve.holt@reqres.in',
    'password': 'cityslicka'
    }

def post_login(): #cre info o inicia sesion
    response = requests.post(URL_BASE, headers= HEADERS, json = creds)
    print(response.status_code)# sale numero de error, si es 200 o mas esta OK

    success = response.json()
    
    print(success["id"])

post_login()