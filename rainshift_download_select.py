import os
import zipfile

from huggingface_hub import hf_hub_download


# Dataset configuration
REPO_ID = "RainShift/rainshift"
REGIONS = [
    # "africa-south",
    # "amazon-basin",
    # "arabian-peninsula",
    # "australasia-east",
    "blacksea",
    # "cape-horn",
    # "caribbean",
    # "east-asia-north-east",
    # "east-asia-south",
    "europe_west",
    # "horn-of-africa",
    # "melanesia",
    # "northamerica-east",
    # "northamerica-west",
    # "southamerica-east",
    # "southeastasia-west",
    # "tibetan-plateau",
    # "west-africa"
]

SPLITS = ["train_data_in", "train_data_out", "test_data_in", "test_data_out"]
SPLIT = "test_data_in" # "test_data_out" # smallest split for now

if __name__ == "__main__":
    # download
    for region in REGIONS:
        filename = f"{region}/{SPLIT}.zarr.zip"
        if not os.path.exists(f"data/rainshift_dataset/{filename}"):
            # download zip file from Hugging Face Hub
            hf_hub_download(
                repo_id=REPO_ID, 
                repo_type="dataset", 
                filename=filename, 
                local_dir=f"data/rainshift_dataset/"
            )
        if not os.path.exists(f"data/rainshift_dataset/{region}/{SPLIT}.zarr"):
            # unzip the downloaded file to folder
            unzip_path = f"data/rainshift_dataset/{filename}"
            print(f"Unzipping {unzip_path}...")
            with zipfile.ZipFile(unzip_path, 'r') as zip_ref:
                zip_ref.extractall(f"data/rainshift_dataset/{region}/")
        
    # clean up zip files
    for region in REGIONS:
        zip_path = f"data/rainshift_dataset/{region}/{SPLIT}.zarr.zip"
        if os.path.exists(zip_path):
            os.remove(zip_path)
        