# a simple program to calculate how many are tables needed based on guest count
# the program will ask for total guest count, show how many tables are needed (min and max), 
# show leftover seats if not divisible, and output options are clearly grouped
# the program will also show a mixture of round and rectangle tables
import math

# define table options 
table_options = {
    "round": [
        {"name": '30" Round', "seatsMin": 2, "seatsMax": 3}, 
        {"name": '48" Round', "seatsMin": 6, "seatsMax": 8}, 
        {"name": '60" Round', "seatsMin": 8, "seatsMax": 10}, 
        {"name": '72" Round', "seatsMin": 10, "seatsMax": 12}, 
    ],
    "rectangle": [
        {"name": "6' Rectangle", "seatsMin": 6, "seatsMax": 6}, 
        {"name": "8' Rectangle", "seatsMin": 8, "seatsMax": 10}, 
    ]
}

# calculate table options based on guest count
def calculate_table_options(guest_count): 
    print(f"\n Table Options for {guest_count} Guests\n")

    # calculate min and max tables needed 
    for shape, tables in table_options.items():
        print(f"\n {shape.capitalize()} Tables:")
        # find all possibilities of number of tables with min and max seats
        for table in tables: 
            min_tables = math.ceil(guest_count / table["seatsMax"])
            max_tables = math.ceil(guest_count / table["seatsMin"])
            print(f"{table['name']}:")
            print(f"    - Min Needed: {min_tables} (at {table['seatsMax']} per table)")
            print(f"    - Max Needed: {min_tables} (at {table['seatsMin']} per table)")

# define table options for mix
round_tables = [
    {"name": '30" Round', "seatsMin": 2, "seatsMax": 3},
    {"name": '48" Round', "seatsMin": 6, "seatsMax": 8},
    {"name": '60" Round', "seatsMin": 8, "seatsMax": 10},
    {"name": '72" Round', "seatsMin": 10, "seatsMax": 12},
]

rectangle_tables = [
    {"name": "6' Rectangle", "seatsMin": 6, "seatsMax": 6},
    {"name": "8' Rectangle", "seatsMin": 8, "seatsMax": 10},
]

# function to calculate the different combinations of tables based on guest count
def mixed_table_combinations(guest_count):
    print(f"\n Mixed Table Options for {guest_count} Guests\n")
    
    combinations = []

    # loop through each round and rectangle table combinations 
    for rtype in round_tables: 
        for rectype in rectangle_tables: 
            # decide how many of each type to try 
            max_r = guest_count // rtype["seatsMin"] + 1
            max_rect = guest_count // rectype["seatsMin"] + 1

        # try all combinations
        for r_count in range(0, max_r + 1):
            for rect_count in range(0, max_rect + 1):
                # compute total seating range of that combination
                min_capacity = (r_count * rtype["seatsMin"]) + (rect_count * rectype["seatsMin"])
                max_capacity = (r_count * rtype["seatsMax"]) + (rect_count * rectype["seatsMax"])
                # check if combination is valid 
                if min_capacity <= guest_count <= max_capacity: 
                    combinations.append({
                        "round": {"type": rtype["name"], "count": r_count},
                        "rectangle": {"type": rectype["name"], "count": rect_count},
                        "total_tables": r_count + rect_count,
                        "min_seats": min_capacity,
                        "max_seats": max_capacity,
                        "extra_min": min_capacity - guest_count,
                        "extra_max": max_capacity - guest_count
                    })
    # sort by fewest tables
    combinations.sort(key=lambda x: x["total_tables"])

    if not combinations: 
        print("No valid combinations found.")
        return 

    # save the combination
    for combo in combinations[:20]:
        print(f"{combo['round']['count']} x {combo['round']['type']} + "
              f"{combo['rectangle']['count']} x {combo['rectangle']['type']} "
              f"(Total Tables: {combo['total_tables']})\n"
              f"   Seats: {combo['min_seats']}–{combo['max_seats']} "
              f"(Extra: {combo['extra_min']}–{combo['extra_max']})\n")

# run the program 
if __name__ == "__main__":
    try: 
        total_guests = int(input("Enter total guest count: "))
        calculate_table_options(total_guests)
        mixed_table_combinations(total_guests)
    except ValueError:
        print("Please enter a valid number.")