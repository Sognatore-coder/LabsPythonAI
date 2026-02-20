s = input()
first_f = s.find('f')
last_f = s.rfind('f')

if first_f != -1:  
    if first_f == last_f:
        print(first_f)  
    else:
        print(first_f, last_f)
