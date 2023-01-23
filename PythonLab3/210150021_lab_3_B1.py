import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from myfunctions import euler

func = lambda x: 0.5*x*(1-x)

arg_list = [func, 0.1, 20, 1.1]

x_values, t_values = euler(*arg_list)

df = pd.DataFrame({'Time': t_values, 'X': x_values})
df.to_csv('time_vs_x_data', index = False)

plt.plot(t_values, x_values)
plt.show()