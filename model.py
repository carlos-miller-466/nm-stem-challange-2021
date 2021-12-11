import numpy as np

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

