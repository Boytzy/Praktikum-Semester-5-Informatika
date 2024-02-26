import math
import os

def translasi(x, y, tx, ty):
    x_baru = x + tx
    y_baru = y + ty
    return x_baru, y_baru

def dilatasi(x, y, sx, sy):
    x_baru = x * sx
    y_baru = y * sy
    return x_baru, y_baru

def rotasi(x, y, sudut):
    sudut_rad = math.radians(sudut)
    x_baru = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
    y_baru = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
    return x_baru, y_baru

def perbesaran_skala(x, y, skala_x, skala_y):
    x_baru = x * skala_x
    y_baru = y * skala_y
    return x_baru, y_baru

def gabungan_decorator(function):
    def function(x, y, tx, ty, sudut, skala_x, skala_y):
        translasi_xy = translasi(x, y, tx, ty)
        rotasi_xy = rotasi(translasi_xy[0], translasi_xy[1], sudut)
        dilatasi_xy = dilatasi(rotasi_xy[0], rotasi_xy[1], skala_x, skala_y)
        return dilatasi_xy
    return function

@gabungan_decorator
def gabungan(x, y, tx, ty, sudut, skala_x, skala_y):
    return x, y, tx, ty, sudut, skala_x, skala_y
    

def inputan():
     tx = float(input("tx : "))
     ty = float(input("ty : "))
     sudut = float(input("sudut : "))
     skala_x = float(input("skala x : "))
     skala_y = float(input("skala y : "))
     return tx, ty, sudut, skala_x, skala_y

# Contoh penggunaan
data_user = inputan()
titik_awal = (9, 1)
gradien = 2

titik_baru= gabungan(titik_awal[0], titik_awal[1], *data_user)
#9, 1, 60, 1, 2
#2, -3, 60, 1.5, 2 

def point(x, y):
    return x, y

def line_equation_of(x, y, m):
    c = y - m * x  # Menghitung nilai C
    return f"y = {m:.2f}x + {c:.2f}"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

print(titik_baru)
print(f"Persamaan garis yang melalui titik A ({titik_awal[0]}, {titik_awal[1]}) dengan gradien {gradien}:")
print(line_equation_of(titik_awal[0], titik_awal[1], gradien))

print("Persamaan garis baru setelah trnsformasi")
print(line_equation_of(titik_baru[0], titik_baru[1], gradien))





