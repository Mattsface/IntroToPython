#!/usr/bin/env python


def main():

    hex_dict = {}

    list = [ (x, hex(x)) for x in range(0, 16)]

    for x in list:
        hex_dict[x[0]] = x[1]

    print hex_dict


    new_hex_dict = { x: hex(x) for x in range(0, 16)}

    print new_hex_dict
    food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}


    new_dict = { key: value.count("a") for key, value in food_prefs.items() }

    print new_dict

if __name__ == "__main__":
    main()
