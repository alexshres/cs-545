import mlp
import numpy as np


def main():
    # XOR example
    X = np.array([[0, 0], [0, 1], [1, 0], [1,1]])
    y = np.array([[0], [1], [1], [0]])

    nodes = [2, 2, 1]


    model = mlp.MLP(X, y, nodes=nodes)

    for mat in range(len(model.weights_array)):
        print(model.weights_array[mat].shape)


    return

if __name__ == "__main__":
    main()
   
