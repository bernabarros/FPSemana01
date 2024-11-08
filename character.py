creatures = []
life = []
level = []
stats = (life,level)
creature_count = 0

while creature_count < 3:

    creatures.append(input(""))
    life.append(input(""))
    level.append(input(""))
    creature_count = creature_count + 1

print("[['" + creatures[0] + "', " + "(" + life[0] + ", " + level[0] + ")], " + 
      "['" + creatures[1] + "', " + "(" + life[1] + ", " + level[1] + ")], " + 
      "['" + creatures[2] + "', " + "(" + life[2] + ", " + level[2] + ")]]")

if level[0] > level[1] and level[0] > level[2]:
    print(creatures[0])
    if level[1] > level[2]:
        print(creatures[1])
        print(creatures[2])
    else:
        print(creatures[2])
        print(creatures[1])

if level[1] > level[0] and level[1] > level[2]:
    print(creatures[1])
    if level[0] > level[2]:
        print(creatures[0])
        print(creatures[2])
    else:
        print(creatures[2])
        print(creatures[0])

if level[2] > level[0] and level[2] > level[1]:
    print(creatures[2])
    if level[0] > level[1]:
        print(creatures[0])
        print(creatures[1])
    else:
        print(creatures[1])
        print(creatures[0])


