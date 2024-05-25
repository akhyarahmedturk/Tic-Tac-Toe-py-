import random

def comp_pick(buttons, difficulty, middle):
    if difficulty == "Hard":
        if  middle:
            if buttons[4].cget("text") == " ":
                return 4
            else:
                return 0
        
        if (((buttons[0].cget("text") != " " and buttons[8].cget("text") != " ") and not (buttons[2].cget("text") != " " and buttons[6].cget("text") != " ")) or (not (buttons[0].cget("text") != " " and buttons[8].cget("text") != " ") and (buttons[2].cget("text") != " " and buttons[6].cget("text") != " "))) and buttons[4].cget("text") != " " and buttons[7].cget("text") == " " and buttons[5].cget("text") == " " and buttons[3].cget("text") == " " and buttons[1].cget("text") == " ":
            if buttons[4].cget("text") == "O":
                return 5
            elif buttons[2].cget("text") == "O" or buttons[6].cget("text") == "O":
                return 8
            elif buttons[0].cget("text") == "O" or buttons[8].cget("text") == "O":
                return 2
        
        for i in range(3):
            if buttons[i*3].cget("text") == "O" and buttons[i*3].cget("text") == buttons[i*3+1].cget("text") and buttons[i*3+2].cget("text") == " ":
                return i*3+2
            if buttons[i*3].cget("text") == "O" and buttons[i*3].cget("text") == buttons[i*3+2].cget("text") and buttons[i*3+1].cget("text") == " ":
                return i*3+1
            if buttons[i*3+1].cget("text") == "O" and buttons[i*3+1].cget("text") == buttons[i*3+2].cget("text") and buttons[i*3].cget("text") == " ":
                return i*3
        
        for i in range(3):
            if buttons[i].cget("text") == "O" and buttons[i].cget("text") == buttons[i+3].cget("text") and buttons[i+6].cget("text") == " ":
                return i+6
            if buttons[i].cget("text") == "O" and buttons[i].cget("text") == buttons[i+6].cget("text") and buttons[i+3].cget("text") == " ":
                return i+3
            if buttons[i+3].cget("text") == "O" and buttons[i+3].cget("text") == buttons[i+6].cget("text") and buttons[i].cget("text") == " ":
                return i
        
        if buttons[0].cget("text") == "O" and buttons[0].cget("text") == buttons[4].cget("text") and buttons[8].cget("text") == " ":
            return 8
        if buttons[0].cget("text") == "O" and buttons[0].cget("text") == buttons[8].cget("text") and buttons[4].cget("text") == " ":
            return 4
        if buttons[4].cget("text") == "O" and buttons[4].cget("text") == buttons[8].cget("text") and buttons[0].cget("text") == " ":
            return 0
        if buttons[2].cget("text") == "O" and buttons[2].cget("text") == buttons[4].cget("text") and buttons[6].cget("text") == " ":
            return 6
        if buttons[2].cget("text") == "O" and buttons[2].cget("text") == buttons[6].cget("text") and buttons[4].cget("text") == " ":
            return 4
        if buttons[4].cget("text") == "O" and buttons[4].cget("text") == buttons[6].cget("text") and buttons[2].cget("text") == " ":
            return 2
        
    if difficulty == "Hard" or difficulty == "Medium":
        for i in range(3):
            if buttons[i*3].cget("text") == "X" and buttons[i*3].cget("text") == buttons[i*3+1].cget("text") and buttons[i*3+2].cget("text") == " ":
                return i*3+2
            if buttons[i*3].cget("text") == "X" and buttons[i*3].cget("text") == buttons[i*3+2].cget("text") and buttons[i*3+1].cget("text") == " ":
                return i*3+1
            if buttons[i*3+1].cget("text") == "X" and buttons[i*3+1].cget("text") == buttons[i*3+2].cget("text") and buttons[i*3].cget("text") == " ":
                return i*3
        
        for i in range(3):
            if buttons[i].cget("text") == "X" and buttons[i].cget("text") == buttons[i+3].cget("text") and buttons[i+6].cget("text") == " ":
                return i+6
            if buttons[i].cget("text") == "X" and buttons[i].cget("text") == buttons[i+6].cget("text") and buttons[i+3].cget("text") == " ":
                return i+3
            if buttons[i+3].cget("text") == "X" and buttons[i+3].cget("text") == buttons[i+6].cget("text") and buttons[i].cget("text") == " ":
                return i
        
        if buttons[0].cget("text") == "X" and buttons[0].cget("text") == buttons[4].cget("text") and buttons[8].cget("text") == " ":
            return 8
        if buttons[0].cget("text") == "X" and buttons[0].cget("text") == buttons[8].cget("text") and buttons[4].cget("text") == " ":
            return 4
        if buttons[4].cget("text") == "X" and buttons[4].cget("text") == buttons[8].cget("text") and buttons[0].cget("text") == " ":
            return 0
        if buttons[2].cget("text") == "X" and buttons[2].cget("text") == buttons[4].cget("text") and buttons[6].cget("text") == " ":
            return 6
        if buttons[2].cget("text") == "X" and buttons[2].cget("text") == buttons[6].cget("text") and buttons[4].cget("text") == " ":
            return 4
        if buttons[4].cget("text") == "X" and buttons[4].cget("text") == buttons[6].cget("text") and buttons[2].cget("text") == " ":
            return 2
        
    while 1:
        x = random.randint(0, 9)
        if buttons[x].cget("text") == " ":
            return x
