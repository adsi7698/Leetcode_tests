class DfsMethods:
    
    def graphical_dfs_0_1(self, matrix, each_row, visited, names):
        if not visited[each_row]:
            print(names[each_row], '->', end=" ")
            visited[each_row] = True
            for each_col in range(len(matrix[each_row])):
                if matrix[each_row][each_col] == 1 and each_col != each_row and (not visited[each_col]):
                    self.graphical_dfs_0_1(matrix, each_col, visited, names)


    def is_valid(self, sx, sy, matrix, visited):
        row_length = len(matrix)
        col_length = len(matrix[0])

        if sx < 0 or sy < 0 or sx >= row_length or sy >= col_length or matrix[sx][sy] == 0 or visited[sx][sy]:
            return False
        return True
    

    def dfs(self, matrix, sx, sy, visited):
        if not self.is_valid(sx, sy, matrix, visited):
            return 
        
        visited[sx][sy] = True
        self.dfs(matrix, sx-1, sy, visited)
        self.dfs(matrix, sx, sy-1, visited)
        self.dfs(matrix, sx+1, sy, visited)
        self.dfs(matrix, sx, sy+1, visited)


    def dfs_check(self, matrix, sx, sy, fx, fy):
        row_length = len(matrix)
        col_length = len(matrix[0])

        visited = [[False for _ in range(col_length)] for _ in range(row_length)]

        self.dfs(matrix, sx, sy, visited)
        if visited[fx][fy]:
            return True
        return False


if __name__ == '__main__':
    dfs = DfsMethods()
    matrix = [
                [1,1,1,0,0,0,0],
                [1,1,0,1,0,0,0],
                [1,0,1,0,1,0,0],
                [0,1,0,1,0,0,0],
                [0,0,1,0,1,1,1],
                [0,0,0,0,1,1,0],
                [0,0,0,0,1,0,1]
            ]

    visited = [False]*len(matrix)
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for each_row in range(len(matrix)):
        dfs.graphical_dfs_0_1(matrix, each_row, visited, names)

    print()


    matrix = [
                [1,1,1,1,0,0,0],
                [1,0,0,1,0,0,0],
                [1,0,0,1,1,0,0],
                [0,1,0,1,1,1,0],
                [0,0,1,0,0,1,1],
                [0,0,0,1,1,1,0],
                [0,0,0,1,1,1,1]
            ]

    sx = 0
    sy = 0
    fx = 6
    fy = 6

    print(dfs.dfs_check(matrix, sx, sy, fx, fy))
    

    