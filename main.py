def sandwiches(size, *ingredients):
    print(f'\nMaking a {size} - inch sandwich with the '
          f'following ingredients: ')

    for ingredient in ingredients:
        print(f' - {ingredient}')


sandwich_one = sandwiches(12, 'steak', 'cheese', 'green peppers')
sandwich_two = sandwiches(12, 'steak', 'eggs')
sandwich_three = sandwiches(6, 'steak')
