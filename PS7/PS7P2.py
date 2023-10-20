aye = 1
bee = 1

print(aye)
print(bee)

for count in range(1, 19, 1):
  cee = aye + bee
  print(cee)
  aye = bee
  bee = cee
