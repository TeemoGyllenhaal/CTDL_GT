def is_valid_move(x, y, board):
    """Kiểm tra nước đi (x, y) có hợp lệ trên bàn cờ hay không"""
    n = len(board)
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if board[x][y] != -1:
        return False
    return True


def knight_tour(board, x, y, move_x, move_y, step):
    """Giải bài toán mã đi tuần bằng giải thuật quay lui"""
    n = len(board)
    if step == n**2:
        return True

    for i in range(n):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = step
            if knight_tour(board, next_x, next_y, move_x, move_y, step+1):
                return True
            board[next_x][next_y] = -1

    return False


def print_board(board):
    """In ra bàn cờ"""
    for row in board:
        print(row)


# Kích thước của bàn cờ
n = 8

# Khởi tạo bàn cờ
board = [[-1 for i in range(n)] for i in range(n)]

# Các nước đi có thể của quân mã
move_x = [2,1,-1,-2,-2,-1,1,2]
move_y = [-1,-2,-2,-1,1,2,2,1]

# Đặt quân mã vào ô đầu tiên
board[0][0] = 6

# Giải bài toán mã đi tuần
if knight_tour(board, 0, 0, move_x, move_y, 1):
    print_board(board)
else:
    print("Không tìm thấy giải pháp")