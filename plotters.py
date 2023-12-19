import matplotlib.pyplot as plt
import numpy as np

def plot_dict_as_graph(dictionary, x_axis_name, y_axis_name, graph_name):
    x = list(dictionary.keys())
    y = list(dictionary.values())
    
    plt.plot(x, y, "bo")
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)
    plt.title(graph_name)
    plt.savefig(f"./assets/graphs/{graph_name}")
    plt.show()

