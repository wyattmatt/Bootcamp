x = int(input("Input Number x: "))
y = int(input("Input Number y: "))
x_biner = ""
temp_x = x
while temp_x > 0:
    remain = temp_x % 2
    x_biner = str(remain) + x_biner
    temp_x = temp_x // 2
y_biner = ""
temp_y = y
while temp_y > 0:
    remain = temp_y % 2
    y_biner = str(remain) + y_biner
    temp_y = temp_y // 2
if len(x_biner) > len(y_biner):
    y_biner = y_biner.zfill(len(x_biner))
elif len(y_biner) > len(x_biner):
    x_biner = x_biner.zfill(len(y_biner))
result_biner = ""
for i in range(len(x_biner)):
    if x_biner[i] == "1" and y_biner[i] == "1":
        result_biner += "1"
    else:
        result_biner += "0"
result_decimal = 0
for bit in result_biner:
    result_decimal = result_decimal * 2 + int(bit)
print(f"x = {x} = [{', '.join(x_biner)}]")
print(f"y = {y} = [{', '.join(y_biner)}]")
print(f"Result AND = {result_decimal} = [{', '.join(result_biner)}]")