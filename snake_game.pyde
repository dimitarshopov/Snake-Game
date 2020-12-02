import config
import snake
import food
import score

def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    frameRate(8)
    
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    score.show()
    score.show_highest_score()


    
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()
        score.scr += 1
        
    if snake.is_dead():
        print('GAME OVER!')
        noLoop()
        score.save_highest_score_to_file()
        
    
def keyPressed():
    if keyCode == UP and config.CURRENT_DIR != "down":
        config.CURRENT_DIR = "up"
    
    elif keyCode == DOWN and config.CURRENT_DIR != "up":
        config.CURRENT_DIR = "down"
        
    elif keyCode == LEFT and config.CURRENT_DIR != "right":
        config.CURRENT_DIR = "left"
        
    elif keyCode == RIGHT and config.CURRENT_DIR != "left":
        config.CURRENT_DIR = "right"
        
