distances = {
    "vioger 1": 163,
    "vioger 2": 168,
    "pioneer 10": 80,
    "new horizon": 58,
    "pioneer 11": 44,
}


def main():
    # dictionary.keys() method
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from earth")

    # dictionary.values() method
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 149597870700


main()
