from bitstring import BitArray

folder = "Day_4"
part1_data = open(f"{folder}/Part1Data.txt").readlines()
part2_data = open(f"{folder}/Part2Data.txt").readlines()
test_data = open(f"{folder}/Test.txt").readlines()


def get_boards(input_data):
    boards = []
    current_board = []
    for i in range(1, len(input_data)):
        if (input_data[i] != '\n'):
            nums = input_data[i].strip().replace("  ", " ").split(" ")
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            current_board.append(nums)
        else:
            current_board = []
            boards.append(current_board)
    return boards


def set_val_in_board(board, value):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if (board[y][x] == value):
                board[y][x] = 0


def has_board_won(board):
    for y in range(len(board)):
        all = True
        for x in range(len(board[0])):
            if (board[y][x] != 0):
                all = False
        if (all):
            return True

    for x in range(len(board[0])):
        all = True
        for y in range(len(board)):
            if (board[y][x] != 0):
                all = False
        if (all):
            return True

    return False


def get_board_score(board):
    score = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            score += board[y][x]
    return score


def solve():
    data = part1_data
    input = data[0].split(",")
    for i in range(len(input)):
        input[i] = int(input[i])
    boards = get_boards(data)

    winning_boards = set()

    for num in input:
        for i in range(len(boards)):
            board = boards[i]
            set_val_in_board(board, num)
            if (has_board_won(board) and i not in winning_boards):
                print(get_board_score(board) * num)
                winning_boards.add(i)


solve()
