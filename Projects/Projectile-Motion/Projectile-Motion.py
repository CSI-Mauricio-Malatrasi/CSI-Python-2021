import math
from ExperimentData import ExperimentData

# Gunname = ("HK 416A5")
# Guncartridge = ("5.56x45mm NATO")
# Round = ("5.56x45mm HP")
# Roundvelocity = 947 #m/s
# Building = ("El Choli")
# Buildingheight = 48.5 #meters
# gravity = 9.8 #m/s

def experiment(experimentData:ExperimentData):
    # Im calculating time and DeltaX.

    time = (math.sqrt(2 * experimentData.Buildingheight/experimentData.gravity))
    DeltaX = (experimentData.Roundvelocity * time)

    print(f"I shot a projectile from {experimentData.Building}, it's {experimentData.Buildingheight} meters high. It goes at {experimentData.Roundvelocity} and it takes about {time} seconds to reach the ground. The distance covered is {DeltaX}.")


# experimentData = {
#     "Gunname" : "HK 416A5",
#     "Guncartridge" : "5.56x45mm NATO",
#     "Round" : "5.56x45mm HP",
#     "Roundvelocity" : 947,
#     "Building" : "El Choli",
#     "Buildingheight" : 48.5,
#     "gravity" : 9.8
# }

myData = ExperimentData("HK 416A5", "5.56x45mm NATO", "5.56x45mm HP", 947, "El Choli", 48.5, 9.8)

experiment(myData)