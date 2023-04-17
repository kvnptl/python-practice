import concurrent.futures
import time
from tqdm import tqdm

def process_data(data):
    # function to process data
    time.sleep(0.1)  # simulate some processing time
    return data ** 2

# create a list of 10000 items
data = list(range(1000))

with concurrent.futures.ProcessPoolExecutor() as executor:
    # set up a process pool executor with 4 workers
    results = list(tqdm(executor.map(process_data, data), 
                        total=len(data), desc="Processing data", colour="green"))
