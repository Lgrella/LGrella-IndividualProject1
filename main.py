"""
Created on Tue Sep 19 2023
@author: lillygrella
"""
from lib import readin, get_summ_stats, make_line_graph

# Generate example data using common library
df = readin()

# Perform descriptive statistics using common library and Pandas
print("Summary Statistics using Pandas:")
stats = get_summ_stats(df)
print(stats)

# Generate scatter plot
make_line_graph(df)
