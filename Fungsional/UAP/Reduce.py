from functools import reduce

def is_palindrome(s):
    cleaned_str = ''.join(filter(str.isalnum, s.lower()))

    def is_palindrome_recursive(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

    return is_palindrome_recursive(cleaned_str)
''
def filter_palindrome_words(sentence):
    kata_kata = sentence.split()
    palindromes = list(filter(lambda kata: is_palindrome(kata), kata_kata))
    non_palindromes = list(filter(lambda kata: not is_palindrome(kata), kata_kata))
    return palindromes, non_palindromes

kalimat = "Ada apa dengan si Bayu Puspito Aji"
palindromes, _ = filter_palindrome_words(kalimat)

total_panjang_palindromes = reduce(lambda x, kata: x + len(kata), palindromes, 0)

print("Kata-kata palindrom:", palindromes)
print("Total panjang kata palindrom:", total_panjang_palindromes)