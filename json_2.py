import json

products = {1001: {"name": "avocado", "price": 230,
                   "category": "grocery",
                   "quantity": 10, "date": "10/03/2021"},
            1002: {"name": "lotion", "price": 250,
                   "category": "beauty & personal",
                   "quantity": 100,
                   "date": "15/07/2021"},
            1003: {"name": "pain reliever", "price": 500,
                   "category": "health",
                   "quantity": 200, "date": "12/04/2021"},
            1004: {"name": "dry pasta", "price": 20,
                   "category": "grocery",
                   "quantity": 50, "date": "27/06/2021"},
            1005: {"name": "toothbrush", "price": 700,
                   "category": "beauty & personal",
                   "quantity": 100,
                   "date": "30/01/2021"},
            1006: {"name": "halloween candy", "price": 33,
                   "category": "grocery",
                   "quantity": 56, "date": "22/02/2021"},
            1007: {"name": "mascara", "price": 765,
                   "category": "beauty & personal",
                   "quantity": 70,
                   "date": "11/03/2021"},
            1008: {"name": "capsicum", "price": 764,
                   "category": "grocery",
                   "quantity": 90, "date": "16/02/2021"},
            1009: {"name": "blush", "price": 87,
                   "category": "beauty & personal",
                   "quantity": 50, "date": "17/07/2021"},
            1010: {"name": "granola bars", "price": 24,
                   "category": "grocery", "quantity": 60,
                   "date": "20/05/2021"},
            }


# def find_products(product):
#     gt_90 = []
#     for i in product:
#         if product[i]['quantity'] > 90:
#             gt_30.append(product[i])
#
#     return gt_90
#
#
# print(find_products(products))


def view_all():
    import json
    import pandas as pd

    js = json.dumps(products)
    fd = open("data.json", "w")
    fd.write(js)
    fd.close()

    fd = open("data.json", "r")
    txt = fd.read()
    data = json.loads(txt)
    table = pd.DataFrame(columns=['ID','name','price','category','quantity' ,'date'])

    for i in data.keys():
        t = pd.DataFrame(columns=['ID'])
        t['ID'] = [i]
        for j in data[i].keys():
            t[j] = [data[i][j]]
        table = table.append(t)
    table = table.reset_index(drop=True)

    return table

    # import json
    # import pandas as pd
    #
    # df = pd.read_table("/Users/e9/Downloads/products.txt", sep=' ', header=0)
    # print(df)

    grocery_data = table[table.category == 'grocery']
    print(grocery_data)


def add_item():
    import json
    import pandas as pd
    cur_table = view_all()
    latest_id = int(cur_table.tail(1)['ID'])+1
    name = input("Name of item: ")
    price = input("Price of item (in cents): ")
    category = input("Category: ")
    quantity = input("Quantity: ")
    date = input("Date (mm/dd/yyyy): ")
    # new_item_info = [int(id), name, price, category, quantity, date]

    new_item = pd.DataFrame(columns=["ID", "name", "price", "category", "quantity", "date"])

    new_item.loc[len(new_item)] = [latest_id, name, price, category, quantity, date]
    # print(new_item)
    cur_table = cur_table.append(new_item, ignore_index=True)
    print(cur_table)


users = {0000: {"username": "Ethan", "Password": "Choi",
                "Is_Admin": True}, 0o0001: {"username": "John", "Password": "Doe",
                "Is_Admin": False}}


def log_in():
    is_logged_in = False

    while is_logged_in == False:
        user_id = int(input("Enter id: "))
        username = input("Enter username: ")
        password = input("Enter password: ")

        user_name = users[user_id]['username']
        pass_word = users[user_id]['Password']
        if username == user_name and password == pass_word and users[user_id]['Is_Admin'] == True:
            is_logged_in = True
            print("logged in as admin")
            user_name = Admin()
            user_name.sel_and_run()

        elif username == user_name and password == pass_word and users[user_id]['Is_Admin'] != True:
            is_logged_in = True
            print("logged in as user")
            user_name = Others()
            user_name.sel_and_run()
        else:
            print('Login Failed')


class Admin:
    def __init__(self, user='null', password='null'):
        self.password = 'null pass'
        self.user = 'null user'

    def sel_and_run(self):
        logged_in = True
        while logged_in == True:
            selection = input("View all(1), edit(2), add user(3), quit(4), change user(5): ")
            if selection == "1":
                print(view_all())

            if selection == "2":
                add_item()
                export_products()

            if selection == "3":
                # users = {0000: {"username": "Ethan", "Password": "Choi",
                #                 "Is_Admin": True}, 0o0001: {"username": "John", "Password": "Doe",
                #                                             "Is_Admin": False}}
                id = int(input("Enter id:"))
                username = input("Enter Username:")
                password = input("Enter Password:")
                admin = bool(input("Is Admin(y):"))
                users[id] = {"username": username, "Password": password, "Is_Admin": admin}
                print(users)
                export_users()


            if selection == "4":
                export_users()
                export_products()
                logged_in = False
                quit()

            if selection == "5":
                export_users()
                export_products()
                log_in()



class Others:
    def __init__(self, user='null', password='null'):
        self.password = 'null pass'
        self.user = 'null user'

    def sel_and_run(self):
        logged_in = True
        while logged_in == True:
            selection = input("View all(1), quit(2), change user(3): ")
            if selection == "1":
                print(view_all())

            if selection == "2":
                logged_in = False
                quit()

            if selection == "3":
                log_in()


def view_all_users():
    import json
    import pandas as pd

    js = json.dumps(users)
    fd = open("data.json", "w")
    fd.write(js)
    fd.close()

    fd = open("data.json", "r")
    txt = fd.read()
    data = json.loads(txt)
    table = pd.DataFrame(columns=['ID','username','Password','Is_Admin'])

    for i in data.keys():
        t = pd.DataFrame(columns=['ID'])
        t['ID'] = [i]
        for j in data[i].keys():
            t[j] = [data[i][j]]
        table = table.append(t)
    table = table.reset_index(drop=True)

    return table


def view_all_users_json():
    import json
    import pandas as pd

    js = json.dumps(users)
    fd = open("data.json", "w")
    fd.write(js)
    fd.close()

    fd = open("data.json", "r")
    txt = fd.read()
    data = json.loads(txt)
    return data


def export_users():
    with open("/Users/e9/Downloads/users.txt", "w") as f:
        f.write(str(view_all_users_json()))


def export_products():
    with open("/Users/e9/Downloads/products.txt", "w") as f:
        f.write(str(view_all()))


log_in()
