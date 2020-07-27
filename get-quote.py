import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()


  last = 13
  rnd = random.randint(0, last)

  print(quotes[rnd].strip('\n'))

  new = int(input('Enter number between 1 and 13: \n'))
  print(quotes[new].strip('\n'))
  
  new2 = input('Enter new string: \n')
  f = open("quotes.txt", "a")
  f.write(new2)
  f.close()
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  print(quotes[-1])
  
if __name__== "__main__":
  primary()
