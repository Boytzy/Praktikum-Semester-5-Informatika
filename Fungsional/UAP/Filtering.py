def is_palindrome(s):
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil
    cleaned_str = ''.join(filter(str.isalnum, s.lower()))

    # Fungsi rekursif untuk memeriksa palindrom
    def is_palindrome_recursive(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

    return is_palindrome_recursive(cleaned_str)

def filter_palindrome_words(sentence):
    # Memisahkan kata-kata dalam kalimat
    kata_kata = sentence.split()

    # Menggunakan fungsi filter untuk memisahkan kata-kata yang merupakan palindrom
    palindromes = list(filter(lambda kata: is_palindrome(kata), kata_kata))

    # Menggunakan fungsi filter untuk memisahkan kata-kata yang bukan palindrom
    non_palindromes = list(filter(lambda kata: not is_palindrome(kata), kata_kata))

    return palindromes, non_palindromes

# Contoh penggunaan
kalimat = "Ada apa dengan si Bayu Puspito Aji"
palindromes, non_palindromes = filter_palindrome_words(kalimat)

print("Kata-kata palindrom:", palindromes)
print("Kata-kata bukan palindrom:", non_palindromes)
