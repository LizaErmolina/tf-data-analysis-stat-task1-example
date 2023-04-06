import pandas as pd
import numpy as np


chat_id = 33259271 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
      n = len(x)
    print(n)
    t = 46
    lam = x.mean()/t
    return lam # Ваш ответ
