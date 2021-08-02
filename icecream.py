icecream= ["flavors", "salty"] 
tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]
icecream.append(99)

import random
random.shuffle(tlgclass)


while True:
  try:
    number = input("number 0-19: ")
    name = int(number)
    if (0 < name and name < 20):
          icecream.append(name)
          break
  except (ValueError):
    continue


print("<{}> <{}>, and <{}> chooses to be <{}>".format(icecream[2],icecream[0],tlgclass[3],icecream[1]))


