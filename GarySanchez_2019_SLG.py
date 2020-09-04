import numpy as np
import pandas as pd

batterTable = pd.read_csv('BaseballCsv\Batting.csv')

garySanchez = batterTable.iloc[107102]

atBats = garySanchez[6]
hits = garySanchez[8]
doubles = garySanchez[9]
triples = garySanchez[10]
homeRuns = garySanchez[11]
singles = hits - doubles - triples - homeRuns
totalBases = singles+(doubles*2)+(triples*3)+(homeRuns*4)
slugging = totalBases/atBats
sluggingPercentage = round(slugging, 3)

print("Gary Sanchez's 2019 SLG% was " + str(sluggingPercentage))
