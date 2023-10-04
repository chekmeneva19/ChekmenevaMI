domen = input()
new_dom = ''
while 1:
    if len(domen) > 0:
        str = domen[0]
        if str!= '.':
            new_dom += str
            domen = domen[1::]
        else:
            print(new_dom)
            domen = domen[1::]
            new_dom = ''
    else:
        print(new_dom)
        break
        
    
