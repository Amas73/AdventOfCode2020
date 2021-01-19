import math

#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_12_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_12_training_v2.txt'
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_12.txt'

rawdata = [r.strip('\n') for r in open(fn).readlines()]

y,x = 0,0
dir={'N':[-1,0],'E':[0,1],'S':[1,0],'W':[0,-1],'F':[0,1]}

for i in rawdata:
  if i[0] in ['L','R']:
    if i[0] == 'L':
      a=-1
    else:
      a=1
    angle = math.radians(a*int(i[1:]))
    yt = round(math.sin(angle) * (dir['F'][1]) + math.cos(angle) * (dir['F'][0]))
    xt = round(math.cos(angle) * (dir['F'][1]) - math.sin(angle) * (dir['F'][0]))
    dir['F']=[yt,xt]
  else:
    d = i[0]
    n = int(i[1:])
    y += dir[d][0]*n
    x += dir[d][1]*n

print ('Part 1:',abs(y)+abs(x))
