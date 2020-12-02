import os
scr = 0
file_name = "highest_score.txt"

def show():
    fill(255)
    textSize(24)
    text("Score: " + str(scr), 20, 40)


def show_highest_score():
    fill(255)
    textSize(24)
    text("Highest Score: " + str(get_highest_score_from_file()), 20, 80)
    

def save_highest_score_to_file():
    current_highest_score = get_highest_score_from_file()
    
    if scr > current_highest_score:
        with open(file_name, "w") as file:
            file.write(str(scr))
    print(scr)
    print(current_highest_score)
    

    
    
def get_highest_score_from_file():
    with open(file_name, 'r') as file:
        highest_score = file.readline()
        if highest_score == "":
            highest_score = 0
        else:
         highest_score = int(highest_score)
         
        return highest_score
