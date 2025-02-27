import requests
from config.settings import Config

class ProductRepository:
    @staticmethod
    def get_product_by_id(product_id):
        url = f"{Config.API_BASE_URL}{product_id}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    
    @staticmethod
    def get_all_products():
        """Obtiene una lista de productos desde la API pública"""
        url = Config.API_ALL_PRODUCTS_URL
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
