import requests

URL_BASE = "https://reqres.in/api"

HEADERS = {
    "x-api-key" : "free_user_3EouvbgL6ZFXMATaBLukuXfTGNL"
}

creds = {
    'email': 'eve.holt@reqres.in',
    'password': 'cityslicka'
    }

def get_users():
   return requests.get(
      f"{URL_BASE}/users", headers= HEADERS
   )

def create_users(name, job):
   data = {
      "name" : name,
      "job" : job
   }

   return requests.post(
      f"{URL_BASE}/users", headers= HEADERS, json = data
   )

def login_users(email, password):
   data = {
      "email" : email,
      "password" : password
   }

   return requests.post(
        f"{URL_BASE}/login", headers= HEADERS, json = data
   )

def update_users(name, job):
    data = {
      "name" : name,
      "job" : job
   }