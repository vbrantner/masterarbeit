import csv
import os
import subprocess

import pandas as pd
from PIL import Image
from pyzbar.pyzbar import decode

from helper import delete_all_files_in_folder, get_all_files_in_folder

# video name should have following format
# <technology>_<resolution>_<fps>_<network>_<tool>
recordings = get_all_files_in_folder("./recordings")

for recording in recordings:
    # prepare new run
    delete_all_files_in_folder("./images")
    delete_all_files_in_folder("./split_images")
    print(recording["path"])
    # 1
    # run ffmpeg on video to extract frames
    subprocess.run(
        ["ffmpeg", "-i", recording["path"], "-vf",
            "fps=60", "./images/frame%06d.png"]
    )

    # 2
    # split each frame into 2 parts and safe with id_0 id_1
    for i, filename in enumerate(os.listdir("images")):
        if filename.endswith(".png"):
            subprocess.run(
                [
                    "convert",
                    "-crop",
                    "50%x100%",
                    f"images/{filename}",
                    f"./split_images/split_{i}_%d.png",
                ]
            )

    # 3
    # split each frame into 2 parts and safe with id_0 id_1
    def process_image(filename):
        if filename.endswith(".png"):
            # Assuming filename is '0.png', '1.png', etc.
            i = filename.split(".")[0]
            subprocess.run(
                [
                    "convert",
                    "-crop",
                    "50%x100%",
                    f"images/{filename}",
                    f"./split_images/split_{i}_%d.png",
                ]
            )

    # 4
    # grab each image from the split_images folder.
    timestamps_0 = []
    timestamps_1 = []
    for filename in os.listdir("split_images"):
        if filename.startswith("split_"):
            img_id, split_id = filename.split(".")[0].split("_")[
                1:
            ]  # Extract the id and split number
            with Image.open(f"split_images/{filename}") as img:
                try:
                    results = decode(img)
                    qrcodes = [
                        result.data.decode()
                        for result in results
                        if result.type == "QRCODE"
                    ]

                    if qrcodes:
                        # Determine the highest value (assuming lexicographically largest string is "highest")
                        highest_data_point = max(qrcodes)
                        print(img_id, highest_data_point)
                        if split_id == "0":
                            timestamps_0.append((img_id, highest_data_point))
                        elif split_id == "1":
                            timestamps_1.append((img_id, highest_data_point))
                except:
                    print("error")

    # save the result to timestamps_0.csv and timestamps_1.csv
    file_zero = f'./evaluation/{recording["filename"]}_0.csv'
    file_one = f'./evaluation/{recording["filename"]}_1.csv'
    with open(file_zero, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["img_id", "data_point"])
        writer.writerows(timestamps_0)

    with open(file_one, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["img_id", "data_point"])
        writer.writerows(timestamps_1)

        # Load the data from the CSV files
    df0 = pd.read_csv(file_one)
    df1 = pd.read_csv(file_zero)

    # Rename the data_point columns for clarity
    df0 = df0.rename(columns={"data_point": "data_point_0"})
    df1 = df1.rename(columns={"data_point": "data_point_1"})

    # Merge the two dataframes on the img_id column
    df = pd.merge(df0, df1, on="img_id")
    print(df)
    # Calculate the difference between the two data points
    df["difference"] = pd.to_numeric(df["data_point_0"]) - pd.to_numeric(
        df["data_point_1"]
    )

    df["difference_from_mean"] = round(
        df["difference"] - df["difference"].mean())

    df.sort_values(by="img_id", inplace=True)
    # Now df contains the data from both CSV files, plus an additional column 'difference', 'mean_difference', and 'difference_from_mean'
    df.to_csv(f'./result/{recording["filename"]}.csv', index=False)

    # move file from recordings to processed
    os.rename(recording["path"], f'./processed/{recording["filename"]}')
    print(df)
