from flask import Blueprint, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/product/<string:product_id>', methods=['GET'])
def get_product(product_id):
    """Obtiene un producto por su ID"""
    product = ProductService.get_product(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({"error": "Product not found"}), 404

@product_bp.route('/products', methods=['GET'])
def get_all_products():
    """Obtiene una lista de productos"""
    products = ProductService.get_all_products()
    if products:
        return jsonify(products), 200
    return jsonify({"error": "No products found"}), 404