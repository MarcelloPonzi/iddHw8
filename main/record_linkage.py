import pandas as pd
import recordlinkage
import numpy
from recordlinkage.preprocessing import clean, phonetic


dfA = pd.read_csv('../MergedDS/ds_output-filtered.csv')



indexer = recordlinkage.Index()
indexer.random(10000000)
candidate_links = indexer.index(dfA)

# Comparison step
compare_cl = recordlinkage.Compare()

compare_cl.exact("name", "name", label="name")


features = compare_cl.compute(candidate_links, dfA)

# Classification step
matches = features[features.sum(axis=1) > 3]
print(len(matches))