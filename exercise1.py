def count_occurrences(text, target_word):
    text_length = get_length(text)
    word_length = get_length(target_word)
    count_match_word = 0
    i = 0

    while i <= text_length - word_length:
        match = True
        j = 0

        while j < word_length:
            if not are_equal(text[i + j], target_word[j]):
                match = False
                break
            j += 1

        # Block to check that it is a single word
        # and not part of another word (e.g., 'stick' vs 'sticker')
        if match:
            before_ok = i == 0 or not is_letter(text[i - 1])

            after_index = i + word_length
            if after_index >= text_length:
                after_ok = True
            else:
                after_ok = not is_letter(text[after_index])

            if before_ok and after_ok:
                count_match_word += 1

        i += 1

    return count_match_word


def get_length(string):
    count = 0
    try:
        while True:
            _ = string[count]
            count += 1
    except IndexError:
        pass
    return count


def is_letter(char):
    return (
        ("a" <= char <= "z")
        or ("A" <= char <= "Z")
        or is_accented_letter(char)
    )


def is_accented_letter(char):
    accented_letters = [
        "á",
        "é",
        "í",
        "ó",
        "ú",
        "Á",
        "É",
        "Í",
        "Ó",
        "Ú",
        "ü",
        "Ü",
        "ñ",
        "Ñ",
    ]

    i = 0
    while True:
        try:
            if char == accented_letters[i]:
                return True
            i += 1
        except IndexError:
            break
    return False


def are_equal(c1, c2):
    return uppercase_to_lowercase(c1) == uppercase_to_lowercase(c2)


def uppercase_to_lowercase(char):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

    i = 0
    while True:
        try:
            if char == uppercase_letters[i]:
                return lowercase_letters[i]
            i += 1
        except IndexError:
            break

        accented_map = {
            "Á": "á",
            "É": "é",
            "Í": "í",
            "Ó": "ó",
            "Ú": "ú",
            "Ü": "ü",
            "Ñ": "ñ"
        }

    if char in accented_map:
        return accented_map[char]

    return char  # If it's not an uppercase letter, return it unchanged
