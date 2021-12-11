from datetime import datetime
import numpy as np

class Data:
    def __init__(self):
        self.trial1_timestamps = np.array([
            datetime(2021, 11, 30, 14, 46),
            datetime(2021, 12, 1, 9, 0),
            datetime(2021, 12, 1, 14, 41),
            datetime(2021, 12, 1, 15, 2),
            datetime(2021, 12, 2, 10, 12)
        ], dtype='object')

        self.trial1_growing = np.array([
            [0, 1000],
            [1000, 1250],
            [1900, 1250],
            [1900, 1250],
            [1900, 1250]
        ])

        self.trial2_timestamps = np.array([
            datetime(2021, 11, 30, 14, 46),
            datetime(2021, 12, 1, 9, 0),
            datetime(2021, 12, 1, 14, 41),
            datetime(2021, 12, 1, 15, 2),
            datetime(2021, 12, 2, 10, 12)
        ], dtype='object')

        self.trial2_growing = np.array([
            [0, 1000],
            [820, 1375],
            [1000, 1375],
            [1180, 1375],
            [1930, 1260]
        ])

        self.trial3_timestamps = np.array([
            datetime(2021, 12, 2, 12, 35),
            datetime(2021, 12, 3, 7, 47),
            datetime(2021, 12, 3, 10, 16),
            datetime(2021, 12, 3, 13, 52)
        ], dtype='object') 

        self.trial3_growing = np.array([
            [0, 1000],
            [860, 1125],
            [860, 1125],
            [860, 1150]
        ])

        self.trial4_timestamps = np.array([
            datetime(2021, 12, 2, 12, 46),
            datetime(2021, 12, 3, 7, 47),
            datetime(2021, 12, 3, 10, 13),
            datetime(2021, 12, 3, 13, 52)
        ], dtype='object')

        self.trial4_growing = np.array([
            [0, 1000],
            [840, 1250],
            [1000, 1250],
            [1980, 1250]
        ])

        # GENERAL SLURRY #

        self.start_volumes = np.array([1000, 1000, 1000, 1000])
        self.acidity = np.array([6.0, 6.0, 6.5, 6.5])
        self.blended = np.array([True, False, True, True])

        self.trials = [self.trial1_timestamps, self.trial1_growing,
            self.trial2_timestamps, self.trial2_growing,
            self.trial3_timestamps, self.trial3_growing,
            self.trial4_timestamps, self.trial4_growing
        ]

# SAVE DATA POINTS #

if __name__ == "__main__":
    temp = Data()
    np.savez('numpy_data/general_slurry', start_volumes=temp.start_volumes,
        acidity=temp.acidity, 
        blended=temp.blended)

    np.savez('numpy_data/slurry_mass', 
        trial1_timestamps=temp.trial1_timestamps, 
        trial1_growing=temp.trial1_growing,
        trial2_timestamps=temp.trial2_timestamps,
        trial2_growing=temp.trial2_growing,
        trial3_timestamps=temp.trial3_timestamps,
        trial3_growing=temp.trial3_growing,
        trial4_timestamps=temp.trial4_timestamps,
        trial4_growing=temp.trial4_growing
    )

