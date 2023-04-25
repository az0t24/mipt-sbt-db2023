import redis
import time
import json


with open('large-file.json') as f:
    data = json.load(f)

db = redis.StrictRedis(
    host='localhost',
    port=6380
)

# ADD
print("ADD")
# string
result = 0
for i in range(10):
    start = time.time()
    db.set('json_string' + str(i), json.dumps(data))
    end = time.time()
    result += end - start
print("add string to redis:", result / 10)

# hset
result = 0
for i in range(10):
    start = time.time()
    db.hset('json_hset' + str(i), 'hw' + str(i), json.dumps(data))
    end = time.time()
    result += end - start
print("add hset to redis:  ", result / 10)

# zset
result = 0
zset_count = []
for i in range(10):
    zset_data = {}
    for j, elem in enumerate(data):
        zset_data[json.dumps(elem)] = j
    start = time.time()
    zset_count_elem = db.zadd('json_zset' + str(i), zset_data)
    end = time.time()
    zset_count.append(zset_count_elem)
    result += end - start
print("add zset to redis:  ", result / 10)

# list
result = 0
list_count = []
for i in range(10):
    list_data = []
    for elem in data:
        list_data.append(json.dumps(elem))
    start = time.time()
    list_count_elem = (db.lpush('json_list' + str(i), *list_data))
    end = time.time()
    list_count.append(list_count_elem)
    result += end - start
print("add list to redis:  ", result / 10)


# READ
print("READ")
# string
result = 0
for i in range(10):
    start = time.time()
    read_json_string = db.get('json_string' + str(i))
    end = time.time()
    result += end - start
print("get string from redis:", result / 10)

# hset
result = 0
for i in range(10):
    start = time.time()
    read_json_hset = db.hget('json_hset' + str(i), 'hw' + str(i))
    end = time.time()
    result += end - start
print("get hset from redis:  ", result / 10)

# zset
result = 0
for i in range(10):
    start = time.time()
    read_json_zset = db.zrange('json_zset' + str(i), 0, zset_count[i])
    end = time.time()
    result += end - start
print("get zset from redis:  ", result / 10)

# list
result = 0
for i in range(10):
    start = time.time()
    read_json_list = db.lrange('json_list' + str(i), 0, list_count[i])
    end = time.time()
    result += end - start
print("get list from redis:  ", result / 10)

db.flushall()
