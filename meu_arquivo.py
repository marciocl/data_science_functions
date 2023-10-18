import pandas as pd
import numpy as np
import seaborn as sns

# Load Titanic dataset
df_titanic = sns.load_dataset('titanic')

df_titanic.to_csv('titanic.csv')
