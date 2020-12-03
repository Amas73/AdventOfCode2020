fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_03.txt'
in_data = [r.rstrip('\n') for r in open(fn).readlines()]
#training data
#in_data = ['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.','..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#']
slopes=[[1,1], [3,1], [5,1], [7,1], [1,2]]

total=1
for run in slopes:
  trees=0
  x=0
  for i, row in enumerate(in_data):
    if i%run[1] == 0:
      t=x%len(row)
      if row[t]=="#": trees += 1
      x+=run[0]
  total = total * trees

print (total)