import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("0 이하의 값은 입력할 수 없습니다.")

myline.set_length(20, 30)
width, height = myline.get_length()
try:
    triangle = figure.area_right_triangle(width, height)
    print(triangle)
except ValueError:
    print("0 이하의 값은 입력할 수 없습니다.")

myline.set_length(30, 40)
width, height = myline.get_length()
try:
    eclipse = figure.area_eclipse(width, height)
    print(eclipse)
except ValueError:
    print("0 이하의 값은 입력할 수 없습니다.")
