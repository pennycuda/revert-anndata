from argparse import ArgumentParser
from pathlib import Path


import anndata
import pandas as pd
import numpy as np
import scipy.sparse


def convert(orig_file: Path):
    adata = anndata.read_h5ad(str(orig_file))
    # get the matrix
    mtx = adata.X
    mtx_path = Path(orig_file.name).with_suffix('.mtx')
    scipy.sparse.save_npz(mtx_path, mtx)
    # get the obs
    obs_data = adata.obs
    obs_path = Path(orig_file.name).with_suffix('_obs.csv')
    obs_data.to_csv(obs_path)
    # get the var
    var_data = adata.var
    var_path = Path(orig_file.name).with_suffix('_var.csv')
    var_data.to_csv(var_path)



if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('raw_file', type=Path)
    p.add_argument('secondary_analysis_file', type=Path)
    args = p.parse_args()

    convert(args.raw_file)
    convert(args.secondary_analysis_file)