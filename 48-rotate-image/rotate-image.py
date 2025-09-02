class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix)-1
        
        for i in range(ceil(len(matrix)/2)):
            for j in range(floor(len(matrix)/2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[dim - j][i]
                matrix[dim - j][i] = matrix[dim - i][dim - j]
                matrix[dim - i][dim - j] = matrix[j][dim - i]
                matrix[j][dim - i] = temp