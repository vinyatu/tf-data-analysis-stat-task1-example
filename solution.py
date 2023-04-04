import pandas as pd
import numpy as np


chat_id = 5991293770 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    sample_mean = np.mean(x)
    sample_var = np.var(x)
    a = np.log(sample_mean/np.sqrt(sample_var/sample_mean**2 +1))
    return a # Ваш ответ
