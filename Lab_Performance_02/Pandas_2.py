import pandas as pd

data_sample = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, None, 3, None, 5]
}

data_frame = pd.DataFrame(data_sample)

data_frame_filled = data_frame.fillna(data_frame.mean())

print(data_frame_filled)
