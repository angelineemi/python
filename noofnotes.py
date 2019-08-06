def no_notes(a):
  Q = [500, 200, 100, 50, 20, 10]
  notes = 0
  for i in range(6):
    q = Q[i]
    notes += int(a / q)
    a = int(a % q)
  if a > 0:
    notes = -1
  return notes
print(no_notes(880))
print(no_notes(1000))
