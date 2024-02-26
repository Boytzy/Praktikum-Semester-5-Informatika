def is_palindrome(s):
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil
    cleaned_str = ''.join(filter(str.isalnum, s.lower()))

    # Fungsi rekursif untuk memeriksa palindrom
    def is_palindrome_recursive(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

    return is_palindrome_recursive(cleaned_str)

# Contoh penggunaan
input_str = "A man, a plan, a canal, Panama"
result = is_palindrome(input_str)

print(f"Apakah '{input_str}' merupakan palindrom? {result}")
