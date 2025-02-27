from app.models.product_model import Product
from app.repositories.product_repository import ProductRepository


class ProductService:
    @staticmethod
    def get_product(product_id):
        product_data = ProductRepository.get_product_by_id(product_id)
        if product_data and "product" in product_data:
            product_info = product_data["product"]
            return Product(
                product_id=product_info.get("id", "N/A"),
                name=product_info.get("product_name", "Unknown"),
                brands=product_info.get("brands", "Unknown"),
                categories=product_info.get("categories", "Unknown")
            )
        return None
    
    @staticmethod
    def get_all_products():
        data = ProductRepository.get_all_products()

        if data and "products" in data:
            products = [
                Product(
                    product_id=item.get("id", "N/A"),
                    name=item.get("product_name", "Unknown"),
                    brands=item.get("brands", "Unknown"),
                    categories=item.get("categories", "Unknown")
                ).to_dict()
                for item in data["products"]
            ]
            return products

        return []
