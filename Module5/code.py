""" 
Solution code for the Module 05 Workshop.
"""
from typing import Tuple

def string_games(name:str = "Guido van Rossum") -> None:
    """Plays different games with a name. 

    Args:
        name (str, optional): name. Defaults to "Guido van Rossum".
    """
    length = len(name)
    print(f"Q1: {length}")

    first  = name[:5]
    length = len(first)
    print((first, length))

    first = name[:name.find(' ')]
    print((first, len(first)))


def get_area_name(data:str) -> str:
    """gets a location name out of the string of format

    PLACE,LATITUDE,LONGITUDE

    Args:
        data (str): string that matches the above pattern

    Returns:
        str: the name / PLACE
    """
    return data.split(',')[0]


def get_lat_long(data:str) -> Tuple[float, float]:
    """get a latitude, longitude  out of a string
    with the format PLACE,LATITUDE,LONGITUDE

    it converts the lat/long into floats, and assumes
    it is a decimal value format. no error checking happens. 

    Args:
        data (str): a string that matches 
        the format PLACE,LATITUDE,LONGITUDE

    Returns:
        Tuple[float, float]: latitude,longitude as a tuple
    """
    vals = data.split(",")
    lat = float(vals[1])
    lon = float(vals[2])
    return lat, lon  #multiple return values become a tuple by default

def show_pattern():
    """Just a call to show the various pattern functions"""
    locations = ("Boston,42.3395683,-71.0922272",
                 "San Francisco,37.79292,-122.4068792",
                 "Vancouver,49.2806832,-123.1178707")

    counter = 0
    while(counter < len(locations)):
        name = get_area_name(locations[counter])
        coords = get_lat_long(locations[counter])
        print(f"{name} can be found at coordinates: {coords}")
        counter += 1

def main():
    string_games() # defaults to "Guido van Rossum"
    print("##### What happens when we put in a different name? #####")
    string_games("Barbara Liskov")  
    ## why did find work, but just using the location didn't?

    print("### looking at patterns ###")
    show_pattern()




if __name__ == "__main__":
    main()

