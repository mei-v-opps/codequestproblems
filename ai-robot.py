import string

for i in range(int(input())):
    face = 1
    command = input().split(" ")
    if(command[2] == "N"):
        face = 1
    elif(command[2] == "E"):
        face = 2
    elif(command[2] == "S"):
        face = 3
    elif(command[2] == "W"):
        face = 4
    coordx, coordy = int(command[0]), int(command[1])
    sface = command[2]
    dir = list(command[3])
    for r in range(len(dir)):
        if(dir[r] == "R"):
            face+=1
            if(face == 5):
                face = 1
            elif(face == 0):
                face = 4
        elif(dir[r] == "L"):
            face-=1
            if(face == 5):
                face = 1
            elif(face == 0):
                face = 4
        else:
            if(face%4 == 0):
                coordx-=1
                sface = "W"
            elif(face%3 == 0):
                coordy-=1
                sface = "S"
            elif(face%2 == 0):
                coordx+=1
                sface = "E"
            elif(face%1 == 0):
                coordy+=1
                sface = "N"
    if(face == 4):
        sface = "W"
    elif(face == 3):
        sface = "S"
    elif(face == 2):
        sface = "E"
    elif(face == 1):
        sface = "N"
    print(f"{coordx} {coordy} {sface}")