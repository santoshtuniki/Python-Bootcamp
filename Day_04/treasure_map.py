line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input('Where do you want to place the treasure: \n')
location = ['a', 'b', 'b']

col = location.index(position[0].lower())
row = int(position[1])-1
map[row][col] = 'X'

print(f"{line1}\n{line2}\n{line3}")
