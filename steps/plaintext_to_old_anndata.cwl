#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: DockerRequirement
    dockerImageId: pcuda/plaintext_to_old_anndata

inputs:
    raw_mtx_file:
        type: File
        inputBinding:
            position: 0
    raw_var_file:
        type: File
        inputBinding:
            position: 1
    raw_obs_file:
        type: File
        inputBinding:
            position: 2
    sa_mtx_file:
        type: File
        inputBinding:
            position: 3
    sa_var_file:
        type: File
        inputBinding:
            position: 4
    sa_obs_file:
        type: File
        inputBinding:
            position: 5
    raw_file:
        type: File
        inputBinding:
            position: 6
    secondary_analysis_file:
        type: File
        inputBinding:
            position: 7
outputs:
    raw_anndata_file:
        type: File
        outputBinding:
            glob: raw_anndata.h5ad
    secondary_analysis_anndata_file:
        type: File
        outputBinding:
            glob: secondary_analysis_anndata.h5ad

baseCommand: ['python', '/opt/plaintext_to_old_anndata.py']