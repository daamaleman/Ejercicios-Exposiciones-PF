"""
Ejercicio
Escribe una función en Python que implemente el algoritmo Merge Sort. La función debe tomar una lista de números como entrada y devolver la lista ordenada de menor a mayor.

Instrucciones:
Divide la lista en dos sublistas aproximadamente iguales.


Ordena recursivamente ambas sublistas utilizando el algoritmo Merge Sort.


Combina las dos sublistas ordenadas en una sola lista ordenada.
"""


def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def get_number_list():
    while True:
        user_input = input("Introduce una lista de números separados por comas: ")
        try:
            list = [float(num.strip()) for num in user_input.split(',')]
            return list
        except ValueError:
            print("Por favor, introduce solo números válidos separados por comas.")


def main():
    print("Algoritmo Merge Sort")
    numbers = get_number_list()
    sorted_numbers = merge_sort(numbers)
    print(f"Lista ordenada: {sorted_numbers}")


if __name__ == "__main__":
    main()


