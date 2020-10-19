import os
import pandas as pd

mTurk_dir = '/Users/yonatab/data/gqa_data/mTurk'
# img_base = f"https://github.com/yonatanbitton/EvalGQAContrastSets/blob/main/images/1159289.jpg"

def main():
    csv_files = [x for x in os.listdir(mTurk_dir) if x.endswith(".csv") and 'turks_data' not in x]
    all_dataframes = [pd.read_csv(os.path.join(mTurk_dir, x)) for x in csv_files]
    all_dataframes_merged = pd.concat(all_dataframes)
    all_dataframes_merged = all_dataframes_merged.sample(frac=1)
    all_dataframes_merged['image_url'] = all_dataframes_merged['img_id'].apply(lambda x: f"https://github.com/yonatanbitton/EvalGQAContrastSets/blob/main/images/{x}.png")
    all_dataframes_merged.drop(columns=['Unnamed: 0'], inplace=True)
    all_dataframes_merged.to_csv(os.path.join(mTurk_dir, 'turks_data.csv'), index=False)
    batches_dir = os.path.join(mTurk_dir, 'batches')
    first_batch = all_dataframes_merged.iloc[0:500]
    first_batch.to_csv(os.path.join(batches_dir, 'turks_data_0_500.csv'), index=False)
    second_batch = all_dataframes_merged.iloc[500:1000]
    second_batch.to_csv(os.path.join(batches_dir, 'turks_data_500_1000.csv'), index=False)
    third_batch = all_dataframes_merged.iloc[1000:]
    third_batch.to_csv(os.path.join(batches_dir, 'turks_data_1000_end.csv'), index=False)

    print("Done")


if __name__ == '__main__':
    main()