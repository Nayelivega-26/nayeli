import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
df = pd.DataFrame({'x': x, 'seno': np.sin(x), 'coseno': np.cos(x)})

df.plot(x='x', y=['seno', 'coseno'], color=['y', 'b'], linewidth=4)
plt.show()
