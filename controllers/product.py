from flask import request
from .blueprint import product
# from models.mongo import conn_mongodb
from models.product import Product

#상품 API
@product.route('/regist', methods=['POST'])
def regist():
    # 전달받은 상품 정보
    form_data = request.form

    #이미지 정보를 저장


    # 저장하는 일
    Product.insert_one(form_data)

    return "상품 등록 API입니다."

@product.route('/test', methods=['GET'])
def test():
    return "테스트 API입니다."