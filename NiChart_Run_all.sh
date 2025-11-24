#!/bin/bash

INPUT_ROI_DEMOG=$1 # path to the CSV file containing concatenated ROI + clinical vars + Demographics + SPARE-AD and SPARE-BA scores
OUTPUT_PATH=$2 # designated output folder path (mounted path recommended)

# create output path if they don't exist
if [ ! -d "$OUTPUT_PATH" ]; then
  echo "Directory '$OUTPUT_PATH' does not exist. Creating it..."
  mkdir -p "$OUTPUT_PATH"
else
  echo "Directory '$OUTPUT_PATH' found."
fi

if [ ! -d "$OUTPUT_PATH/data" ]; then
echo "Directory '$OUTPUT_PATH/data' does not exist. Creating it..."
  mkdir -p $OUTPUT_PATH/data
else
  echo "Existing '$OUTPUT_PATH/data' found."
fi

if [ ! -d "$OUTPUT_PATH/output" ]; then
echo "Directory '$OUTPUT_PATH/output' does not exist. Creating it..."
  mkdir -p $OUTPUT_PATH/output
else
  echo "Existing '$OUTPUT_PATH/output' found."
fi

## STEP 1: Split the input CSV into :
### data_dl_muse_nichart_spare_test_unnorm.csv
### data_dl_muse_nichart_mmse_test_unnorm.csv
### data_dl_muse_nichart_adas_test_unnorm.csv
python preprocess_csv.py -i $INPUT_ROI_DEMOG -o "$OUTPUT_DIR/data"

# # STEP 2: Run Preprocessing
# ./run_preprocess_data.sh ${OUTPUT_PATH}/data

# # STEP 3: Run Inference
# ./run_inference.sh all ${OUTPUT_PATH}/output