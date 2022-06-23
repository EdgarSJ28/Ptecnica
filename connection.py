from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv

#coneccion con la base de datos en https://upstash.com/

try:
    rdb = Redis(
    host= 'us1-upward-piglet-37457.upstash.io',
    port= '37457',
    password= 'da5feb2be0884e07a207007006605af0', ssl=True)
    ssl = bool(getenv("REDIS_SSL"))

    print("connection to redi")


except ConnectionError as e:
    print(e)
    
