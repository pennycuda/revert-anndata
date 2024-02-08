class: Workflow
cwlVersion: v1.0

inputs:
    raw_file:
        type: File
    secondary_analysis_file:
        type: File

outputs:
    raw_anndata_file:
        type: File
        outputSource: plaintext_to_old_anndata/raw_anndata_file
    secondary_analysis_anndata_file:
        type: File
        outputSource: plaintext_to_old_anndata/secondary_analysis_anndata_file

steps:
    new_anndata_to_plaintext:
        run: steps/new_anndata_to_plaintext.cwl
        in:
            raw_file:
                source: raw_file
            secondary_analysis_file:
                source: secondary_analysis_file
        out: [raw_mtx_file, raw_var_file, raw_obs_file, sa_mtx_file, sa_var_file, sa_obs_file]
    
    plaintext_to_old_anndata:
        run: steps/plaintext_to_old_anndata.cwl
        in:
            raw_file: 
                source: raw_file
            secondary_analysis_file:
                source: secondary_analysis_file
            raw_mtx_file:
                source: new_anndata_to_plaintext/raw_mtx_file
            raw_var_file:
                source: new_anndata_to_plaintext/raw_var_file
            raw_obs_file:
                source: new_anndata_to_plaintext/raw_obs_file
            sa_mtx_file:
                source: new_anndata_to_plaintext/sa_mtx_file
            sa_var_file:
                source: new_anndata_to_plaintext/sa_var_file
            sa_obs_file:
                source: new_anndata_to_plaintext/sa_obs_file
        out: [raw_anndata_file, secondary_analysis_anndata_file]