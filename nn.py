from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, LeakyReLU
from keras import backend
import numpy as np
import pandas as pd

# loading the data
df=pd.read_csv("data/options.csv")
df.head()



## Normalize the data exploiting the fact that the BS Model is linear homogenous in S,K
#df["Stock Price"] = df["Stock Price"]/df["Strike Price"]
#df["Call Price"] = df["Call Price"]/df["Strike Price"]

# splitting data into training and test set


"""n=30000

n_train=int(0.8*n)
train=df[0:n_train]
X_train = train[['Stock Price', 'Maturity', 'Dividends', 'Volatility', 'Risk-free']].values
y_train = train['Call Price'].values

test = df[n_train+1:n]
X_test = test[['Stock Price', 'Maturity', 'Dividends', 'Volatility', 'Risk-free']].values
y_test = test['Call Price'].values

# defining activation function
def custom_activation(x):
    return backend.exp(x)

# NN config : 6 input nodes, 4 hidden layers of 120 nodes each, 1 output node
nodes=120
model=Sequential()

model.add(Dense(nodes, input_dim=X_train.shape[1]))

model.add(LeakyReLU())
model.add(Dropout(0.25))

model.add(Dense(nodes, activation='elu'))
model.add(Dropout(0.25))

model.add(Dense(nodes, activation='relu'))
model.add(Dropout(0.25))

model.add(Dense(nodes, activation='elu'))
model.add(Dropout(0.25))

model.add(Dense(1))
model.add(Activation(custom_activation))

model.compile(loss='mse', optimizer='rmsprop') # using mean squared error as loss function, and RMSProp for optimization (I'll try Gradient Descent later)

# fitting the model to calibrate using the loss fct, we use 10 epochs
model.fit(X_train, y_train, batch_size=64, epochs=10, validation_split=0.1, verbose=2)

# function to check the accuracy of the model
def check_acc(y,y_hat):
    stats=dict()
    stats['diff']=y - y_hat

    # Mean Squared Error
    stats['mse']=mean(stats['diff']**2)
    print("MSE:", stats['mse'])
    # Root Mean Squared Error
    stats['squareMSE']=np.sqrt(stats['mse'])
    print("Squred MSE:", stats['squareMSE'])
    # Mean Absolute Error
    stats['mae']=np.mean(np.abs(stats['diff']))
    print("MAE:", stats['mae'])
    # Mean Percent Error
    stats['mpe']=np.sqrt(stats['mse']/np.mean(y))
    print("MPE:", stats['mpe'])


y_train_hat=model.predict(X_train)

# reducing dimensionality to match y_train dimensionality
y_train_hat=squeeze(y_train_hat)
check_acc(y_train, y_train_hat)"""
