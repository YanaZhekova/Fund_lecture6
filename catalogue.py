class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, letter):
        letter_product_list = list(x for x in self.products if x[0] == letter)
        return letter_product_list

    def __repr__(self):
        result = ""

        result += f"Items in the {self.name} catalogue:"
        self.products.sort()
        for x in self.products:
            result += f"\n{x}"

        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)