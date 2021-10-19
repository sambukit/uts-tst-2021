import json
from fastapi import FastAPI,HTTPException
from auth.auth_handler import signJWT, get_password_hash, verify_password
from auth.helper import verify_login

with open("menu.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()
@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/menu/{item_id}')
async def read_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )

@app.post('/menu/{item_id}/{item_name}')
async def write_menu(name: str):
    item_id = len(data['menu'])+1
    newdata = {'id': item_id, 'name' : name}
    if(item_id > 1):
        data['menu'].append(newdata)
        with open("menu.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
        return data
        
@app.put('/menu/{item_id}')
async def update_menu(item_id: int, new_name: str):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            menu_item['name'] = new_name
        read_file.close()    
        with open("menu.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
    return {'message':'Data changed successfully'}

@app.delete('/menu/{item_id}')
async def delete_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            data['menu'].remove(menu_item)
        read_file.close()    
        with open("menu.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
    return {'message':'Data deleted successfully'}

@app.post('/user')
async def new_user(username: str, password: str):
    hashed_password = get_password_hash(password)
    newdata = {'username': username, 'password' : hashed_password}
    print(newdata)
    with open("user.json", "r") as read_user_file:
        user_data = json.load(read_user_file)
    print(user_data)
    user_data.append(newdata)
    with open("user.json", "w") as write_user_file:
        json.dump(user_data, write_user_file)
    write_user_file.close()
    return signJWT(username)

@app.post('/login')
async def user_login(username: str, password: str):
    db_password = "abc"
    with open("user.json", "r") as read_user_file:
        user_data = json.load(read_user_file)
    for user in user_data:
        if user['username'] == username:
            db_password = user['password']
    if db_password != "abc":
        if verify_password(password, db_password):
            return signJWT(username)
        else:
            return("Login gagal karena kesalahan username atau password")
    else:
        return("Login gagal karena kesalahan username atau password")
    
