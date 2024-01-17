import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.hat = kwargs
    self.contents = list()
    for k, v in self.hat.items():
        i = 0
        while i < v:
            self.contents.append(k)
            i += 1


  def draw(self, num_balls_drawn):
    if num_balls_drawn > len(self.contents):
        num_balls_drawn = len(self.contents)

    balls_drawn = list()
    for _ in range(num_balls_drawn):
        rnd_i = random.randint(0, len(self.contents)-1)
        balls_drawn.append(self.contents.pop(rnd_i))

    return balls_drawn  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  count = 0 #[N] number of times the expected result occurred
  for _ in range(num_experiments):
      hat_cp = copy.deepcopy(hat)
      balls_drawn = hat_cp.draw(num_balls_drawn)
      balls_drawn_count = dict()
      for ball in balls_drawn:
          balls_drawn_count[ball] = balls_drawn_count.get(ball, 0) + 1

      # Checking the number of results that meet the expected
      check_flag = list()
      for x_ball in expected_balls:
          if expected_balls.get(x_ball, 0) <= balls_drawn_count.get(x_ball, 0):
              check_flag.append(1)
          else:
              check_flag.append(0)

      check = all(check_flag)
      if check:
          count += 1 #[N] number of times the expected result occurred
      else:
          pass

  probability = count / num_experiments

  return probability
#