# downscaling_transferability_with_geographic_features

`conda activate downscaling` (python 3.11)

SatCLIP setup requirements (see SatCLIP Hugging Face Usage notebook):
```
pip install lightning --quiet
pip install rasterio --quiet
pip install torchgeo --quiet
pip install albumentations
```


rainshift dataset requirements:
`xarray`, `zarr` for using the dataset
dataset is stored as `[region_name]/train_data_in.zarr/` and `[region_name]/train_data_out.zarr/` directories plus a `static_variables.nc` file, 


TODO:
* [ ] what is the `static_variables.nc` file and how do I read it and what data is in it? 
* [ ] What are in and out files?
    * in: low-res input data (era5)
    * out: high-res precipitation (target variable)
* [ ] understand RainShift dataset format: each region has data as `xarray.core.dataset.Dataset` form.
    * [x] for a xarr.Dataset, get the lat/lon range: see notebook for example
    * don't think i have room to download the entire dataset so how do i get all the bounds...?? one at a time??
    * [x] extract the coordindate bounds of all the rainshift regions 
        * solution: download the smallest data split for each region (test_data_out) (`rainshift_download_select.py`) and then extract bounds (`inspect_rainshift_data.ipynb`)
        * results: saved as `rainshift_regions_info.csv`

[x] set up satclip - can query a simple 
[ ] set up alpha earth embeddings

[ ] determine the resolution to sample points at: sample embeddings at input or target res?

[ ] identify some regions with similar physical drivers for precipitation for comparison