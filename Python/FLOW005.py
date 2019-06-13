for a in range(int(input())):
  coins = 0 
  value = int(input())
  coins += value // 100
  value = value - (value//100)*100

  coins += value // 50
  value = value - (value//50)*50
  
  coins += value // 10
  value = value - (value//10)*10

  coins += value // 5
  value = value - (value//5)*5

  coins += value // 2
  value = value - (value//2)*2

  coins += value // 1
  value = value - (value//1)*1
  print(coins)
