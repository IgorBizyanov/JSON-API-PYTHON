# JSON-API-PYTHON

### Запуск веб-приложения
    python3 pyjsonapi/main.py
Доступно 3 метода: создание нового объявления, получение списка объявлений и получение конкретного объявления
Для выполнения воспользуемся HTTPie:
    pip install httpie
    
Создание нового объявления выполним с помощью команды
    http POST http://localhost:5000/api/create_advert/ head='ad_head' content='description' price=99.99 photo1='stock_photos.com/photo93569356'
