## запуск приложения

```
python main.py
```

### добавление продукта

```
curl http://localhost:5000/api/v1/product -X POST -H 'Content-Type: application/json' -d '{"name": "Видеомагнитофон", "price": 20}'
```

### получение списка продуктов

```
curl "localhost:5000/api/v1/product?page=0&limit=10"
```

### получение продукта по его ID

```
curl "http://127.0.0.1:5000/api/v1/product/1"
```
