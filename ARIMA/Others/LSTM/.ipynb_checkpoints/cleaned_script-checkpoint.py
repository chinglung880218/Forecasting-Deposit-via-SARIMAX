
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime
from statsmodels.tsa.stattools import adfuller
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
import statsmodels
import statsmodels.api as sm
from statsmodels.graphics import tsaplots

path = r"C:\Users\publi\OneDrive\TriLeafTech\Education\DukeUniversity\Duke-Math789\daily-treasury-rates-2022.csv"
df = pd.read_csv(path)

#define a function to preprocess the x and y variables
def prepare_data(timeseries_data, n_steps):
    x, y = [], []
    for i in range(len(timeseries_data)):
        end_ix = i + n_steps  # find the end of this pattern
        if end_ix > len(timeseries_data) - 1:  # if longer than timeseries, break the loop
            break
        # gather the input and output sequences
        seq_x = timeseries_data[i:end_ix]
        seq_y = timeseries_data[end_ix]
        x.append(seq_x)
        y.append(seq_y)
    return np.array(x), np.array(y)

n_steps = 60
n_features = 1

x, y = prepare_data(np.array(df[['1 Mo']]), n_steps)
x.shape, y.shape

y[188]

# initiate the model
model = Sequential()  # initiate the model
# Add input layer with 50 neurons
model.add(LSTM(50, activation='relu', return_sequences=True, input_shape=(n_steps, n_features)))
# Add second layer with 50 neurons
model.add(LSTM(50, activation='relu'))
# Add a fully connected output layer with 1 output
model.add(Dense(1))
# compile the model
model.compile(optimizer='adam', loss='mse')

# fit the model
model.fit(x, y, epochs=300, verbose=1)

yhat = model.predict(x[185::], verbose=0)
yhat
