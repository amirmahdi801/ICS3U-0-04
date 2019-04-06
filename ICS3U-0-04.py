print ("Welcome to my program")
print ("please choose your language: 1.English 2.French 3.Spanish")
language = input()
language = int(language)
if language == 1:
    print ("hello my friend!")
elif language == 2:
    print ("requescate de patche")
elif language == 3:
    print ("Hola mi amigo")
elif language > 3:
    print ("wrong input!")
