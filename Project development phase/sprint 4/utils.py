from connect import execDB, execReturn

# INSERT into user_data(username , email , pass ) values ('Manoj' , 'manoj.selvam312@gmail.com' , 'Abcd123$')


def addUser(username, email, password):
    sql_fd = f"SELECT * FROM user WHERE username='{username}'"
    r = execReturn(sql_fd)
    sql_fd = f"SELECT * FROM user"
    a = execReturn(sql_fd)
    print(a)
    if r != []:
        return "Username Exists"

    sql_st = f"INSERT INTO user(username , email , pass ) values ( '{username}' , '{email}' , '{password}' )"
    r = execDB(sql_st)
    return "User registered successfully"

def check():
    sql_fd = f"SELECT * FROM user"
    a = execReturn(sql_fd)
    return a



def getPassword(username):
    sql_fd = f"SELECT password FROM user WHERE email='{username}'"
    r = execReturn(sql_fd)
    print(r)
    return r[0]['PASSWORD']


def fetchFinanceRecord(username):
    sql_fd = f"SELECT * FROM financee WHERE username='{username}'"
    r = execReturn(sql_fd)
    return r


def createFinanceRecord(username, amount, category, description, date):
    sql_st = f"INSERT INTO financee(username , amount , category , description , date ) values ( '{username}' , '{amount}' , '{category}' , '{description}' , '{date}' )"
    r = execDB(sql_st)
    return "Record created successfully"
