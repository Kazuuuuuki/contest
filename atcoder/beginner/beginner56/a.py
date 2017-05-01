a = input().split()

if(a[0] == "H"):
  if(a[1] == "H"):
    print("H")
  else:
    print("D")
else:
  if(a[1] == "H"):
    print("D")
  else:
    print("H")