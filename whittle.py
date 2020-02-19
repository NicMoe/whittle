import numpy as np
import pandas as pd

# 1. set up / import data frame (table) of relevant proportions
df2 = pd.DataFrame(np.array([[1000, 'single family', 0.64, 'transit proximity', 0.22],
    [1000, 'row house', 0.14, 'transit proximity', 0.32],
    [1000, 'multi-family', 0.22, 'transit proximity', 0.65]]),
    columns=['n', 'group', 'proportion', 'variable', 'sub_prop'])

print(df2)

# 2. calculate ranges of possible values for each metric's proportions