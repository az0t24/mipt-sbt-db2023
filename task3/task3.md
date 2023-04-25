В качестве большого Json-файла я использую файл [из первой ссылки в гугле](https://github.com/json-iterator/test-data/blob/master/large-file.json).

### Тест на 1 ноде
Поднимем контейнер при помощи [`docker-compose.yaml`](redis/docker-compose.yaml),
расположенном в папке [`redis`](redis). Проверим, что он поднялся и работает:

![PingRedis](images/ping_redis.png)

Теперь при помощи файла [test.py](test.py) измерим скорость операций:

![TestRedis](images/test_redis.png)

### Тест на 3 нодах
Теперь поднимем контейнер при помощи [`docker-compose.yaml`](redis_cluster/docker-compose.yaml),
находящимся в [`redis_cluster`](redis_cluster). Опять проверим, что все работает:

![PingRedisCluster](images/ping_cluster.png)

Теперь при помощи все того же файла [test.py](test.py) измерим скорость:

![TestRedisCluster](images/test_cluster.png)

Как видим, время увеличилось, зато повысилась надежность нашей системы.