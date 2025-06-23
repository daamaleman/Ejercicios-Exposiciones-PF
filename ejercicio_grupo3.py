"""
Ejercicio propuesto

Una tienda en línea necesita mostrar sus productos ordenados por precio, desde el más bajo hasta el más alto. Tiene listas de productos de diferentes tamaños (pequeñas, medianas y grandes), que pueden estar:

Totalmente desordenadas

Parcialmente ordenadas

Ya ordenadas (por ejemplo, cuando alguien vuelve a ver la misma categoría)
"""

def get_products():
    """
    Prompts the user to enter products with name and price.
    Returns a list of dictionaries with the products.
    """
    products = []
    while True:
        name = input("Ingrese el nombre del producto (o presione Enter para terminar): ").strip()
        if not name:
            break
        while True:
            try:
                price = float(input(f"Ingrese el precio de '{name}': "))
                if price < 0:
                    print("El precio no puede ser negativo. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el precio.")
        products.append({'name': name, 'price': price})
    return products

def sort_products_by_price(products):
    """
    Sorts a list of products (dictionaries) by the 'price' field from lowest to highest.
    """
    return sorted(products, key=lambda x: x['price'])

def display_products(products):
    """
    Displays the list of products in a readable way.
    """
    if not products:
        print("No hay productos para mostrar.")
        return
    print("\nProductos ordenados por precio:")
    for product in products:
        print(f"- {product['name']}: ${product['price']:.2f}")

def main():
    """
    Main function of the program.
    """
    print("Bienvenido al sistema de ordenamiento de productos por precio.")
    products = get_products()
    sorted_products = sort_products_by_price(products)
    display_products(sorted_products)

if __name__ == "__main__":
    main()
