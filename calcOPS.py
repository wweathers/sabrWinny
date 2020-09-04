player = input("Which player? ")

hits = float(input("How many hits does the player have: "))
walks = float(input("How many intentional walks?: "))
hbp = float(input("How many HBP's?: "))

atBats = float(input("How many total at bats?: "))
sf = float(input("How many SAC flys?: "))

numerator = hits + walks + hbp
denomenator = atBats + walks + hbp + sf

OBP = round((numerator/denomenator), 3)


doubles = float(input("How many doubles?: "))
triples = float(input("How many triples?: "))
homeRuns = float(input("How many HomeRuns?: "))


singles = hits - doubles - triples - homeRuns
totalBases = singles+(doubles*2)+(triples*3)+(homeRuns*4)
slugging = round((totalBases/atBats), 3)
    
OPS = slugging + OBP
print(player + "'s OPS is " + str(OPS))