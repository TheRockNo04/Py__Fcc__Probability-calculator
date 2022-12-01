import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for ball_color,ball_count in kwargs.items():
            self.contents.extend(ball_color for _ in range(ball_count))
        self.contents_copy = self.contents
    

    def draw(self, num_balls_drawn):
        draw = []
        self.contents = copy.copy(self.contents_copy)
        if len(self.contents) < num_balls_drawn:
            return self.contents
        for _ in range(num_balls_drawn):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            draw.append(ball)
        return draw




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    for color, count in expected_balls.items():
        expected_balls_list.extend(color for _ in range(count))

    m=0
    draw = []
    expected_balls_list_copy = []

    for _ in range(num_experiments):
        draw = hat.draw(num_balls_drawn)
        expected_balls_list_copy = copy.copy(expected_balls_list)
        for i in draw:
            if i in expected_balls_list_copy:
                expected_balls_list_copy.remove(i)
        if len(expected_balls_list_copy) < 1:
            m+=1
    
    probability = m/num_experiments
    return probability