
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_16_training.txt'
#fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_16_training_p2.txt'
fn = 'c:/LocalData/aslade/AdventOfCode/2020/input_16.txt'

rawdata = [r.strip('\n') for r in open(fn).readlines()]

ticket_fields=rawdata[:rawdata.index('')]
my_ticket=rawdata[rawdata.index('your ticket:')+1].split(',')
nearby_tickets=[x.split(',') for x in rawdata[rawdata.index('nearby tickets:')+1:]]
t_fields = {}

for typ, rnge in [x.split(': ') for x in ticket_fields]:
  t_fields[typ] = []
  tmp = rnge.split(' or ')
  for x in tmp:
    t_fields[typ].append(x.split('-'))
ticket_fields=None

error_rate = 0
invalid_tickets = []
for t in nearby_tickets:
  ticket_valid = True
  for f in t:
    valid = False
    for a,b in sum(t_fields.values(), []):
      if (int(f)>=int(a) and int(f)<=int(b)):
        valid = True
    if not valid:
      error_rate += int(f)
      ticket_valid =False
  if not ticket_valid:
    invalid_tickets.append(t)

for t in invalid_tickets:
  nearby_tickets.remove(t)

print ('Part 1:', error_rate)


field_lookup = 'departure'
field_positions={x:[] for x in range(len(my_ticket))}
for n, v in enumerate(my_ticket):
  for cl in t_fields:
    for a, b in t_fields[cl]:
      if (int(v) >= int(a) and int(v) <= int(b)):
        field_positions[n].append(cl)

for t in nearby_tickets:
  for n, v in enumerate(t):
    for cl in field_positions[n]:
      exists = False
      for a, b in t_fields[cl]:
        if (int(v) >= int(a) and int(v) <= int(b)):
          exists = True
      if not exists:
        field_positions[n].remove(cl)

completed_fields = []
while True:
  ones=[]
  for pos in field_positions:
    if len(field_positions[pos]) == 1 and pos not in completed_fields:
      ones.append(pos)
  for pos in ones:
    for p in field_positions:
      if p != pos and field_positions[pos][0] in field_positions[p]:
        field_positions[p].remove(field_positions[pos][0])
    completed_fields.append(pos)
  if len(completed_fields) == len(field_positions):
    break

ans = 1
for pos in field_positions:
  if field_lookup in field_positions[pos][0]:
    ans *= int(my_ticket[pos])

print('Part 2:', ans)