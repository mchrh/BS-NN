from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, LeakyReLU
from keras import backend


## Normalize the data exploiting the fact that the BS Model is linear homogenous in S,K
df["Stock Price"] = df["Stock Price"]/df["Strike Price"]
df["Call Price"] = df["Call Price"]/df["Strike Price"]

# splitting data into training and test set
n=30000

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
