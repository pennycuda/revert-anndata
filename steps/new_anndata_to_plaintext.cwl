#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: DockerRequirement
    dockerImageId: pcuda/new_anndata_to_plaintext

inputs:
    raw_file:
        type: File
        inputBinding:
            position: 0
    secondary_analysis_file:
        type: File
        inputBinding:
            position: 1

outputs:
    raw_mtx_file:
        type: File
        outputBinding:
            glob: raw_mtx.mtx
    raw_var_file:
        type: File
        outputBinding:
            glob: raw_var.csv
    raw_obs_file:
        type: File
        outputBinding:
            glob: raw_obs.csv
    sa_mtx_file:
        type: File
        outputBinding:
            glob: sa_mtx.mtx
    sa_var_file:
        type: File
        outputBinding:
            glob: sa_var.csv
    sa_obs_file:
        type: File
        outputBinding:
            glob: sa_var.csv

baseCommand: ['python', '/opt/new_anndata_to_plaintext.py']