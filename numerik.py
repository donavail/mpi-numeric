from mpi4py import MPI
import numpy as np
import time

def parallel_factorial(n, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Distribute the range of numbers among processes
    local_start = (rank * n) // size + 1
    local_end = ((rank + 1) * n) // size

    # Calculate the local factorial
    local_factorial = 1
    for i in range(local_start, local_end + 1):
        local_factorial *= i

    # Gather local results to compute the final factorial
    global_factorial = comm.reduce(local_factorial, op=MPI.PROD, root=0)

    return global_factorial

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        # Master process takes user input for the number
        number = 12345
        start_time = time.time()
    else:
        number = None

    # Broadcast the number to all processes
    number = comm.bcast(number, root=0)

    # Calculate the parallel factorial
    result = parallel_factorial(number, comm)

    if rank == 0:
        end_time = time.time()
        print("The factorial of {} is: {}".format(number, result))
        elapsed_time = end_time - start_time
        print("Execution time: {:.6f} seconds".format(elapsed_time))
