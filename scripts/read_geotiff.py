"""Read annual windbreak and sand fixation data, excluding NoData."""
import argparse
import numpy as np
import rasterio

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("path", help="Path to the annual GeoTIFF")
args = parser.parse_args()
with rasterio.open(args.path) as ds:
    values = ds.read(1)
    valid = (ds.read_masks(1) > 0) & np.isfinite(values)
    if ds.nodata is not None:
        valid &= values != ds.nodata
    print("CRS:", ds.crs)
    print("Resolution (m):", ds.res)
    print("Dimensions (columns, rows):", ds.width, ds.height)
    print("NoData:", ds.nodata)
    print("Unit: kg/(m2*a)")
    print("Valid cells:", int(valid.sum()))
    if valid.any():
        print("Valid range:", float(values[valid].min()), float(values[valid].max()))
