def verify_login(username: str, password: str):
    for user in user_data:
        if user['username'] == username and user['password'] == password:
            return True
    return False