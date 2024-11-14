# End-to-End-Brain-Cancer-Classification-using-MLflow-DVC


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Akhilpm156/Brain-Cancer-Classification-using-MLflow-DVC.mlflow\
MLFLOW_TRACKING_USERNAME="" \
MLFLOW_TRACKING_PASSWORD="" \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Akhilpm156/Brain-Cancer-Classification-using-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME="Akhilpm156"

export MLFLOW_TRACKING_PASSWORD=""

```

### DVC cmd

```bash

dvc init

dvc repro

dvc dag

```