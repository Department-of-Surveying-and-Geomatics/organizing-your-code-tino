
import matplotlib.pyplot as plt
points = [
    [-18.9686, 31.1668],
    [-17.8274, 31.0521],
    [-20.1505, 28.5845],
    [-19.8327, 32.7649],
    [-17.5222, 30.9737],
    [-18.3712, 26.4995],
    [-20.2901, 30.0582],
    [-16.5174, 28.7902],
    [-19.3458, 29.5485],
    [-17.9009, 25.8201],
    [-20.2739, 29.4214],
    [-18.9622, 31.0444],
    [-16.5261, 30.8099],
    [-19.3597, 30.8711],
    [-17.8136, 29.4608],
    [-19.7907, 31.0036],
    [-18.3141, 27.0326],
    [-19.4346, 29.8174],
    [-20.2277, 29.1534],
    [-17.3569, 30.1662],
]
x = [point[0] for point in points]
y = [point[1] for point in points]

plt.figure(figsize=(10, 12))
plt.scatter(x, y, c='RED',  label='points')
point_numbers = range(1, len(points) + 1)
for i, (xi, yi, point_number) in enumerate(zip(x, y, point_numbers)):
    plt.annotate(point_number, (xi, yi), textcoords="offset points", xytext=(0, 10),fontsize=8)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('plotted points')

plt.legend()
plt.show()
