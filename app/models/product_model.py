class Product:
    def __init__(self, product_id, name, brands, categories):
        self.product_id = product_id
        self.name = name
        self.brands = brands
        self.categories = categories

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "brands": self.brands,
            "categories": self.categories
        }