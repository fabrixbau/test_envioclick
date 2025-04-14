import unittest
from exercise1 import count_occurrences


class TestCountOccurrences(unittest.TestCase):
    def test_paragraph_occurrences(self):
        paragraph = (
            "La logística Digital es un concepto que surge de la integración"
            "entre la logística tradicional y la era digital. Con el auge"
            "del correo electrónico y las descargas digitales reemplazando"
            "productos físicos, podríamos estar hablando de un golpe"
            "devastador para la industria de la logística, pero,"
            "de hecho, ha ocurrido algo muy diferente. El sector "
            "de la logística ha introducido las innovaciones digitales."
        )
        word = "logística"
        result = count_occurrences(paragraph, word)
        self.assertEqual(result, 4)

    def test_no_occurrences(self):
        text = "This sentence does not contain the target word."
        word = "logística"
        result = count_occurrences(text, word)
        self.assertEqual(result, 0)

    def test_case_insensitive(self):
        text = "LOGÍSTICA logística Logística LoGíStIcA"
        word = "logística"
        result = count_occurrences(text, word)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
