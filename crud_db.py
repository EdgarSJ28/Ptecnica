from ast import Try
from connection import rdb
from redis.exceptions import ResponseError

#CRUD de la db

def save_hash(key: str, data: dict):
    try:
        rdb.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)

def get_hash(key: str):
    try:
        return rdb.hgetall(name=key)
    except ResponseError as e:
        print(e)

def delete_hash(key: str, keys: list):
    try:
        rdb.hdel(key, *keys)
    except ResponseError as e:
        print(e)