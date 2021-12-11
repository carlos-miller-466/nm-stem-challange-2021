import os
import numpy as np

# FUNCTIONS FOR ARRAY PRE-PROCESSING 
def replace_loop(np_array):
    new_np_array = np_array.copy()
    pos = 0
    for dp in np_array:
        dp = input(f"{dp} <- ")
        if dp == '':
            pass
        else:
            new_np[pos] = int(dp)
        pos += 1
    return new_np_array


def append_loop(np_array):
    while True:
        dp_in = input("New data point: ")
        if dp_in == 'q':
            break
            return np_array
        else:
            np_array = np.hstack([np_array, int(dp_in)])

            
def verify_data(np_array):
    print("A: Append Data\nR: Replace Data\nC: Check\n")
    print("Press any unlisted key to quit!")
    while True:
        u_in = input("CMD: ").lower()
        if u_in == 'a':
            np_array = append_loop(np_array)
        elif u_in == 'r':
            np_array = replace_loop(np_array)
        elif u_in == 'c':
            print(np_array)
        else:
            break
    
    return np_array


# FUNCTIONS FOR DATA PROCESSING
def diffs_between_times(time_array):
    differences = np.empty(time_array.shape)  # Initialize empty array for cumulative time differences
    for timestamp_index in range(time_array.shape[0]):  # Start index for length of time_array
        if timestamp_index + 1 >= time_array.shape[0]:  # If possibly out of bounds, set the difference to 0
            differences[timestamp_index] = 0
        else:
            difference = time_array[timestamp_index + 1] - time_array[timestamp_index]  # Determine difference
            difference = round((difference.seconds / 60) / 60)  # Convert the difference in seconds -> hours

            differences[timestamp_index] = difference  # Append the approx. hour(s) between timestamps to array

    return differences


def time_from_start(time_array):
    differences = np.empty(time_array.shape)
    for timestamp_index in range(time_array.shape[0]):
        difference = time_array[timestamp_index] - time_array[0]
        if difference.days > 0:
            difference = round(
                (((difference.days * 86400) + (difference.seconds)) / 60) / 60)
        else:
            difference = round((difference.seconds / 60) / 60)  # Convert the difference in seconds -> hours

        differences[timestamp_index] = difference  # Append the approx. hour(s) between timestamps to array

    return differences


def data_predict(time_differences, gas_data):
    """
    Takes diffs_between_times and known gas production in order to find all produced gas between recorded times.
    """
    predicted_data = np.zeros([round(time_differences[-1])])

    for dbt1, dbt2, gas1, gas2 in zip(*[iter(time_differences)]*2, *[iter(gas_data)]*2):  # Hack
        gas_median = (gas1 + gas2) / 2
        time_median = round((dbt1 + dbt2) / 2)

        predicted_data[time_median] = gas_median

    return predicted_data


# FUNCTIONS FOR NPZ FILES

def load_files(filenames):
    """
    Load numpy arrays from npz files. Returns a dictionary of array names
    and arrays.

    Filenames: list, tuple OF str, path
    """

    # Correct lack of file extension from input.
    temp_filenames = [
        filename + '.npz' 
        for filename in filenames 
        if '.npz' not in filename
        ]
    temp_filenames += [
        filename 
        for filename in filenames 
        if '.npz' in filename
        ]
    
    filenames = temp_filenames

    # Define empty dictionary to be filled with ARRAY NAME:ARRAY, ...
    loaded_arrays = {}

    for input_file in filenames:
        if os.access(input_file, os.F_OK): # Ensure existence of file
            npzfile = np.load(input_file) # Load contents of file

            # Loop through each array in file, storing the key and array
            for key in sorted(npzfile.files):
                loaded_arrays[key] = npzfile[key]
        else:
            print(f'Cannot access {ifile}!')

    return loaded_arrays

if __name__ == '__main__':
    x = load_files(['test1'])
    print(verify_data(x['onlyfifteen']))
