import copy

#rawdata = [0,3,6]
rawdata = [15,5,1,4,7,0]

#e=10
p1_e=2020
p2_e=30000000

num={}
for n,i in enumerate(rawdata):
  num[i] = n

current_count = len(num)
next_num = 0

def game(cc, nn, e):
  num={}
  for n,i in enumerate(rawdata):
    num[i] = n
  for c in range(cc, e):
    cn = nn
    if cn not in num:
      nn = 0
    else:
      nn = c - num[cn]
    num[cn] = c
  return cn


print('Part 1:',game(current_count, next_num, p1_e))

print('Part 2:',game(current_count, next_num, p2_e))