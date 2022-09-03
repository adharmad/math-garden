# Find the average distance between the points in a 1x1 square
# having coordinates (0,0), (0,1), (1,0) and (1,1)
# The answer needs calculus and has been solved by Michael Penn
# here:
# https://www.youtube.com/watch?v=YJU4iy3cnK4
# Answer is:
# (2+sqrt_2)/15 + log(1+sqrt_2)/3 = 0.5214
# The current program is to just verify the same numerically assuming
# a fixed distance between points i.e. in a discrete manner

import sys, math

def get_all_points(delta):
    """
    Get a list of all the points in the square incremented by the delta
    """
    points = []
    steps = int(1.0/delta)

    xs = (x * 0.1 for x in range(0, steps))
    for x in xs:
        ys = (y * 0.1 for y in range(0, steps))
        for y in ys:
            points.append((x,y))

    return points

def main():
    delta = 0.1
    points = get_all_points(delta)
    total_distance = 0.0
    count = 0

    for i in range(len(points)-1):
        pi = points[i]
        for j in range(i+1, len(points)):
            pj = points[j]
            dy = pj[1] - pi[1]
            dx = pj[0] - pi[0]
            distance = math.sqrt(dy ** 2 + dx ** 2)
            total_distance += distance
            count += 1

    average_distance = total_distance / count
    print(average_distance)

    # With a delta of 0.1, this value converges to 0.5239264869912361

if __name__ == '__main__':
    main()
