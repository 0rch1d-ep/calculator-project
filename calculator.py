def get_number(prompt)
 while True:
  try:
   return float(input(prompt))
  except ValueError:
   print("Ошибка: введите число")

def add(a,b);
 return a + b

def subtract(a,b):
 return a - b

def multuply(a,b):
 return a * b

def divide(a,b):
 if b != 0:
  return a / b
 else:
  return "NULL"

print("Pr0sToi kAlkulAt0r")
print("OpErAtor: +,-,*,/")
