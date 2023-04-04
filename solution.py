import pandas as pd
import numpy as np


chat_id = 5991293770 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    #sample_mean = np.mean(x)
    #sample_var = np.var(x)
    #a = np.log(sample_mean/np.sqrt(sample_var/sample_mean**2 +1))
    return np.log(x-855).mean()
