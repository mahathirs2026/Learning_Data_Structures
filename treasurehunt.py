island_map = [3, 4, 2, 1, 99, -1]

#each number is the index of the next island you need to jump on starting with index 0

i =0
visited_islands = set()
while island_map[i] != -1 :
    visited_islands.add(i)
    print("Visiting island", i)
    i = island_map[i]

    if i == -1:  
        print("Treasure found!")
        break

    elif i in visited_islands:
   
        print("you are in a loop! no treaure in this island")
        break

    elif i >= len(island_map):
        print("You fell off the map!")
        break
    


