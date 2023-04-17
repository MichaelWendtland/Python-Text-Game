with open('story.txt','r', encoding = "utf8") as s:
    a = s.readlines()
    i = 1
    line = {}
    for x in a:
        x = x.rstrip('\n')
        x = x.rstrip('')
        line[i] = x
        i += 1


#LINES and their location:
