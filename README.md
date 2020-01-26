# JSON-API-PYTHON

### Установка зависимостей
    pip install -r requirements.txt
### Запуск веб-приложения
    python3 pyjsonapi/main.py
##### Доступно 3 метода: создание нового объявления, получение списка объявлений и получение конкретного объявления
##### Общий формат запросов
	http://domain:port/api/method_name/?params
##### Для выполнения запросов воспользуемся HTTPie
	pip install httpie
    
##### Создание нового объявления выполним с помощью команды
	http POST http://localhost:5000/api/create_advert/ head='ad_head' content='description' price=99.99 photo1='stock_photos.com/photo93569356'

##### Получение конкретного объявления по заданному id
	http GET http://localhost:5000/api/get_advert/1

##### Получение списка всех объялений в базе, отсортированных по возрастанию цены, по убыванию даты публикации
	http GET http://localhost:5000/api/get_all_adverts/ sort_price=asc sort_date=desc
