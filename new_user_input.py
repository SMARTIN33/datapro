from sys import argv

for element in argv :
    if'@' in element :
        parts=element.split("@") 
        if  ".com" not in parts[0] and ".com" in parts[1] and element [-4:] == ".com" :
                print(element[0:2]+"...@..." + element[-2:])

   