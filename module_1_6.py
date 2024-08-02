# module_1_6.py
mi_dict = {'Denis': 1970, 'Max': 1980, 'Pen':1990}
print(mi_dict)
print(mi_dict['Denis'])
# mi_dict['Denis'] = 1979 # в этом случае значение  'Denis' в mi_dict поменяется
# print(mi_dict)
print(mi_dict.get('Denis'))
print(mi_dict.get('Kamila')) # выводится None, т.к. Kamila  в справочнике нет
mi_dict.update({'Sasha': 1995,
                'Anton': 2000})
print(mi_dict)
a=(mi_dict.pop('Denis'))
print(a)
# list_ = [1,2,3] # работа со списками
# list_.pop(0)
# print(list_)
print(mi_dict)
print(mi_dict.keys()) # выводится список ключей
print(mi_dict.values()) # выводится список значений ключей
print(mi_dict.items()) # выводится список пар: ключ-значение
my_set={1,2,3,4,3,2,3, 'String', True, (1,2,3)}
print(my_set)
my_set.update({6, 7})
print(my_set)
print(my_set.discard(4))
print(my_set)
print(my_set.remove(3))
print(my_set)