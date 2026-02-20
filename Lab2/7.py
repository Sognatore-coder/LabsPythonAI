path = input()
draw_char = path[0]
movements = path[1:]

x,y=0,0
grid = {(0,0): draw_char}
min_x, max_x, max_y = 0, 0, 0

for move in movements:
    if move == '<':
        x-=1
    elif move == '>':
        x+=1
    elif move == 'V':
        y+=1
        if y > max_y:
            max_y = y
    
    grid[(x,y)] = draw_char

    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x

for row in range(max_y + 1):
    line = ''
    for col in range(min_x, max_x + 1):
        if(col,row) in grid:
            line+=draw_char
        else:
            line+= ' '
    print(line)