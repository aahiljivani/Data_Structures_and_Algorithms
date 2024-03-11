class ELLMatrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.cols = len(matrix[0])
        self.positions, self.values = self.compress(matrix)

    def compress(self, matrix):
        max_non_zeros = max(sum(1 for item in row if item != 0) for row in matrix)
        positions = [[-1] * max_non_zeros for _ in matrix]
        values = [[0] * max_non_zeros for _ in matrix]

        for row_idx, row in enumerate(matrix):
            non_zero_count = 0
            for col_idx, value in enumerate(row):
                if value != 0:
                    positions[row_idx][non_zero_count] = col_idx
                    values[row_idx][non_zero_count] = value
                    non_zero_count += 1

        return positions, values

    def reconstruct(self):
        rows = len(self.values)
        reconstructed_matrix = [[0 for _ in range(self.cols)] for _ in range(rows)]
        for row_idx, (row_positions, row_values) in enumerate(zip(self.positions, self.values)):
            for pos, val in zip(row_positions, row_values):
                if pos != -1:  # Check if the position is valid
                    reconstructed_matrix[row_idx][pos] = val
        return reconstructed_matrix
