# Peshka

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
 
if y1 == 2 and y1 != 1:
  if x1 == x2 and y2 == y1 + 1 or y2 == y1 + 2:
    print('YES')
  else:
    print("NO")
else:
  if x1 == x2 and y1 + 1 == y2 and y1 != 1:
    print("YES")
  else:
    print("NO")