import math

# Variables of the gun.

Gunname = ("HK 416A5")
Guncartridge = ("5.56x45mm NATO")
Round = ("5.56x45mm HP")
Roundvelocity = 947 #m/s

# Chose the building and assigned the variables.

Building = ("El Choli")
Buildingheight = 48.5 #meters
gravity = 9.8 #m/s

# Im calculating time and DeltaX.

time = (math.sqrt(2 * Buildingheight/gravity))
DeltaX = (Roundvelocity * time)