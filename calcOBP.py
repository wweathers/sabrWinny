player = input("Which player? ")

hits = float(input("How many hits does the player have: "))
walks = float(input("How many intentional walks?: "))
hbp = float(input("How many HBP's?: "))

atBats = float(input("How many total at bats?: "))
sf = float(input("How many SAC flys?: "))

numerator = hits+walks+hbp
denomenator = atBats+walks+hbp+sf

onBasePercentage = round((numerator/denomenator), 3)
print(player + "'s On-Base Percentage is " + str(onBasePercentage))