import numpy as np
import pandas as pd
import scipy.stats as si


# fct that calculates option prices using B-S closed form formula

def bs(S,K,T,r,sigma,option):
  d1=(np.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
  d2=(np.log(S/K)+(r-0.5*sigma**2)*T)/(sigma*np.sqrt(T))

  if option=='call':
    c=(S*si.norm.cdf(d1,0.0,1.0)-K*np.exp(-r*T)*si.norm.cdf(d2,0.0,1.0))
    result=c
  elif option=='put':
    p=(K*np.exp(-r*T)*si.norm.cdf(-d2,0.0,1.0)-S*si.norm.cdf(-d1,0.0,1.0))
    result=p

  return result


# generating random values for volatility, strike, maturity
r=0.
S=1.
sigma_lower=0.1
sigma_upper=1.
T_lower=0.03
T_upper=1.
K_lower=0.6
K_upper=1.2

sigma=np.random.uniform(sigma_lower,sigma_upper, 100000)
maturity=np.random.uniform(T_lower,T_upper,100000)
strike=np.random.uniform(T_lower, T_upper, 100000)

# creating dataframes with the generated data
df=pd.DataFrame()
df['Vol']=sigma
df['T']=maturity
df['K']=strike

df.to_csv('x.csv')
