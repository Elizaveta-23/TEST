# Задание 1
#example_str = '***---Добро пожаловать!---***'
#result = example_str.strip('*-')
#print(result)

# Задание_2
#example_str = 'В строке, есть, ошибка, снова ошибка.'
#result = example_str.replace('ошибка', 'исправление').replace(',', '.')
#print(result)

# Задание_3
#example_str = 'Иванов;Петров;Сидоров;Кузнецов'
#result = example_str.split(';')[1]
#print(result)

# Задание_4
#words = ['Скоро', 'будет', 'контрольная']
#result = ' '.join(words) + '.'
#print(result)

# Задание_5
#nums = [4, 2, 9, 0, 4, 7]
#list.remove(nums, 4)
#list.sort(nums)
#print(nums)

# Задание_6
#numbers = [10, 20, 30, 40]
#numbers.pop()
#print(numbers)

# Задание_7
#numbers = [5, 2, 9, 1]
#list.sort(numbers)
#print(numbers)

# Задание_8
#nums = [3, 1, 3, 7, 3, 2]
#count = nums.count(3)
#print(count)

# Задание_9
#a = ('RGB', 255, 0, 128)
#mode, r, g, b = a
#print(mode, r, g, b)

# Задание_10
#nums = {'a': 1, 'b': 2}
#nums = dict(
#   a=1,
#    b=2
#)
#new_dict = {'c': 3}
#nums.update(new_dict)
#nums['a'] = nums['a'] + 5
#print('Печатаем словарь с цифрами:', nums)

# Задание_11
#person = {'имя': 'Аня', 'город': 'Тверь'}
#print(person['имя'])

# Задание_12
person = {'имя': 'Игорь'}
print(person.get('телефон', 'неизвестно'))