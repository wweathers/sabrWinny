import pandas as pd
import numpy as np

df = pd.read_csv('BaseballCsv\Batting.csv')

player = input("Insert the player's name: ")
hits = float(input("How many hits does the player have in total?: "))
doubles = float(input("How many doubles?: "))
triples = float(input("How many triples?: "))
homeRuns = float(input("How many HomeRuns?: "))
atBats = float(input("How many total at bats?: "))

singles = hits - doubles - triples - homeRuns
totalBases = singles+(doubles*2)+(triples*3)+(homeRuns*4)
slugging = round((totalBases/atBats), 3)
print(player + "'s SLG% is " + str(slugging))