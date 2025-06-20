distances = {
    "Vioger 1": "163",
    "Vioger 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft name: ")
    try:
        au = float(distances[spacecraft])
    except ValueError:
        print(f"can't convert {distances[spacecraft]} to float ")
        return

    m = convert_au_to_m(au)
    print(f"{spacecraft} is {m} m away")


def convert_au_to_m(au):
    if not isinstance(au, (int, float)):
        raise TypeError("au must be int or float")
    return au * 149597870700


if __name__ == "__main__":
    main()
