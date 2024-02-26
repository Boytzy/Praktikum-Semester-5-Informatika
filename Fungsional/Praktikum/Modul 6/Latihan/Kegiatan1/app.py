import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Buka gambar
gambar_path = "Kegiatan1/image/LogoUMM.jpg"
img = Image.open(gambar_path)

# Ubah gambar menjadi hitam-putih
img = img.convert("L")

# Tambahkan teks
draw = ImageDraw.Draw(img)
font_path = "Kegiatan1/Roboto-Medium.ttf"
font = ImageFont.truetype(font_path, 24)

nama_nim = "BAYU PUSPITO AJI - 202110370311291"
text_width, text_height = draw.textsize(nama_nim, font)
text_position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
draw.text(text_position, nama_nim, font=font, fill="black")

# Simpan gambar hasil edit
hasil_path = "hasil_kegiatan1.jpg"
img.save(hasil_path)

# Tampilkan hasil pengolahan gambar
plt.imshow(Image.open("hasil_kegiatan1.jpg"))
plt.set_cmap('gray')
plt.show()
