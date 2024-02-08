FROM python:3.8

COPY docker/plaintext_to_old_anndata/requirements.txt /opt/requirements.txt
RUN python3 -m pip install -r /opt/requirements.txt 

COPY bin/plaintext_to_old_anndata.py /opt