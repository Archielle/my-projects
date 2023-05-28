def start():
    nums = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    print(f'   |   |   \n {nums[7]} | {nums[8]} | {nums[9]} \n___|___|___')
    print(f'   |   |   \n {nums[4]} | {nums[5]} | {nums[6]} \n___|___|___')
    print(f'   |   |   \n {nums[1]} | {nums[2]} | {nums[3]} \n   |   |   ')
    print('Это нумерация ячеек, выбирайте по очереди, куда хотите вставить ваш символ.\n Игрок 1 играет за крестики, а игрок 2 - за нолики.\nУспехов!')
    input('Наведите курсор на поле, кликните и...\nPress start!!!')


def board(choice, nums, player):
    if player == 'x' and nums[choice] == ' ':
        nums[choice] = 'x'

    elif player == 'o' and nums[choice] == ' ':
        nums[choice] = 'o'

    print('\n' * 10)
    print(f'   |   |   \n {nums[7]} | {nums[8]} | {nums[9]} \n___|___|___')
    print(f'   |   |   \n {nums[4]} | {nums[5]} | {nums[6]} \n___|___|___')
    print(f'   |   |   \n {nums[1]} | {nums[2]} | {nums[3]} \n   |   |   ')


def step(nums, player):
    choice = 0
    all_choices = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9]
    choice = int(input(f'Сейчас ход игрока {player}, введите число ячейки: \n'))
    if choice in all_choices:
        if nums[choice] == ' ':
            board(choice, nums, player)
        else:
            print('Неверный выбор, попробуйте еще раз')
            step(nums, player)
    else:
        print('Неверный выбор, попробуйте еще раз')
        step(nums, player)



def players(player):
    if player == 'x':
        player = 'o'
    elif player == '':
        player = 'x'
    else:
        player = 'x'
    return player


def end(nums, run): # Проверка всех вариантов выигрыша. У каждого игрока их может быть по 8 вариантов
    if nums[1] == 'x' and nums[2] == 'x' and nums[3] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[4] == 'x' and nums[5] == 'x' and nums[3] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[7] == 'x' and nums[8] == 'x' and nums[9] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[7] == 'x' and nums[4] == 'x' and nums[1] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[8] == 'x' and nums[5] == 'x' and nums[2] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[9] == 'x' and nums[6] == 'x' and nums[3] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[9] == 'x' and nums[5] == 'x' and nums[1] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[7] == 'x' and nums[5] == 'x' and nums[3] == 'x':
        print('Крестики победили!')
        run = False
    elif nums[1] == 'o' and nums[2] == 'o' and nums[3] == 'o':
        print('Нолики победили!')
        run = False
    elif nums[4] == 'o' and nums[5] == 'o' and nums[6] == 'o':
        print('Нолики победили!')
        run = False
    elif nums[7] == 'o' and nums[8] == 'o' and nums[9] == 'o':
        print('Нолики победили!')
        run = False
    elif nums[7] == 'o' and nums[4] == 'o' and nums[1] == 'o':
        print('Нолики победили!')
        run = False
    elif nums[8] == 'o' and nums[5] == 'o' and nums[2] == 'o':
        print('Нолики победили!')
        run = False
    elif nums[9] == 'o' and nums[6] == 'o' and nums[3] == 'o':
        print('Нолики победили!')
        run = False
    elif nums[9] == 'o' and nums[5] == 'o' and nums[1] == 'o':
        print('Нолики победили!')
        run = False
    elif nums[7] == 'o' and nums[5] == 'o' and nums[3] == 'o':
        print('Нолики победили!')
        run = False
    return run


def player_input(player):
    print('\n' * 2)
    player_choice = input('За кого хотите играть? Х или О?\nP.S. Раскладка клавиатуры должна быть на английском.\n')
    if player_choice.lower() == 'x':
        player = 'x'
    elif player_choice.lower() == 'o':
        player = 'o'
    else:
        print('Неверный выбор, начните заново.')
        player = player_input(player)
    return player


def main():
    nums = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', }
    run = True
    player = ''
    start()
    player = player_input(player)

    while run:
        step(nums, player)
        player = players(player)
        run = end(nums, run)

main()
