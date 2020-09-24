# knn-demo
simple demo for knn algorithm

## Install and run

1. Create virtualenv
    ```bash
    python3 -m venv env
   ```
2. Activate virtualenv
    ```bash
    source env/bin/activate
   ```
3. Install dependencies
    ```bash
    pip install -r requirements.txt
   ```
4. Run program
```
python knn_demo.py
```

## How to use
There are two modes for the program: 
  - **DATASET** mode allows you to enter samples for the dataset, with the Class button you can toggle between 2 classes. For adding a new example just click on the white canvas.
  - **PREDICTION** mode call the knn implementation using the K value in the text box. For performing a prediction just click on the canvas.

You can change the mode of the app by pushing the button with the current mode, this will toggle the mode.
## Algorithm

This demo implements a simple version of KNN algorithm
for binary classification using numpy.

The implementation can be found in [knn.py](knn.py).
