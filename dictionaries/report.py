def main():
    spacecraft = {"name": "James webb"}
    spacecraft["distance"] = 0.01
    spacecraft.update(
        {"orbit": "Sun", "meters_away": convert_au_to_m(spacecraft["distance"])}
    )
    print(print_report(spacecraft))


def print_report(data):
    return f"""
        ========= REPORT =========

          name, {data["name"]}
          distance , {data.get("distance", "unknown")} AU
          Orbit , {data.get("orbit", "Unknown")}
          away from earth , {data["meters_away"]}

        ==========================
          """


def convert_au_to_m(au):
    return au * 149597870700


main()
