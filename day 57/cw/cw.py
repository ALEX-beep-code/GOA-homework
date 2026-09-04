spaceship = {
    "status": "active",
    "fuel": "full",
    "speed": "high",
    "passangers": "a lot"
}

print(spaceship["fuel"])

spaceship["fuel"] = "half"

spaceship["color"] = "white"

del spaceship["speed"]

print(spaceship)

for value in spaceship.values():
    print(value)

for key in spaceship.keys():
    print(key)

for item in spaceship.items():
    print(item)