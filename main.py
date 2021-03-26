import calc_bmi

weight = int(input("体重(kg):"))
height = int(input("身長(cm):"))

height = height / 100

bmi = calc_bmi.get_bmi(weight, height)

print(bmi)
print(bmi)
