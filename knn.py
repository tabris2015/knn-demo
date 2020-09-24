import numpy as np


class Knn():
    def __init__(self, task='cl'):
        self.task = task
        if self.task not in ['rg', 'cl']:
            raise Exception('Tipo de tarea inválida, use "rg" para regresión o "cl" para clasificación')

    def distance(self, a, b):
        pass

    def mode(self, array):
        pass

    def mean(self, array):
        pass

    def predict(self, x, y, example, k):
        pass
