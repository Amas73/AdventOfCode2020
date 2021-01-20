#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_13_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_13_training_v2.txt'
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_13.txt'

rawdata = [r.strip('\n') for r in open(fn).readlines()]

tm = int(rawdata[0])

bus = {}
for sc in rawdata[1].split(','):
  if sc != 'x':
    bus[sc] = (((tm//int(sc))+1)*int(sc))-tm

bus_id = min(bus, key=bus.get)
print ('Part 1:', int(bus_id) * bus[bus_id])

lst = []
for n, sc in enumerate(rawdata[1].split(',')):
  if sc != 'x':
    lst.append([n,int(sc)])
lst.sort(key=lambda z: z[1])
tm = lst[0][1]
interval = 1
for n,sc in lst:
  while not((tm + n) % int(sc)==0):
    tm += interval
  interval *= sc
  

print ('Part 2:', tm)
