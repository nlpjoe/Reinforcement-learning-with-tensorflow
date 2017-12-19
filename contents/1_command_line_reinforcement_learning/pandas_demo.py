from __future__ import print_function
import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df['A'], df.A)
print(df[0:3], df['20130102':'20130104'])
