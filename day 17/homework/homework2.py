def filter(word):
    vowels = "aeiou"
    result = ""

    for char in word:
        if char in vowels:
            result += char
    
    return result


filter("lasha")