import math
# Variables of the gun.

# Gunname = ("HK 416A5")
# Guncartridge = ("5.56x45mm NATO")
# Round = ("5.56x45mm HP")
# Roundvelocity = 947 #m/s

# Chose the building and assigned the variables.

# Building = ("El Choli")
# Buildingheight = 48.5 #meters
# gravity = 9.8 #m/s

def experiment( Gunname:str, Guncartridge:str, Round:str, Roundvelocity:float, Building:str, Buildingheight:float, gravity:float):
    # Im calculating time and DeltaX.

    time = (math.sqrt(2 * Buildingheight/gravity))
    DeltaX = (Roundvelocity * time)

    print(f"I shot a projectile from {Building}, it's {Buildingheight} meters high. It goes at {Roundvelocity} and it takes about {time} seconds to reach the ground. The distance covered is {DeltaX}.")

experiment("HK 416A5", "5.56x45mm NATO", "5.56x45mm HP", 947, "El Choli", 48.5, 9.8)