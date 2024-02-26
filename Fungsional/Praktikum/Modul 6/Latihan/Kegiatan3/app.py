import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

# Langkah 1: Buka gambar menggunakan Pillow
gambar_path = "Kegiatan3/hasil_kegiatan2.jpg"
img = Image.open(gambar_path)

# Langkah 2: Ubah tingkat kecerahan dan kontras
brightness_factor = 1.5
contrast_factor = 1.2

enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(contrast_factor)

# Langkah 3: Simpan gambar hasil edit
hasil_path = "brightness_contrast_image.jpg"
img.save(hasil_path)

# Langkah 4: Tampilkan hasil edit gambar
plt.imshow(Image.open("brightness_contrast_image.jpg"))
plt.show()
