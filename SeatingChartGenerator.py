# a simple seating chart generator 
import random
from collections import defaultdict

# guest list with tag
guests = [
    {"name": "Penny", "tag": "bride_family"}, 
    {"name": "Greg", "tag": "bride_family"}, 
    {"name": "Aayden", "tag": "bride_family"}, 
    {"name": "Makayla", "tag": "bride_family"}, 
    {"name": "Gran", "tag": "bride_family"}, 
    {"name": "Alicia", "tag": "bride_family"}, 
    {"name": "Sal", "tag": "bride_family"}, 
    {"name": "Jake", "tag": "bride_family"}, 
    {"name": "Brandy", "tag": "groom_family"}, 
    {"name": "Danny", "tag": "groom_family"},
    {"name": "Nick", "tag": "groom_family"},
    {"name": "Hiedi", "tag": "groom_family"},
    {"name": "Simmons", "tag": "groom_family"},
    {"name": "Ransmey", "tag": "groom_family"},
    {"name": "Nana Hewitt", "tag": "groom_family"},
    {"name": "Nana Johnson", "tag": "groom_family"},
    {"name": "Cliff", "tag": "groom_family"},
    {"name": "Cliffs wife", "tag": "groom_family"},
    {"name": "Emily", "tag": "couple"}, 
    {"name": "Joaquin", "tag": "couple"}, 
    {"name": "Emily", "tag": "couple"},
    {"name": "Andrew", "tag": "couple"},
    {"name": "Marissa", "tag": "friend"},
    {"name": "Brynn", "tag": "couple"},
    {"name": "Spencer", "tag": "couple"},
    {"name": "Carly", "tag": "couple"},
    {"name": "Kyle", "tag": "couple"},
    {"name": "Ike", "tag": "friend"},
    {"name": "Will", "tag": "couple"},
    {"name": "Jo", "tag": "couple"},
    {"name": "Ella", "tag": "couple"},
    {"name": "Matt", "tag": "couple"},
    {"name": "Ricki", "tag": "friend"},
    {"name": "Sav", "tag": "friend"},
]

# function that groups guests by their tag
def group_guests_by_tag(guests):
    #create an empty list
    grouped = defaultdict(list)
    #append guest to list
    for guest in guests:
        grouped[guest["tag"]].append(guest)
    return grouped

# function to assign guests to tables
def assign_seating_grouped(guests, num_tables, seats_per_table):
    grouped = group_guests_by_tag(guests)
    # initialize table and seating capacities
    tables = {f"Table {i+1}": [] for i in range(num_tables)}
    capacities = {table: seats_per_table for table in tables}
    table_num = 1

    # helper function to fit an entire group to available tables
    def place_group(group):
        nonlocal table_num
        for guest in group:
            placed = False
            attempts = 0
            while attempts < num_tables:
                table = f"Table {((table_num - 1 + attempts) % num_tables) + 1}"
                if capacities[table] > 0:
                    tables[table].append(guest)
                    capacities[table] -= 1
                    placed = True
                    break
                attempts += 1
            if not placed:
                print(f"⚠️ No space left for guest: {guest['name']}")
        table_num += 1

    # place bride's family together
    bride_family = grouped.get("bride_family", [])
    random.shuffle(bride_family)
    place_group(bride_family)

    # place groom's family together
    groom_family = grouped.get("groom_family", [])
    random.shuffle(groom_family)
    place_group(groom_family)

    # place couples in pairs
    couples = grouped.get("couple", [])
    random.shuffle(couples)
    couple_pairs = [couples[i:i+2] for i in range(0, len(couples), 2)]

    for pair in couple_pairs:
        if len(pair) < 2:
            print(f"⚠️ Unpaired 'couple': {pair[0]['name']}")
            continue
        placed = False
        for i in range(num_tables):
            table = f"Table {(table_num + i - 1) % num_tables + 1}"
            if capacities[table] >= 2:
                tables[table].extend(pair)
                capacities[table] -= 2
                placed = True
                break
        if not placed:
            print(f"⚠️ No space left for couple: {[g['name'] for g in pair]}")
    table_num += 1

    # place friends together if available
    friends = grouped.get("friend", [])
    random.shuffle(friends)
    place_group(friends)

    return tables

# print the chart
def print_chart(tables):
    for table, guests in tables.items():
        print(f"\n{table} ({len(guests)} guests):")
        for guest in guests:
            print(f" - {guest['name']} ({guest['tag']})")

# run the program
if __name__ == "__main__":
    num_tables = 6
    seats_per_table = 6
    chart = assign_seating_grouped(guests, num_tables, seats_per_table)
    print_chart(chart)
