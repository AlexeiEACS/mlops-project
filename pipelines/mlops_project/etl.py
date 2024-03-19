import io
import os
import sys
import zipfile
import requests


def save_data(response, save_path):
    if response.status_code == 200:
        zip_file = io.BytesIO(response.content)

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(save_path)
            log_info("Succesfully raw data extracted")
    else:
        log_error("Cannot extract the Data")


if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..')))
    from config.logger import log_info, log_error

    path_download_zip_data = "https://archive.ics.uci.edu/static/public/851/steel+industry+energy+consumption.zip"
    path_raw_download = r"data/0_raw"

    response = requests.get(path_download_zip_data)

    save_data(response, path_raw_download)
