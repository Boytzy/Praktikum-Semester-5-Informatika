import matplotlib.pyplot as plt
from PIL import Image

# Langkah 1: Buka gambar latar belakang (background) dan gambar overlay
background_path = "Kegiatan2/MapUMM.jpeg"
overlay_path = "Kegiatan2/Logo umm.png"  # Pastikan gambar overlay memiliki alpha channel

background_img = Image.open(background_path)
overlay_img = Image.open(overlay_path)

# Langkah 2: Konversi overlay image ke mode RGB
overlay_img = overlay_img.convert("RGBA")

# Langkah 3: (Optional) Perkecil ukuran gambar overlay
# Misalnya, kita perkecil menjadi setengah dari ukuran aslinya
width, height = overlay_img.size
new_size = (width // 2, height // 2)
overlay_img = overlay_img.resize(new_size, Image.ANTIALIAS)

# Langkah 4: Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_img.paste(overlay_img, (50, 50), overlay_img)

# Langkah 5: Simpan gambar hasil edit
hasil_path = "hasil_kegiatan2.jpg"
background_img.save(hasil_path)

# Langkah 6: Tampilkan hasil edit gambar
plt.imshow(Image.open("hasil_kegiatan2.jpg"))
plt.show()
