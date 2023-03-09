import dask.array as da
import time


def matrix_multiplication(chunk_size):
    start_time = time.time()
    x = da.random.random((1000, 1000), chunks=chunk_size)
    y = da.random.random((1000, 1000), chunks=chunk_size)
    matrix_product = da.dot(x, y)
    print("Size of matrix:", matrix_product.shape)
    print("Chunk Size:",chunk_size,"Computation time:", time.time()-start_time)


def dask_array_save_to_HDF5(chunk_size):
    start_time = time.time()
    x = da.random.random(100000000)

    da.to_hdf5("test.hdf5", "/X", x, chunks=chunk_size)

    print("Chunk Size:",chunk_size,"Computation time:", time.time()-start_time)


if __name__ == "__main__":
    chunk_sizes = [(100, 10), (100, 100), (100, 1000)]
    for i in chunk_sizes:
        matrix_multiplication(i)
    for i in chunk_sizes:
        dask_array_save_to_HDF5(i)
