#Nesting Mavzusi
car0 = {
        'model':'Cobalt',
        'rang':'sariq',
        'yil':2018,
        'narh':14000,
        'km':75000,
        'korobka':'Avtomat'
        }
car1 = {
        'model':'nexia 1',
        'rang':'oq',
        'yil':2015,
        'narh':10000,
        'km':25000,
        'korobka':'mexanika'
        }
car2 = {
        'model':'matiz',
        'rang':'kuli',
        'yil':2019,
        'narh':4000,
        'km':61200,
        'korobka':'Mexanik'
        }

# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, \
#   {car['narh']}$")
#
# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, \
#   {car['narh']}$")
#
# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, \
#   {car['narh']}$")

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")

for car in [car0, car1,car2]:
        print(car)

















# print(car0["model"][0])