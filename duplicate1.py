def rotate(matrix, M):
    for i in range(M):
        start_row, start_column = 0, 0
        end_row, end_column = len(matrix) - 1, len(matrix) - 1
        while start_row < end_row:
            rotateEdge(matrix, start_row, start_column, end_row, end_column)
            start_row += 1
            start_column += 1
            end_row -= 1
            end_column -= 1


def rotateEdge(array, start_row, start_column, end_row, end_column):
    times = end_row - start_row
    for i in range(times):
        temp = array[start_row][start_column + i]
        array[start_row][start_column + i] = array[end_row - i][start_column]
        array[end_row - i][start_column] = array[end_row][end_column - i]
        array[end_row][end_column - i] = array[start_row + i][end_column]
        array[start_row + i][end_column] = temp


if __name__ == '__main__':
    arr = []
    N = int(input())
    for i in range(N):
        arr.append(list(map(int, input().split())))
    M = int(input())
    rotate(arr, M)
    for i in range(N):
        print(' '.join(list(map(str, arr[i]))))
