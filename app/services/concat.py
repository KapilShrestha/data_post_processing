import pandas as pd
from fastapi import UploadFile
from typing import List
import logging

# Set up logger for this file
logger = logging.getLogger(__name__)


def concat_csv_files(files: List[UploadFile]) -> pd.DataFrame:
    dataframes = []

    for file in files:
        try:
            # Access filename directly from the UploadFile object
            logger.info(f"Processing file: {file.filename}")

            # Use file.file to read the content (SpooledTemporaryFile)
            df = pd.read_csv(
                file.file
            )  # This works because file.file is a file-like object
            dataframes.append(df)

            logger.info(f"Successfully processed: {file.filename}")
        except Exception as e:
            logger.error(f"Error processing file {file.filename}: {str(e)}")

    if dataframes:
        # Concatenate all dataframes into one
        combined_df = pd.concat(dataframes, ignore_index=True)
        logger.info("Concatenation successful.")
    else:
        logger.error("No valid files to concatenate.")
        combined_df = (
            pd.DataFrame()
        )  # Return an empty DataFrame if no files were processed

    return combined_df
