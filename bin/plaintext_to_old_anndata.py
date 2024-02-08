from argparse import ArgumentParser
from pathlib import Path

import anndata
import numpy as np
import pandas as pd
import scipy.io
import scipy.sparse


def convert_raw(mtx_file: Path , obs_file: Path, var_file: Path):
    mtx = scipy.io.mmread(mtx_file)
    mtx_dense = mtx.tocsr() if scipy.sparse.issparse(mtx) else mtx
    obs = pd.read_csv(obs_file)
    var = pd.read_csv(var_file)
    print("Mtx shape: ", mtx_dense.shape)
    print("Obs shape: ", obs.shape)
    print("Var shape: ", var.shape)
    # if mtx_dense.shape[0] != obs.shape[0]:
    #     mtx_dense = mtx_dense.T
    adata = anndata.AnnData(X=mtx_dense, obs=obs, var=var)
    output_path = Path('raw_anndata.h5ad')
    adata.write_h5ad(output_path)


def convert_sa(mtx_file: Path , obs_file: Path, var_file: Path):
    mtx = scipy.io.mmread(mtx_file)
    mtx_dense = mtx.tocsr() if scipy.sparse.issparse(mtx) else mtx
    obs = pd.read_csv(obs_file)
    var = pd.read_csv(var_file)
    print("Mtx shape: ", mtx_dense.shape)
    print("Obs shape: ", obs.shape)
    print("Var shape: ", var.shape)
    # if mtx_dense.shape[0] != obs.shape[0]:
    #     mtx_dense = mtx_dense.T
    adata = anndata.AnnData(X=mtx_dense, obs=obs, var=var)
    output_path = Path('secondary_analysis_anndata.h5ad')
    adata.write_h5ad(output_path)


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('raw_mtx_file', type=Path)
    p.add_argument('raw_var_file', type=Path)
    p.add_argument('raw_obs_file', type=Path)
    p.add_argument('sa_mtx_file', type=Path)
    p.add_argument('sa_var_file', type=Path)
    p.add_argument('sa_obs_file', type=Path)
    args = p.parse_args()
    print("Converting raw file")
    convert_raw(args.raw_mtx_file, args.raw_obs_file, args.raw_var_file)
    print("Converting secondary analysis file")
    convert_sa(args.sa_mtx_file, args.sa_obs_file, args.sa_var_file)
