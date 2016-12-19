import pandas as pd
json_file = pd.read_json("YoutubeDataTest.json", orient='DataFrame', typ='frame', dtype=True, convert_axes=True, convert_dates=True, keep_default_dates=True, numpy=False, precise_float=False, date_unit=None)
json_file.to_csv(path_or_buf="YoutubeDataTest.csv", sep=',', index=False)