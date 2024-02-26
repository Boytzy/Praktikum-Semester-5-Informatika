def dekorasi_output(fungsi):
    def wrapper(s):
        result = fungsi(s)
        if result:
            return f"'{s}' adalah sebuah palindrom."
        else:
            return f"'{s}' bukan palindrom."

    return wrapper

# Fungsi is_palindrome yang akan di-dekorasi
def is_palindrome(s):
    cleaned_str = ''.join(filter(str.isalnum, s.lower()))

    def is_palindrome_recursive(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

    return is_palindrome_recursive(cleaned_str)

# Mendekorasi fungsi is_palindrome dengan dekorator
is_palindrome = dekorasi_output(is_palindrome)

# Contoh penggunaan
input_str = "A man, a plan, a canal, Panama"
result = is_palindrome(input_str)

print(result)
