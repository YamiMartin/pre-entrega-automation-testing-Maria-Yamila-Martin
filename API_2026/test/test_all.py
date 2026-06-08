from api_users import get_users, create_users, login_users

def test_get_users():
    response = get_users()

    assert response.status_code == 200

    data = response.json() #me da una lista de info
    print(data)

    assert "data" in data #constata si esta esta palabra en la respuesta
    assert len(data["data"]) # variable data < 0

def test_create_users(user_data):
    response = create_users(
        user_data["name"],
        user_data["job"],
    )

    #response = create_users( #info a crear usando funcion de api_users
    #   "Yami",
    #   "QA"
    #) Pase info a conftest

    assert response.status_code == 200 or 201

    body = response.json()
    print(body)

    assert body["name"] == "Yami"
    assert body["job"] == "QA"