import matplotlib.pyplot as plt

x = ['Apple', 'Banana', 'Orange', 'Grapes']
y = [10, 15, 7, 12]

plt.bar(x, y, color='skyblue')
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.show()
