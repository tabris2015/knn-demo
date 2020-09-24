import numpy as np


class Knn:
    def __init__(self, task='cl'):
        self.task = task
        if self.task not in ['rg', 'cl']:
            raise Exception('Tipo de tarea inválida, use "rg" para regresión o "cl" para clasificación')

    def distance(self, a, b):
        return np.linalg.norm(a - b, axis=1)

    def mode(self, array):
        return 1 if np.sum(array) > array.size // 2 else 0

    def predict(self, x, y, example, k):
        dists = self.distance(x, np.tile(example, (x.shape[0], 1)))
        ranking = np.argsort(dists)
        labels = y[ranking[:k]]
        neighbors = x[ranking[:k]]
        return self.mode(labels), neighbors, labels
