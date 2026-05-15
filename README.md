# downscaling_transferability_with_geographic_features

## Setup
Set up conda environment from provided `environment.yml`: `conda env create -f environment.yml`.
Install python dependencies using `pip install -r requirements.txt`.

## RainShift
Rainshift dataset source: https://huggingface.co/datasets/RainShift/rainshift
Each region data is stored as `[region_name]/train_data_in.zarr/` and `[region_name]/train_data_out.zarr/` directories plus a `static_variables.nc` file.

Benchmark from original paper. with model implementations and a mini NA west dataset found at https://github.com/RolnickLab/downscaling-transferability.
## Usage
Directories:
* downscaling-transfer
* `satclip/`: clone of https://github.com/microsoft/satclip
* `outputs/`: directory that plots and results are saved to
* `rainshift_aef_cache/`, `rainshift_aef_features/`, `rainshift_satclip_features/`: cache of geospatial features to save compute time

Scripts:
* `rainshift_download_select.py`: download Rainshift data from Huggingface repo for selected regions and splits to a `data/` directly.

Notebooks:
* `inspect_rainshift_data.ipynb`: explore RainShift data structure and extract and save region bounds
* `explore_alphaearth.ipynb`, `explore_satclip.ipynb`: show how to query/retrieve the respective embeddings, visualize embeddings over global landmass via RGB color coding of top-3 PCA components, and perform t-SNE/UMAP embedding clustering visualizations of coordinates in all 18 RainShift regions
* `embedding_predictive_strength.ipynb`: explore how well a linear regression model and an MLP can learn the mapping f(embedding) = precipitation for a region using SatCLIP and AlphaEarth embeddings and measure how much better it is over baseline bilinear interpolation from ERA5 data
* `embedding_zero_shot_transfer.ipynb`: analyze how well models (regression, MLP) trained to learn mapping f(embedding) = precipitation for a single RainShift region can transfer zero-shot to other RainShift regions
* `rainshift_predictions.ipynb`: try to train simple SR model on RainShift data. WIP, model is not currently working/learning

### old TODOs:
* [x] what is the `static_variables.nc` file and how do I read it and what data is in it? 
* [x] What are in and out files?
    * in: low-res input data (era5)
    * out: high-res precipitation (target variable)
* [x] understand RainShift dataset format: each region has data as `xarray.core.dataset.Dataset` form.
    * [x] for a xarr.Dataset, get the lat/lon range: see notebook for example
    * [x] extract the coordindate bounds of all the rainshift regions 
        * solution: download the smallest data split for each region (test_data_out) (`rainshift_download_select.py`) and then extract bounds (`inspect_rainshift_data.ipynb`)
        * results: saved as `rainshift_regions_info.csv`
        * [ ] add column label for each region as test or train
        * [x] shift lon range to be [-180, 180] for all regions (right now some go up to 360)

* [x] set up satclip - can query a simple 
* [x] set up alpha earth embeddings

* [x] determine the resolution to sample points at: sample embeddings at input res (0.25 degree) or target res (0.1 degree)? --> target res

* [x] identify some regions with similar physical drivers for precipitation for comparison

* [x] t-sne and umap
    * [x] satclip
    * [x] alphaearth
    

