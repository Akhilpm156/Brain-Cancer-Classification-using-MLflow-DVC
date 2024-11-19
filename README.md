# End-to-End-Brain-Cancer-Classification-using-MLflow-DVC

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml


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
