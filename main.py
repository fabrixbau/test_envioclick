# from exercise1 import count_occurrences
from exercise2 import sort_by_priority
from input import data


# def main():
#     paragraph = (
#         "La logística Digital es un concepto que surge de
#          la integración entre"
#         "la logística tradicional y la era digital. Con el auge del correo "
#         "electrónico y las descargas digitales reemplazando productos
#          físicos,"
#         "podríamos estar hablando de un golpe devastador
#          para la industria de"
#         "la logística, pero, de hecho, ha ocurrido algo muy diferente. El"
#         "sector de la logística ha introducido las innovaciones digitales."
#     )

#     word = "logística"
#     result = count_occurrences(paragraph, word)
#     print(f"{result} ocurrencias encontradas.")


def main():
    # Criterio para ordenar
    criteria = [('weight', '=', 3)]
    # Aplica ordenamiento
    result = sort_by_priority(data, criteria)
    # Imprime lista modificada una sola vez
    print("LISTA ORDENADA:")
    print(result)
    print("************************* fin de la primera lista")
    # Imprime la lista original
    print("LISTA ORIGINAL:")
    print(data)


if __name__ == "__main__":
    main()
