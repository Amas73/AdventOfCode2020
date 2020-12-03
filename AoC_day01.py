fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_01.txt'
in_data = [int(r) for r in open(fn).readlines()]

check=2020
for i, a in enumerate(in_data):
  for j, b in enumerate(in_data[i+1:]):
    for c in in_data[i+j+2:]:
      if a+b+c == check:
        print ('Entries ' + str(a) + ', ' + str(b) + ', '+ str(c) + ' produce: ' + str(a*b*c))