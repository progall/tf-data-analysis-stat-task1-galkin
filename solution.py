import pandas as pd
import numpy as np
import math

chat_id = 322172960 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    for i in x:
        i = i/10-37+math.exp(1)
        #i = i/10+math.exp(1)
    
    return x.mean() # Ваш ответ
