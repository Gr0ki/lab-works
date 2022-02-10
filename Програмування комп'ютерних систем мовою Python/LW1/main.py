def task_announcement(number: int) -> None:
    print(f'\n_______Task{number}_______')


def hello_world():
    print('Добрий день, світ!')


def print_numbers(nums: list, separator: str) -> None:
    nums = (str(number) for number in nums)
    print(separator.join(nums))


def print_tree(row_amount: int) -> None:
    row_amount *= 2
    tree = [('*'*i).center(row_amount) for i in range(row_amount) if i%2 != 0]
    print('\n'.join(tree))


def ask_for_a_list() -> list:
    return input('Enter a list of data(use space to separate elements): ').split(' ')


def print_two_dimensional_array(array: list, order='normal') -> None:
    if order == 'reverse':
        array.reverse()
    for i in range(len(array)):
        print(' '.join([str(elem) for elem in array[i]]))


task_announcement(1)
hello_world()

task_announcement(2)
print_numbers([4, 8, 15, 16, 23, 42], ' ')

task_announcement(3)
print_numbers([4, 8, 15, 16, 23, 42], '\n')

task_announcement(4)
rows = 8
print_tree(rows)

task_announcement(5)
rows = 3
data = [ask_for_a_list() for i in range(rows)]
print_two_dimensional_array(data)                  # FIFO

task_announcement(6)
rows = 3
data = [ask_for_a_list() for i in range(rows)]
print_two_dimensional_array(data, 'reverse')       # LIFO
