import math

def get_base_score(p_degrees):
    if  -9 <= p_degrees < 9:
        return 6
    elif 9 <= p_degrees < 27:
        return 13
    elif 27 <= p_degrees < 45:
        return 4
    elif 45 <= p_degrees < 63:
        return 18
    elif 63 <= p_degrees < 81:
        return 1
    elif 81 <= p_degrees < 99:
        return 20
    elif 99 <= p_degrees < 117:
        return 5
    elif 117 <= p_degrees < 135:
        return 12
    elif 135 <= p_degrees < 153:
        return 9
    elif 153 <= p_degrees < 171:
        return 14
    elif 171 <= p_degrees < 180 or  -180 <= p_degrees < -171:
        return 11
    elif -171 <= p_degrees < -153:
        return 8
    elif -153 <= p_degrees < -135:
        return 16
    elif -135 <= p_degrees < -117:
        return 7
    elif -117 <= p_degrees < -99:
        return 19
    elif -99 <= p_degrees < -81:
        return 3
    elif -81 <= p_degrees < -63:
        return 17
    elif -63 <= p_degrees < -45:
        return 2
    elif -45 <= p_degrees < -27:
        return 15
    elif -27 <= p_degrees < -9:
        return 10

def get_multiplier(p_distance):
    if  p_distance <= 99 or 107 < p_distance <= 162:
        return 1
    elif 162 < p_distance <= 170:
        return 2
    elif 99 < p_distance <= 107:
        return 3
    else:
        return 0

print("Enter the coordinates in mm from the center of the board.")
x_cordinate = float(input("x? "))
y_cordinate = float(input("y? "))
p_distance = math.sqrt(x_cordinate**2 + y_cordinate**2)

if p_distance <= 6.35:
    score = 50
elif p_distance <= 16:
    score = 25
else:
    p_degrees = math.degrees(math.atan2(y_cordinate, x_cordinate))
    base_score = get_base_score(p_degrees)
    multiplier = get_multiplier(p_distance)
    score = base_score * multiplier

print("SCORE:", score)