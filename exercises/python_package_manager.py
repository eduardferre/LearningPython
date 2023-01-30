# PIP https://pypi.org

import numpy as np

np_array = np.array([35, 24, 58, 49, 12, 28, 76])

print(np_array * 2)

import pandas

import requests # hacer peticiones a una API

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response.status_code)
#print(response.json())

# Arithmetics Package

from packages import arithmetics

print(arithmetics.sum_values(1, 4))