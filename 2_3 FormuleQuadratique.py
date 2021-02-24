# - Importation des module
import math

# - Programme principal
print("------------------------------------------------------------------------------------------")
x1 = int(input("Entre le nombre d'x1 : "))
y1 = int(input("Entre le nombre d'y1 : "))
x2 = int(input("Entre le nombre d'x2 : "))
y2 = int(input("Entre le nombre d'y2 : "))
print("------------------------------------------------------------------------------------------")
# - Premier parenthese
x = x2 - x1
parenthese1 = x * x

# - Deuxieme parenthese
y = y2 - y1
parenthese2 = y * y

# - Deuxieme_Premier parenthese
xy = parenthese1 + parenthese2

#Distance entre premier point et deuxieme point
sqrt = math.sqrt(xy)
print("La distance du point (x1,y1) et (x2,y2) est {}".format(sqrt))




