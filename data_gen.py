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


def bs_div(S,K,T,r,q,sigma,option):
    d1=(np.log(S/K)+(r-q+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2=(np.log(S/K)+(r-q-0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    if option=='call':
      c=(S*np.exp(-q*T)*si.norm.cdf(d1,0.0,1.0)-K*np.exp(-r*T)*si.norm.cdf(d2,0.0,1.0))
      result=c
    elif option=='put':
      p=(K*np.exp(-r*T)*si.norm.cdf(-d2,0.0,1.0)-S*np.exp(-q*T)*si.norm.cdf(-d1,0.0,1.0))
      result=p

    return result



def data_gen_to_csv(N):
    # generating random values for volatility, strike, maturity
    r=0.
    S=1.
    sigma_lower=0.1
    sigma_upper=1.
    T_lower=0.03
    T_upper=1.
    K_lower=0.6
    K_upper=1.2
    q_lower=0.01
    q_upper=0.08

    sigma=np.random.uniform(sigma_lower,sigma_upper, N)
    maturity=np.random.uniform(T_lower,T_upper,N)
    strike=np.random.uniform(T_lower, T_upper, N)
    dividend=np.random.uniform(q_lower, q_upper, N)

    # computing call prices
    call=[]
    for i in range(0,N):
        call.append(bs(S,strike[i], maturity[i], r, sigma[i], option='call'))

    # creating dataframes with the columns : volatility, maturity, strike, call price
    df=pd.DataFrame()
    df['Vol']=sigma
    df['T']=maturity
    df['K']=strike
    df['Call']=call

    df.to_csv('data/x.csv') # exporting the data as a csv


data_gen_to_csv(10)
