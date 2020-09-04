player = input("Which player? ")

hits = float(input("How many hits does the player have? "))
AB = float(input("How many total at bats? "))

BA = round((hits/AB), 3)
print(player + "'s Batting Average is " + str(BA))