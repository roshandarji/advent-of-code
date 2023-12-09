from icecream import ic

def read_file_to_matrix(filename: str) -> list:
    with open(filename, 'r') as f:
        matrix = [list(line.strip()) for line in f.readlines()]

    strings = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '.':
                string = ''
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni = i + dx
                        nj = j + dy
                        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj].isalpha():
                            string += matrix[ni][nj]
                if string:
                    strings.append(string)

    return matrix, strings

ic(read_file_to_matrix('day-3/d3p1-example.txt'))