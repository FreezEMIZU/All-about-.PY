# This is an infinity password change script. Register a name to infinitely change your password
# still working on ordered dict for password used for login


def leng_tion(a):
    while True:
        e = input(a)
        if len(e) < 3:
            print("too short")
        elif e == "logout":
            return e
        elif len(e) > 5:
            print("too long")
        else:
            return e


acc = {}


def logreg(name):
    if name in acc:
        login(name)
        return True
    else:
        print("registered")
        return False


def wordloop(name):
    while True:
        word = leng_tion("New Password: ")
        if word in acc[name]:
            print("Password used")
        elif word == "logout":
            break
        else:
            print("Latest password set")
            acc[name].add(word)
            print(acc[name])


def login(name):
    tri = 0
    limit = 3
    while tri < limit:
        word = leng_tion("Login: ")
        if word in acc[name]:
            print("logged in")
            break
        else:
            tri += 1
    else:
        print("Please reset")  # aka. force login


while True:
    name = leng_tion("Name:")
    if logreg(name) is False:
        word = leng_tion("First Password: ")
        acc[name] = {word}
    else:
        wordloop(name)
