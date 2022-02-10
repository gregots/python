from urllib.request import Request, urlopen
import json
import pandas as pd
from scipy.stats import entropy
round=1604344
randomnums=[]
for i in range(20):
    req = Request("https://drand.cloudflare.com/public/"+str(round), headers={'User-Agent': 'Mozilla/5.0'})
    webpage =json.load(urlopen(req))
    randomnums.append(webpage["randomness"])
    round-=1

pd_series = pd.Series(randomnums)
counts = pd_series.value_counts()
entropy = entropy(counts)
print(entropy)




