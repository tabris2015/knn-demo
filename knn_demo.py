import numpy as np
from tkinter import *
from tkinter.ttk import *
from knn import Knn
from time import sleep
import random
from random import randint

import time


class KnnDemoApp():
    SIZE = 3
    MARKS = ['X', 'O']
    MODES = ['DATASET', 'PREDICCION']

    def __init__(self):
        self.points = []
        self.labels = []
        self.lines = []
        self.knn = Knn()

        self.root = Tk()
        self.root.title("KNN Demo")
        self.root.geometry('800x520')
        self.root.resizable(False, False)

        self.axis = Canvas(self.root, width=720, height=370)
        self.axis.grid(column=0, row=0, columnspan=5)
        self.axis.configure(bg='white')
        self.axis.bind('<Button 1>', self.clickCallback)
        self.axis_points = []
        self.axis_predictions = []

        self.debug_lbl = Label(self.root, text='Mensaje ==>')
        self.debug_lbl.grid(column=0, row=1)

        self.debug_msg = Label(self.root, text='-')
        self.debug_msg.grid(column=0, row=1, columnspan=5)

        self.init_btn = Button(self.root, text='Reiniciar', command=self.cleanHandler)
        self.init_btn.grid(column=5, row=2)

        self.class_lbl = Label(self.root, text='Clase ==>')
        self.class_lbl.grid(column=0, row=2)

        self.current_mark = self.MARKS[0]
        self.class_btn = Button(self.root, text=self.current_mark, command=self.classButtonHandler)
        self.class_btn.grid(column=1, row=2)

        self.mode_lbl = Label(self.root, text='MODO ==>')
        self.mode_lbl.grid(column=2, row=2)

        self.current_mode = self.MODES[0]
        self.mode_btn = Button(self.root, text=self.current_mode, command=self.modeButtonHandler)
        self.mode_btn.grid(column=3, row=2)

        self.k_lbl = Label(self.root, text='K ==>')
        self.k_lbl.grid(column=2, row=3)

        self.k_txt = Entry(self.root, width=2, text='3')
        self.k_txt.grid(column=3, row=3)

        self.root.mainloop()

    def modeButtonHandler(self):
        if self.mode_btn['text'] == self.MODES[0]:
            self.mode_btn.config(text=self.MODES[1])
            self.class_btn['state'] = DISABLED
            self.current_mode = self.MODES[1]
        else:
            self.mode_btn.config(text=self.MODES[0])
            self.class_btn['state'] = NORMAL
            self.current_mode = self.MODES[0]

    def classButtonHandler(self):
        if self.class_btn['text'][-1] == self.MARKS[0]:
            self.class_btn.config(text=self.MARKS[1])
            self.current_mark = self.MARKS[1]
        else:
            self.class_btn.config(text=self.MARKS[0])
            self.current_mark = self.MARKS[0]

    def cleanHandler(self):
        for p in self.axis_points: 
            self.axis.delete(p)
        del self.axis_points[:]
        for pr in self.axis_predictions: 
            self.axis.delete(pr)
        del self.axis_predictions[:]
        for l in self.lines:
            self.axis.delete(l)
        del self.lines[:]
        self.points = [] 
        self.labels = []

    def clickCallback(self, event):
        x = event.x
        y = event.y
        if self.current_mode == 'DATASET':
            self.points.append((x, y))
            self.labels.append(1 if self.current_mark == 'X' else 0)
            self.axis_points.append(
                self.axis.create_text(
                    x,
                    y,
                    text=self.current_mark,
                    fill='red' if self.current_mark == 'X' else 'dark green'
                )
            )
        else:
            # predict knn
            self.predictKnn(x, y)
        print(event.x, event.y)

    def predictKnn(self, x_ex, y_ex):
        # clean previous lines
        for l in self.lines:
            self.axis.delete(l)
        self.lines = []
        # set up dataset
        X = np.array(self.points)
        y = np.array(self.labels)
        example = np.array([x_ex, y_ex])
        k = int(self.k_txt.get())
        print(f'k: {k}')
        # call Knn class
        pred_label, neighbors, labels = self.knn.predict(X, y, example, k)
        prediction = 'X' if pred_label == 1 else 'O'
        # draw knn lines
        for n, label in zip(neighbors, labels):
            print(n, label)
            line = self.axis.create_line(
                n[0],
                n[1],
                x_ex,
                y_ex,
                fill='coral' if label == 1 else 'lime green')
            self.lines.append(line)

        # draw prediction
        self.axis_predictions.append(
            self.axis.create_text(
                x_ex,
                y_ex,
                text=prediction,
                fill='indian red' if pred_label == 1 else 'OliveDrab4',
                font=('freemono', 14, 'bold')
            )
        )


if __name__ == '__main__':
    app = KnnDemoApp()
