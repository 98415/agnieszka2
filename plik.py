
def dodawanie(a,b):
 return a + b
def get_info():
  return "To jest program kalkulator stworzony przez Gunie"
try:
 a = int(input("Podaj pierwsza liczbe:"))
 b = int(input("Podaj druga liczbe:"))
 print(dodawanie(a,b))
except ValueError as ve:
 print("wprowadzono bledne dane")
print(get_info())
input()