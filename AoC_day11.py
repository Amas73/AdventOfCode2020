import copy

#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_11_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_11_training_v2.txt'
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_11.txt'

rawdata = [r.strip('\n') for r in open(fn).readlines()]

def occupied_seats(r,c,l,p=1):
  occupied = 0
  if p == 1:
    for y in range(r-1,r+2):
      for x in range(c-1, c+2):
        if y>=0 and y<len(l) and x>=0 and x<len(l[y]) and not(y==r and x==c):
          occupied += int(l[y][x]=='#')
  elif p == 2 :
    for seat in seat_lu[str(r)+','+str(c)]:
      occupied += l[seat[0]][seat[1]] == '#'
  return occupied

def adjust_seating(lst, q, pt=1):
  matched = False
  run_cnt = 1
  while not matched:
    matched = True
    tmp_lst = []
    for row in range(len(lst)):
      seats = ''
      for column in range(len(lst[row])):
        if lst[row][column] == 'L' and occupied_seats(row, column, lst, pt) == 0: seats += '#'
        elif lst[row][column] == '#' and occupied_seats(row, column, lst, pt) >= q: seats += 'L'
        else:
          seats += lst[row][column]
      tmp_lst.append(seats)
      if lst[row] != seats: matched = False
    lst = copy.copy(tmp_lst)
    run_cnt += 1
  seat_cnt = 0
  for z in lst:
    seat_cnt += z.count('#')
  return seat_cnt

print('Part 1:',adjust_seating(rawdata, 4))


seat_lu = {}
for r in range(len(rawdata)):
  for c in range(len(rawdata[r])):
    seat_lu[str(r)+','+str(c)]=[]
    ya, xa = -1, -1
    ym = len(rawdata)-1
    xm = len(rawdata[0])-1
    yb, xb = r, c
    while True:
      while True:
        yb += ya
        xb += xa
        if yb <0 or yb > ym or xb <0 or xb>xm or (ya==0 and xa==0) or ya >1:
          break
        if rawdata[yb][xb]=='L':
          seat_lu[str(r)+','+str(c)].append([yb,xb])
          break
      xa += 1
      if xa > 1:
        ya += 1
        xa = -1
      yb, xb = r, c
      if ya > 1:
        break

print('Part 2:',adjust_seating(rawdata, 5, 2))



