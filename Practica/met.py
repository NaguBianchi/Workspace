from Practica.Principal import User
import json


def test_usuario():
    usr = User.user_generator()
    print(usr.toJSON())
    print(usr)
    usr.save_user(usr)

def file_creator(file_name, data):
    file = open(file_name, "w")
    file.write(str(data))
    file.close()

def test_mod():
    with open('26.json', 'r') as f:
        json_data = json.load(f)
        json_data['nombre'] = "juan"

    with open('26.json', 'w') as f:
        f.write(json.dumps(json_data))

test_mod()

#test_usuario()

#file_creator()
