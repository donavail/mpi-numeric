from mpi4py import MPI
import numpy as np

def matrix_multiply(A, B):
    return np.dot(A, B)

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        # Inisialisasi matriks A dan B dengan angka integer acak antara 0 dan 100
        rows, cols = 3, 3
        A = np.random.randint(0, 11, size=(rows, cols))
        B = np.random.randint(0, 11, size=(cols, rows))
    else:
        A, B = None, None

    A = comm.bcast(A, root=0)
    B = comm.bcast(B, root=0)

    local_result = matrix_multiply(A, B)

    if rank == 0:
        global_result = np.zeros_like(local_result)
    else:
        global_result = None

    comm.Reduce(local_result, global_result, op=MPI.SUM, root=0)

    if rank == 0:
        print("Matriks A:")
        print(A)
        print("Matriks B:")
        print(B)
        print("Hasil perkalian matriks:")
        print(global_result)
