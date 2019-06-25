for a in range(int(input())):
  n = int(input())
  one = list(map(int,input().split()))
  two = list(map(int,input().split()))
  alice = sum(one) - max(one)
  bob = sum(two) - max(two)
  if alice > bob : 
    print("Bob")
  elif bob > alice : 
    print("Alice")
  else:
    print("Draw")