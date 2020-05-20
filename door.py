open_door = []
close_door = []
door = [False] * 100
def walk(n): # Функция "прогулки"
    for i in range(n,len(door),n+1): # Подходим к каждой N двери.
        door[i] = not door[i]
    return door

for n in range(0,100,1):
    door = walk(n)
for i in range(0,len(door),1): # Проверям открыта дверь(True) или закрыта(False)
    if door[i] == True:
        open_door.append(i+1)
    else:
        close_door.append(i+1)
print(f"{len(open_door)} Open door:")
print(open_door)
print(f"{len(close_door)} Close door:")
print(close_door)
