nums = {'a': 1, 'b': 2}
nums = dict(
   a=1,
    b=2
)
new_dict = {'c': 3}
nums.update(new_dict)
nums['a'] = nums['a'] + 5
print('Печатаем словарь с цифрами:', nums)