### Установка MongoDB

Сначала установим MongoDB в докер, для этого используем docker-compose файл и запустим его: `docker compose up`.

Далее необходимо установить `MongoDB Shell` и `MongoDB Compass`.

### Создание БД и заполнение ее данными
Добавим в БД данные из [источника](http://socr.ucla.edu/docs/resources/SOCR_Data/SOCR_Data_Dinov_020108_HeightsWeights.html),
я выбрал датасет по статистике веса/роста людей. Для установки скопируем `.csv` файл при
помощи `docker cp` и загрузим в БД при помощи `mongoimport`:
``` bash
mongoimport --type csv -d test -c weights_heights --headerline --drop SOCR_Data_Dinov_020108_HeightsWeights.csv 
```

Проверим, что все данные загружены:

![Find all](images/img1.png)

### CRUD операции
Начнем с операции выборки:
![Find](images/find.png)

Теперь исследуем время запросов, начнем с выборки:
![Find_t](images/find_t2.png)

Операция вставки:
![Insert](images/insert.png)

И время ее работы:
![Insert_t](images/insert_t.png)

Операция удаления:
![Delete](images/delete.png)

Время ее работы:
![Delete_t](images/delete_t.png)

Операция обновления:
![Update](images/update.png)

Время ее работы:
![Update_t](images/update_t.png)

### Индексирование

Создадим индекс и измерим время работы:
![index](images/index.png)

Время работы выборки:
![Find_t2](images/find_t3.png)

Время работы удаления:
![Delete_t2](images/delete_t2.png)

Время работы вставки:
![Insert_t2](images/insert_t2.png)

Время работы обновления:
![Update_t2](images/update_t2.png)

В итоге, операции поиска, обновления и удаления стали быстрее,
а вот операция вставки - медленнее. 