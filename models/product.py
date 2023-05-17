from .mongo import conn_mongodb
from datetime import datetime
from bson import ObjectId


# Product 컬렉션의 일들을 작성할 때 에는 models에 자바의 도메인 같은 느낌
class Product():
    @staticmethod
    def insert_one(product, thumbnail_img_url, detail_img_url):
        db = conn_mongodb()
        db.products.insert_one({
            'name': product['name'],
            'price': product['price'],
            'description': product['description'],
            'thumbnail_img': thumbnail_img_url,
            'detail_img': detail_img_url,
            'user': 'admin',
            'create_at': int(datetime.now().timestamp()),
            'update_at': int(datetime.now().timestamp())
        })

    @staticmethod
    def find():
        db = conn_mongodb()
        products = db.products.find({})

        return products;

    @staticmethod
    def delete_one(id):
        db = conn_mongodb()
        db.products.delete_one({'_id': ObjectId(id)})

    @staticmethod
    def update_one(id, product, thumbnail_img_url, detail_img_url):
        db = conn_mongodb()

        new_product = {
            'name': product['name'],
            'price': product['price'],
            'description': product['description'],
            'user': 'admin',
            'update_at': int(datetime.now().timestamp())
        }

        if thumbnail_img_url:
            new_product['thumbnail_img'] = thumbnail_img_url
        if detail_img_url:
            new_product['detail_img'] = detail_img_url

        db.products.update_one(
            {'_id': ObjectId(id)},
            {'$set': new_product}
        )

    @staticmethod
    def find_one(id):
        db = conn_mongodb()
        product = db.products.find_one({'_id': ObjectId(id)})

        return product
