from argparse import ArgumentParser
from pathlib import Path

import anndata
import pandas as pd
import numpy as np
import scipy.io


def convert_raw(raw_file: Path):
    adata = anndata.read_h5ad(str(raw_file))
    # get the matrix
    mtx = adata.X
    mtx_path = Path('raw_mtx.mtx')
    scipy.io.mmwrite(mtx_path, mtx)
    # get the obs
    obs_data = adata.obs
    obs_path = Path('raw_obs.csv')
    obs_data.to_csv(obs_path)
    # get the var
    var_data = adata.var
    var_path = Path('raw_var.csv')
    var_data.to_csv(var_path)


def convert_sa(sa_file: Path):
    adata = anndata.read_h5ad(str(sa_file))
    # get the matrix
    mtx = adata.X
    mtx_path = Path('sa_mtx.mtx')
    scipy.io.mmwrite(mtx_path, mtx)
    # get the obs
    obs_data = adata.obs
    obs_path = Path('sa_obs.csv')
    obs_data.to_csv(obs_path)
    # get the var
    var_data = adata.var
    var_path = Path('sa_var.csv')
    var_data.to_csv(var_path)


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('raw_file', type=Path)
    p.add_argument('secondary_analysis_file', type=Path)
    args = p.parse_args()

    convert_raw(args.raw_file)
    convert_sa(args.secondary_analysis_file)