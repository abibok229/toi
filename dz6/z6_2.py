def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch for ch in s if ch.isalnum()).lower()
    return cleaned == cleaned[::-1]

assert is_palindrome("казак") == True
assert is_palindrome("А роза упала на лапу Азора") == True
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("12321") == True
assert is_palindrome("hello") == False
assert is_palindrome("") == True
assert is_palindrome("a") == True

print("Все тесты пройдены")
