# China 1-km Gridded Windbreak and Sand Fixation Service Dataset for 2023

[中文](README.md) | **English**

2023 · China · 1 km × 1 km · GeoTIFF · kg/(m²·a)

## Overview

This windbreak and sand fixation service assessment dataset was produced by Professor Zhuowei Hu's research group at Capital Normal University under Task 3 (2023YFF1303703) of the National Key Research and Development Program of China project “Intelligent Big Data Mining Technologies for Large-Scale Ecological Quality and Ecosystem Service Assessment and the Development and Demonstration of a Gridded Key-Parameter Platform.”

The dataset provides annual windbreak and sand fixation estimates for China in 2023 on a 1-km grid. It **can be used for** national and regional analyses of the spatial distribution of windbreak and sand fixation services, integrated ecosystem service assessments, and ecological conservation and restoration research. Combined with local evidence, it can also support research on priority areas for wind erosion control, planning of sand-source management projects, ecological compensation in desert areas, and evaluation of windbreak and sand fixation measures.

## Dataset information

| Item | Description |
| --- | --- |
| Year | 2023 (one annual layer) |
| Spatial scope | National-scale China; actual valid coverage is defined by valid raster cells |
| Spatial resolution | 1000 m × 1000 m |
| Variable and unit | Annual windbreak and sand fixation per unit area, kg/(m²·a) |
| Format | GeoTIFF |
| File | `China_Windbreak_Sand_Fixation_Service_2023_1km.tif` |
| File size | 33,142,530 bytes (approximately 31.61 MiB) |
| Bands / data type | 1 / Float32 |
| Dimensions | 7491 columns × 5775 rows |
| CRS | Custom Albers Equal Area Conic projection on the WGS 84 datum; coordinates in metres |
| Projection parameters | Central meridian 105°; latitude of origin 0°; standard parallels 25° and 47°; false easting and false northing both 0 m |
| XY coordinate system | Albers_Conic_Equal_Area |
| NoData | `-9999` |
| Valid range | 0–41.16516876220703 kg/(m²·a) |
| Valid cells | 9,363,520 (excluding NoData) |
| Compression | LZW |
| Producer | Capital Normal University |
| Version | v1.0.0 |

See the [metadata file](metadata/dataset_metadata.json) and [CRS WKT](metadata/crs.wkt) for full spatial information. Explicitly exclude `-9999` when computing statistics; do not rely solely on the internal raster mask.

## Download

Download `China_Windbreak_Sand_Fixation_Service_2023_1km.tif` and `SHA256SUMS.txt` from this repository's [**Releases**](https://github.com/giserwx/ChinaWindbreakSandFixation-1km-2023/releases) page. The repository's “Download ZIP” contains documentation, metadata, figures and a reading example, but not the national GeoTIFF.

Verify file integrity with `sha256sum China_Windbreak_Sand_Fixation_Service_2023_1km.tif` (Linux/macOS) or `Get-FileHash China_Windbreak_Sand_Fixation_Service_2023_1km.tif -Algorithm SHA256` (PowerShell).

## Method

The dataset uses the Revised Wind Erosion Equation (RWEQ) to assess windbreak and sand fixation services across China for 2023 through monthly calculations and annual summation. Inputs include ERA5 reanalysis data, ground meteorological observations, soil moisture, land use and fractional vegetation cover (FVC).

1. **Wind speed optimization.** Paired historical station observations and ERA5 wind speeds are used to learn wind speed residuals with surface-related predictors, including station coordinates, terrain characteristics and land use. Corrected wind speeds are generated and spatially mapped for 2023.
2. **Soil moisture factor optimization.** Soil moisture data at multiple resolutions are integrated to represent the suppression of wind erosion by surface moisture conditions.
3. **Vegetation factor optimization.** Land use and vegetation cover data are combined to refine the representation of vegetation effects on wind erosion under different surface cover conditions.
4. **Annual dataset production.** The optimized inputs and parameters are applied to RWEQ, with monthly calculations summed to produce annual windbreak and sand fixation estimates on a 1-km grid.

![Windbreak and sand fixation dataset production workflow](figures/workflow.jpg)

## Quality assessment

The research team evaluated the dataset through comparisons of wind speed forcing schemes and Monte Carlo simulations, with the following results:

| Evaluation | Result |
| --- | --- |
| Spatial class agreement | At least 85% agreement between service assessment results driven by optimized wind speeds and those driven by observed wind speeds |
| Mean pixel-level coefficient of variation (CV) | Decreased from 0.476 to 0.357, a relative reduction of 24.94% |
| CV of regional mean service amount | Decreased from 0.308 to 0.257, a relative reduction of 16.47% |


## Spatial overview

![Spatial distribution of windbreak and sand fixation services in China at 1-km resolution in 2023](figures/windbreak-sand-fixation-2023.png)

## Reading the data

Open the GeoTIFF in compatible GIS software, or install Python's `rasterio` and `numpy` and run:

```bash
python scripts/read_geotiff.py /path/to/China_Windbreak_Sand_Fixation_Service_2023_1km.tif
```

## Related research paper

Li, S., Hu, Z., Zhu, Z., Hou, W., Wang, M., Liu, X., Zhao, L., & Wang, J. (2026). Assessment of windbreak and sand fixation services driven by land cover changes and their ecological restoration potential: A case study of the Ebinur Lake basin, Xinjiang, China. *Remote Sensing for Natural Resources*, 38(4), 106–117. [DOI: 10.6046/zrzyyg.2025209](https://doi.org/10.6046/zrzyyg.2025209).

## Data use statement

We make our data products available to the research community as we believe that the dissemination of our data will lead to advancement in science. If you plan to use our data in a manuscript or presentation, we request that you inform us at an early stage of your work. You should ensure that your research does not significantly overlap with what we are currently working on with this product. In addition, if our data are essential to your work, or if an important result or finding depends on our data, co-authorship may be appropriate. You should inform us of your analysis and publication plans well in advance of the submission of a paper, give us an opportunity to read and intellectually contribute to the manuscript, and, if appropriate, offer co-authorship. Contact: Dr. Zhuowei Hu (huzhuowei@cnu.edu.cn).

## Contacts

| Contact | Email |
| --- | --- |
| Task lead: Dr. Zhuowei Hu | [huzhuowei@cnu.edu.cn](mailto:huzhuowei@cnu.edu.cn) |
| Technical contact: Jiantong Li | [1845472692@qq.com](mailto:1845472692@qq.com) |
