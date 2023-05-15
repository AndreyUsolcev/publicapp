def sort_list(arg): # Сортировка списка по возрастанию элементов в нем
    for i in range(len(arg)):
        for j in range(len(arg) - i - 1):
            if arg[j] > arg[j + 1]:
                arg[j], arg[j + 1] = arg[j + 1], arg[j]
    return arg


def binary_search(array, element, left, right): # поиск индекса числа, которое стоит перед вводимым числом (element)
    if array[0] >= element or element > array[-1]:  # Условия для номера позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу
        return "индекс предыдущего числа выходит за границы списка"
    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle-1  # возвращаем предыдущий индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)



input_array = list(map(int, input().split())) # Преобразование введённой последовательности в список
print(sort_list(input_array))

array = sort_list(input_array)
element = int(input()) # вводимое число для поиска индекса

print(binary_search(array, element, 0, len(array)-1))
