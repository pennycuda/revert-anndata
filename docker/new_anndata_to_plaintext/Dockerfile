FROM python:3.9

COPY docker/new_anndata_to_plaintext/requirements.txt /opt/requirements.txt
RUN python3 -m pip install -r /opt/requirements.txt 

COPY bin/new_anndata_to_plaintext.py /opt
