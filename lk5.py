class InconsistentDataError(Exception):
    def __str__(self):
        print('Введи одинаковое кол-во катетов')


class NonNumericError(Exception):
    def __str__(self):
        print('Введи цифры')


variant = input("Выберите вариант реализации (1/2):")
if not variant.replace(" ", "").isdigit():
    raise NonNumericError()

if int(variant) == 1:
    string = input('Введите первую группу катетов: ')
    if not string.replace(" ", "").isdigit():
        raise NonNumericError()
    k1 = string.split()

    string = input('Введите вторую группу катетов: ')
    if not string.replace(" ", "").isdigit():
        raise NonNumericError()
    k2 = string.split()

elif int(variant) == 2:
    string = input('Введите катеты: ')
    if not string.replace(" ", "").isdigit():
        raise NonNumericError()
    k1, k2 = [], []
    for num, val in enumerate(string.split(), start=0):
        if num % 2 == 0:
            k1.append(val)
        else:
            k2.append(val)

else:
    print("Я такой вариант не давал...")
    exit(0)

if len(k1) != len(k2):
    raise InconsistentDataError()

for num, val in enumerate(k1, start=0):
    hypotenuse = (int(k1[num]) ** 2 + int(k2[num]) ** 2) ** (1 / 2)
    square = (int(k1[num]) * int(k2[num]) / 2)
    print(f'Треугольник {num + 1} с катетами {k1[num]} и {k2[num]} имеет площадь {square} и гипотенузу {hypotenuse}')










from collections import Counter
persons = [
 {
     "name" : "Anna",
     "age" : 25,
     "gender" : "female"  
 }, {
      "name" : "Lena",
     "age" : 12,
     "gender" : "female" 
 },{
      "name" : "Nastya",
     "age" : 33,
     "gender" : "female" 
 },{
      "name" : "Angelina",
     "age" : 30,
     "gender" : "female" 
 },{
      "name" : "Anna",
     "age" : 22,
     "gender" : "female" 
 },{
      "name" : "Anna",
     "age" : 40,
     "gender" : "female" 
 },{
      "name" : "Ira",
     "age" : 11,
     "gender" : "female" 
 },{
      "name" : "Polina",
     "age" : 17,
     "gender" : "female" 
 },{
      "name" : "Oksana",
     "age" : 18,
     "gender" : "female" 
 },{
      "name" : "Anna",
     "age" : 8,
     "gender" : "female" 
 }, {
     "name" : "Yana",
     "age" : 43,
     "gender" : "female"  
 }, {
      "name" : "Kira",
     "age" : 18,
     "gender" : "female" 
 },{
      "name" : "Nastya",
     "age" : 25,
     "gender" : "female" 
 },{
      "name" : "Tomara",
     "age" : 31,
     "gender" : "female" 
 },{
      "name" : "Rita",
     "age" : 39,
     "gender" : "female" 
 },{
      "name" : "Sveta",
     "age" : 25,
     "gender" : "female" 
 },{
      "name" : "Nastya",
     "age" : 28,
     "gender" : "female" 
 },{
      "name" : "Lera",
     "age" : 19,
     "gender" : "female" 
 },{
      "name" : "Sara",
     "age" : 10,
     "gender" : "female" 
 },{
      "name" : "Anton",
     "age" : 25,
     "gender" : "male" 
 }, {
     "name" : "Dima",
     "age" : 33,
     "gender" : "male"  
 }, {
      "name" : "Fedor",
     "age" : 38,
     "gender" : "male" 
 },{
      "name" : "Nikita",
     "age" : 32,
     "gender" : "male" 
 },{
      "name" : "Alex",
     "age" : 25,
     "gender" : "male" 
 },{
      "name" : "Foma",
     "age" : 7,
     "gender" : "male" 
 },{
      "name" : "Evgeniy",
     "age" : 25,
     "gender" : "male" 
 },{
      "name" : "Alex",
     "age" : 12,
     "gender" : "male" 
 },{
      "name" : "Kiril",
     "age" : 27,
     "gender" : "male" 
 },{
      "name" : "Mihail",
     "age" : 30,
     "gender" : "male" 
 },{
      "name" : "Danil",
     "age" : 60,
     "gender" : "male" 
 }
]

print(len(persons))

ge = [ge["gender"] for ge in persons]
м = ge.count('male')
ж =  ge.count('female')
print(f'Количество мужчин: {м}, и количество девушек: {ж}')

ages = [ge['age'] for ge in persons]
ag = ([ag for ag in ages if ag > 17])
ag = len(ag)
print(f'Количество совершеннолетних людей в журнале: {ag}')

#Выводит список имен в журнале
names = [print(gn['name']) for gn in persons]

#Выводит множество возрастов
ages = [ge['age'] for ge in persons]
no_repeat = set(ages)
print(no_repeat)

#Выводит 3 наиболее встречающихся имени в журнале
namess = Counter([gn['name'] for gn in persons])
print(namess.most_common(3))

for i in persons:
    if i['age'] > 34:
        if i['name'][0] == "F":
            if i['gender'] == 'male':
                print(i['name'])