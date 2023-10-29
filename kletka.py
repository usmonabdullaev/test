data = {
  "A": 1,
  "B": 2,
  "C": 3,
  "D": 4,
  "E": 5,
  "F": 6,
  "G": 7,
  "H": 8
}

a = input()

STR = data[a[0]]

INT = int(a[1])

if STR == INT or STR % 2 == 0 and INT % 2 == 0 or STR % 2 != 0 and INT % 2 != 0:
  print("BLACK")
else:
  print("WHITE")
