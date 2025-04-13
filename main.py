from exercise1 import count_occurrences


def main():
    paragraph = (
        "La logística Digital es un concepto que surge de la integración entre"
        "la logística tradicional y la era digital. Con el auge del correo "
        "electrónico y las descargas digitales reemplazando productos físicos,"
        "podríamos estar hablando de un golpe devastador para la industria de"
        "la logística, pero, de hecho, ha ocurrido algo muy diferente. El"
        "sector de la logística ha introducido las innovaciones digitales."
    )

    word = "logística"
    result = count_occurrences(paragraph, word)
    print(f"{result} ocurrencias encontradas.")


if __name__ == "__main__":
    main()
