# This project can hide the treasure 'X' anywhere coordinately.
# 'index' function is applied.

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

treasure_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

# To specify the place to hide the treasure. Use 'A', 'B', 'C' for columns, and 1, 2, 3 for rows.
# rows after columns: Eg, A1, B3, ...

position = input()

abc = position[0].lower()
letters = ['a', 'b', 'c']
letter_index = letters.index(abc)
number_index = int(position[1]) - 1

treasure_map[number_index][letter_index] = 'X'

print(f'{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}')
