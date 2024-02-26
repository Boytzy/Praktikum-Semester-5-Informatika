import os
from functools import reduce


# Data film
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Fungsi untuk menghitung jumlah film berdasarkan genre
def count_movies_by_genre(movies):
    # Menggunakan reduce untuk menggabungkan data berdasarkan genre
    genre_counts = reduce(
        lambda acc, movie: {**acc, movie['genre']: acc.get(movie['genre'], 0) + 1},
        movies,
        {}
    )
    return genre_counts

# Fungsi untuk menghitung rata-rata rating film berdasarkan tahun rilis menggunakan map
def average_rating_by_year(movies):
    def extract_ratings(movie):
        return (movie['year'], movie['rating'])

    year_ratings = list(map(extract_ratings, movies))

    def calculate_average_ratings(ratings):
        year, ratings_list = ratings
        total_rating = sum(ratings_list)
        count = len(ratings_list)
        return (year, total_rating / count)

    grouped_ratings = {}
    for year, rating in year_ratings:
        if year in grouped_ratings:
            grouped_ratings[year].append(rating)
        else:
            grouped_ratings[year] = [rating]

    average_ratings = list(map(calculate_average_ratings, grouped_ratings.items()))
    return dict(average_ratings)

# Fungsi untuk mencari film dengan rating tertinggi
def find_highest_rated_movie(movies):
    highest_rated_movie = max(movies, key=lambda x: x['rating'])
    return highest_rated_movie


# Fungsi untuk mencari film berdasarkan judul menggunakan filter
def find_movie_by_title(movies, title):
    matching_movies = list(filter(lambda x: x['title'] == title, movies))
    if not matching_movies:
        return None
    return matching_movies[0]


os.system('cls' if os.name == 'nt' else 'clear')
# Program utama
while True:
    print("Pilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if choice == '1':
        print("Jumlah Film Berdasarkan Genre:")
        genre_counts = count_movies_by_genre(movies)
        print(genre_counts)
    if choice == '2':
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
        average_ratings = average_rating_by_year(movies)
        for year, rating in average_ratings.items():
            print(f"Tahun {year}: Rata-rata Rating {rating:.2f}")
    elif choice == '3':
        print("Film dengan Rating Tertinggi:")
        highest_rated_movie = find_highest_rated_movie(movies)
        print(f"Informasi Film: {highest_rated_movie['title']}")
        print(f"Rating: {highest_rated_movie['rating']}")
        print(f"Tahun Rilis: {highest_rated_movie['year']}")
        print(f"Genre: {highest_rated_movie['genre']}")
    elif choice == '4':
        title = input("Masukkan judul film yang ingin dicari: ")
        movie = find_movie_by_title(movies, title)
        if movie is None:
            print("Film dengan judul tersebut tidak ditemukan.")
        else:
            print(f"Informasi Film: {movie['title']}")
            print(f"Rating: {movie['rating']}")
            print(f"Tahun Rilis: {movie['year']}")
            print(f"Genre: {movie['genre']}")
    elif choice == '5':
        print("Program selesai.")
        break

    user_input = input("Apakah Anda ingin melanjutkan program? (Y/N): ")
    if user_input.lower() != 'y':
        break

os.system('cls' if os.name == 'nt' else 'clear')