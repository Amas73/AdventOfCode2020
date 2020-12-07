import re
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_05.txt'
in_data = [r for r in open(fn).readlines()]
#training data
#in_data = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']

rows=list(range(128))
seats=list(range(8))

seat_id=[]
for r in in_data:
  y=rows
  x=seats
  for c in r:
    if c == 'F' : y=y[:len(y)//2]
    if c == 'B' : y=y[len(y)//2:]
    if c == 'R' : x=x[len(x)//2:]
    if c == 'L' : x=x[:len(x)//2]
  s_id = y[0]*8 + x[0]
  seat_id.append(s_id)
print('Part 1: Highest seat ID: '+str(max(seat_id)))
seat_id.sort()
for i in range(seat_id[8],seat_id[len(seat_id)-8]):
  if i not in seat_id: print ('Part 2: My seat: '+str(i))
  