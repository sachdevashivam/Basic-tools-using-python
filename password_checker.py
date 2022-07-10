import requests
import hashlib

def request_api_data(hashed_password):
    url = 'https://api.pwnedpasswords.com/range/' + hashed_password
    res = requests.get(url)
    # print(res)  
    if res.status_code != 200:
        raise RuntimeError(f'Api Error : {res.status_code}, check the api and try again')
    return res    


# print(request_api_data('123'))    

def password_hashing(password):
     sha1_hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
     print(sha1_hashed_password)
     first5_char, tail = sha1_hashed_password[:5], sha1_hashed_password[5:]
     print(first5_char, tail)
     response = request_api_data(first5_char)
     return response

print(password_hashing('123'))     