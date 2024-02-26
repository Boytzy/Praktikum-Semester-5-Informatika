import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 2, 9, 1]
y = [3, 7, 2, 8, 5, 1, 9, 2]

plt.scatter(x, y, label='Titik 2', color='red')


plt.title('Scatter Plot')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')


plt.legend()
plt.show()