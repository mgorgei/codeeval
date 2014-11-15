def f(s):
    odd = False
    result = ""
    for char in s:
        if char.isalpha():
            odd = not odd
        result += char.upper() if odd else char.lower()
    return result
