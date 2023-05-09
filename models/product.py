from .mongo import conn_mongodb

class Product():
    @staticmethod
    def insert_one(product):
        db = conn_mongodb()
        db.products.insert_one({
            'name': Product['name'],
            'price': Product['price'],
            'description': Product['description']
        })
