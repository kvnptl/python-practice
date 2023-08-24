from joblib import Parallel, delayed
import timeit

# Define a function you want to run in parallel
def compute(x):
    return x * x * x * x * x * x * x * x * x * x

# Create a list of inputs
inputs = range(1000000)

# start = timeit.default_timer()
# # Use Joblib's Parallel and delayed to run the compute function in parallel over all inputs
# results = Parallel(n_jobs=-1)(delayed(compute)(i) for i in inputs)
# stop = timeit.default_timer()
# print('Time: ', stop - start)

# 'n_jobs=-1' will use all available CPU cores
# 'results' will now contain the square of each number in 'inputs'

start = timeit.default_timer()
# Do it without parallel processing
results = []
for i in inputs:
    results.append(compute(i))
stop = timeit.default_timer()
print('Time: ', stop - start)

# 'results' will now contain the square of each number in 'inputs'