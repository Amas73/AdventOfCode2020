import re

fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_07.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_07_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_07_training_p2.txt'

rawdata = [r.strip('\n').strip('.') for r in open(fn).readlines()]
srch = 'shiny gold'

bags={}
for bag in rawdata:
  tb = bag.split(' bags contain ')
  bags[tb[0]]={}
  for sb in tb[1].split(', '):
    n = re.search('(\d+) (.*) bags?',sb)
    if n:
      bags[tb[0]][n[2]] = n[1]

result=[]
def inbag(search_str,bags_dict):
  for bag,bag_contents in bags_dict.items():
    if search_str in bag_contents and bag not in result:
      result.append(bag)
      inbag(bag,bags_dict)
  return result

inbag(srch,bags)
print('Part 1:',len(inbag(srch,bags)),'bags.')


def inner_bag_count(bag,bags_dict):
  if bags_dict[bag] =={}:
    return 0
  b=0
  for each_bag, c in bags_dict[bag].items():
    print(bag,'has',c,each_bag,'->',listsum(bags_dict[bag].values()))
    b += int(c)+(int(c)*inner_bag_count(each_bag,bags_dict))
  return b

print('Part 2:',inner_bag_count(srch,bags))
