import copy

grid = [['.','.','.','.','.','.'],
        ['.','o','o','.','.','.'],
        ['o','o','o','o','.','.'],
        ['o','o','o','o','o','.'],
        ['.','o','o','o','o','o'],
        ['o','o','o','o','o','.'],
        ['o','o','o','o','.','.'],
        ['.','o','o','.','.','.'],
        ['.','.','.','.','.','.']]

def picture_grid(grid):
    matrix = copy.deepcopy(grid)
    row = 0
    for row in range(0, len(matrix[0])):
        my_string = ' '
        for col in range(0, len(matrix)):
            my_string = my_string +  matrix[col][row]
        print(my_string)

picture_grid(grid)
