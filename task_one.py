import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv('x_y_coordinates.csv')
def plot_data(data):
    infor = data
    x = infor["x"]
    y = infor[" y"]
    plot = plt.scatter(x,y)
    plot_data = plt.show()
    return plot_data
plot_data(file)
