
import random
import time
from random import sample

import numpy as np
import pandas as pd

def dados_wokwi(n_samples= 3000):
    np.random.seed(555)
    time.sleep(1.5)
    print("Carregando data set. . .")

    dados_temperatura = np.random.normal(loc= 27 , scale= 2,size=n_samples)
    dados_umidade = np.random.uniform(low=0, high=100,size=n_samples)
    acc_x = np.random.normal(loc=0, scale=0.3, size=n_samples)
    acc_y = np.random.normal(loc=0, scale=0.3, size=n_samples)
    acc_z = np.random.normal(loc=9.81, scale=0.4, size=n_samples)
    vibracao_total = np.sqrt(acc_x ** 2 + acc_y ** 2 + (acc_z - 9.81) ** 2)
    corrente = np.random.normal(loc= 5, scale=1.5,size=n_samples)

    df = pd.DataFrame({
        'Temperatura': dados_temperatura,
        'Umidade': dados_umidade,
        'Vibração': vibracao_total,
        'Corrente': corrente
    })
    return df
