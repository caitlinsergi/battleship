from grid_setup import initialize_empty_grid, print_grid

grid = initialize_empty_grid()
#print(grid)

user_input = ["B1", "B2", "B3", "B4", "B7", "C6", "C7", "F1", "G1", "H1"]

def general_ship_placement(grid, user_input):
    dictionary_mapper = {"A":1, "B":3, "C":5, "D":7, "E":9, "F":11, "G":13, "H":15}
    for grid_spot in user_input:
        letter = grid_spot[0]
        number = grid_spot[-1]
        for dict_num, dict_row in grid.items():
            if number == dict_num:
                dict_row_split = []
                for element in dict_row:
                    dict_row_split.append(element)
                dict_row_split[dictionary_mapper[letter]] = "X"
                str_to_add = ''
                for element in dict_row_split:
                    str_to_add += element
                grid[number] = str_to_add
    returned_grid = print_grid(grid)
    return returned_grid


def pick_aircraft_carrier_placement():
    ship_size = 4
    user_input = []
    while ship_size > 0:
        aircraft_input = input("Please choose where you want to place your aircraft carrier. It is big enough for four spots. ")
        user_input.append(aircraft_input)
        ship_size -= 1
    return user_input


pick_aircraft_carrier_placement()