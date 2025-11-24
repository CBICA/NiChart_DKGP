import os
import argparse

import pickle
import pandas as pd

def main():
    # Initialize the parser
    parser = argparse.ArgumentParser(description="A script that processes two arguments.")

    # Add the arguments
    parser.add_argument("-i", type=str, help="Input CSV (DLMUSE ROI Volumes + Clinical data (AD_Status (CN, MCI, AD), ADAS-COG-13, MMSE) + Demographics (Age, Sex, PTID, Scan_Time))")
    parser.add_argument("-o", type=str, help="Output path")

    # Parse the arguments
    args = parser.parse_args()

    df_all = pd.read_csv(args.i)

    # 1. check all columns exist
    with open('references/preprocess_columns_all.pkl','rb') as f:
        all_cols = pickle.load(f)
    
    if not set(all_cols).issubset(df_all.columns):
        print("Failed to detect all necessary columns from the input CSV.")
        return
    else:
        print("All columns checked. Splitting the CSV.")

    # split & recorder csv into each files

    files = [
        'data_dl_muse_nichart_test_unnorm.csv',
        'data_dl_muse_nichart_spare_test_unnorm.csv',
        'data_dl_muse_nichart_spare_test_unnorm.csv',
        'data_dl_muse_nichart_mmse_test_unnorm.csv',
        'data_dl_muse_nichart_adas_test_unnorm.csv'
    ]

    # files_name = [s.split('.')[0] for s in files]

    for i in range(len(files)):
        print("Saved:",files[i])
        with open(f"references/columns_{files[i].split('.')[0]}.pkl", 'rb') as cp:
            columns = pickle.load(cp)
        df_all[columns].to_csv(os.path.join(args.o, files[i]), index=False)


if __name__ == "__main__":
    main()