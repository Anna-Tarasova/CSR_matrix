import time
import numpy as np
from scipy.sparse import csr_matrix

np.random.seed(777)
repeat_count = 10000

def bench(matrix_x, matrix_y, repeat_count):
	start_time = time.time()
	
	for i in range(1, repeat_count):
		matrix_x.multiply(matrix_y)
	
	return time.time() - start_time
	
	
dense_row = np.random.randint(100, size=10000)
dense_col = np.random.randint(100, size=10000)
dense_data = np.random.randint(20, size=10000)
dense_matrix_x = csr_matrix((dense_data, (dense_row, dense_col)), shape=(100, 100))
dense_matrix_y = csr_matrix((dense_data, (dense_row, dense_col)), shape=(100, 100))
	
dense_time = bench(dense_matrix_x, dense_matrix_y, repeat_count)
print("dense matrix  %s seconds" % dense_time)

sparse_row = np.random.randint(20, size=20)
sparse_col = np.random.randint(20, size=20)
sparse_data = np.random.randint(20, size=20)
sparse_matrix_x = csr_matrix((sparse_data, (sparse_row, sparse_col)), shape=(100, 100))
sparse_matrix_y = csr_matrix((sparse_data, (sparse_row, sparse_col)), shape=(100, 100))

sparse_time = bench(sparse_matrix_x, sparse_matrix_y, repeat_count)
print("sparse matrix %s seconds" % sparse_time)
