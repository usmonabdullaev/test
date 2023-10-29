x1, y1, x2, y2 = map(int, input().split())

first = ""
second = ""

if y1 == x1 or y1 % 2 == 0 and x1 % 2 == 0 or y1 % 2 != 0 and x1 % 2 != 0:
  first = "BLACK"
else:
  first = "WHITE"
  

if y2 == x2 or y2 % 2 == 0 and x2 % 2 == 0 or y2 % 2 != 0 and x2 % 2 != 0:
  second = "BLACK"
else:
  second = "WHITE"

if first == second:
  print("YES")
else:
  print("NO")