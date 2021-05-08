"""
this .py file contains some miscellaneous methods.

"""
import os
import rsa
import json
import pandas as pd
from hashlib import sha256
from .des_ import encrypt, decrypt


def tuple_(g):
    g = g[1:-1]
    g = g.split(',')
    d = tuple([int(i) for i in g])
    return d


def add_user(i):
    pubk, privk = rsa.newkeys(1024)


    username = f'user{i}'
    password = f'{username}@123'

    pwd_encr= sha256(password.encode('utf-8')).hexdigest()


    privk = tuple_(str(privk)[10:])
    pubk = str(pubk)[9:]
    prk = encrypt(privk, key = password, plaintext_is_hex = False, key_is_hex = False)

    balance_encr = encrypt(2453690000,key = password, plaintext_is_hex = False, key_is_hex = False)

    user_dict = {
        "username" : username,
        "password_encrypted" : pwd_encr,
        "bankbalance_encrypted" : balance_encr,
        "assets_encrypted" : [],
        "private_key" : prk,
        "public_key" : pubk
    }

    empty = {}

    with open(f'user_data\\{username}.json', 'w') as f:
        json.dump(user_dict, f, indent = 4)


    with open(f'all_texts\\{username}_text.json', 'w') as f:
        json.dump(empty, f, indent = 4)

    files = [j for j in os.listdir('block_chains') if j[-5:] == '.json']
    arr = []
    for file in files:
        df = pd.read_json('block_chains\\'+file).T
        arr.append((df.shape[0], df))
    df = max(arr)[1]
    df.T.to_json(f'block_chains\\user{i}_blockchain.json')
    print(f'user{i} is created. you can login now.')



