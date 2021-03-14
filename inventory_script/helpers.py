from nornir.core.inventory import ConnectionOptions

creds = {
    "SW-1": {"username": "admin", "password": "admin"},
    "SW-2": {"username": "admin", "password": "admin"},
    "SW-3": {"username": "admin", "password": "admin"},
    "SW-4": {"username": "admin", "password": "admin"},
    "SW-5": {"username": "admin", "password": "admin"}, 
    "SW-6": {"username": "admin", "password": "admin"},
    "SW-7": {"username": "admin", "password": "admin"},
    "SW-8": {"username": "admin", "password": "admin"},
    "SW-9": {"username": "admin", "password": "admin"},
    "SW-10": {"username": "admin", "password": "admin"},
    "SW-11": {"username": "admin", "password": "admin"},
    "SW-12": {"username": "admin", "password": "admin"}
    }

def adapt_user_password(host):
    host.username = creds[f"{host}"]["username"]
    host.password = creds[f"{host}"]["password"]