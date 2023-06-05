# DEEPaaS Full Template

> TODO: Complete build status
> [![Build Status]()]()

To launch it, first install the package and prepare your environment then run
[deepaas](https://github.com/indigo-dc/DEEPaaS) from the application client:

> Use editable mode `pip install -e .` when you are testing your patch to a
> package through another project.

```bash
git clone https://github.com/.../{repostory}  # Download repository
cd {repository}  # Navigate inside repository project
pip install -e .  # Install repository project
deepaas-run --listen-ip 0.0.0.0  # You deploy using deepaas
```

Additionally you can configure the following environment variables for
customization:

API configuration environment variables:

- _DATA_PATH_ path pointing to the training datasets, default `./data/raw`.
- _MODEL_NAME_ package name used to provide API metadata, default `deepaas_full`.

Model configuration environment variables:

- _LABEL_DIMENSIONS_ dimensions the labels are hot encoded, default `10`.
- _IMAGE_SIZE_ vertical and horizontal pixels per image, default `28`.

MLflow configuration environment variables:

- _MLFLOW_TRACKING_URI_ pointing to the MLflow server to use for storing models.
- _MLFLOW_TRACKING_USERNAME_ username to use with HTTP Basic authentication on MLflow.
- _MLFLOW_TRACKING_PASSWORD_ password to use with HTTP Basic authentication on MLflow.
- _MLFLOW_EXPERIMENT_NAME_ experiment identification to store trainings on MLflow.
- _MLFLOW_EXPERIMENT_ID_ alternative to _MLFLOW_EXPERIMENT_NAME_ by on MLflow.

To configure DEEPaaS functionalities, create a copy from `deepaas.conf.sample`,
customize it and pass it to the run call as `deepaas-run --config-file deepaas.conf`.
More information about how to configure DEEPaaS can be found a the
[official documentation](https://docs.deep-hybrid-datacloud.eu/projects/deepaas/en/stable/install/configuration/index.html)

## Project structure

```
├── .env.sample               <- Sample file to configure environment from file
├── .gitignore                <- Untracked files that Git should ignore
├── .vscode                   <- Workspace configuration for vscode development
│   ├── launch.json                 <- Run and Debug configurations
│   └── settings.json               <- Settings for testing, formatting, etc.
├── Jenkinsfile               <- Describes basic Jenkins CI/CD pipeline
├── LICENSE                   <- Project and model license file
├── README.md                 <- The top-level README for using this project
├── VERSION                   <- File indicating the API/Model version
├── api                       <- Project package for DEEPaaS API
│   ├── __init__.py                 <- API init module including endpoint methods
│   ├── config.py                   <- API configuration module
│   ├── parsers.py                  <- API core for parsers and content types
│   ├── schemas.py                  <- API schemas with web arguments
│   └── utils.py                    <- API utilities module
├── data                      <- Folder including model datasets
│   └── raw                         <- Folder with raw data to generate datasets
├── deepaas.conf              <- DEEPaaS configuration file
├── deepaas.conf.sample       <- DEEPaaS configuration sample
├── deepaas_full              <- Package folder containing the model code
│   ├── README.md                   <- Model README for model users
│   ├── __init__.py                 <- Model init module with main methods
│   ├── config.py                   <- Model configuration module
│   └── utils.py                    <- Model utilities module
├── pyproject.toml            <- Makes project pip installable (pip install -e .)
├── requirements-test.txt     <- Requirements file for testing the service
├── requirements.txt          <- Requirements file for running the service
├── sync                      <- Folder with cloud data synchronization tools
│   ├── rclone.conf                 <- Configuration file for rclone utils
│   ├── rclone.conf.sample          <- Configuration sample for rclone utils
│   └── sync-folders.sh             <- Synchronization script for models and data
├── tests                     <- Folder containing tests for the API methods
│   ├── conftest.py                 <- File with global test fixtures
│   ├── datasets                    <- Folder including test datasets
│   ├── test_metadata               <- Folder with metadata fixtures and tests
│   ├── test_predictions            <- Folder with predict fixtures and tests
│   └── test_training               <- Folder with train fixtures and tests
└── tox.ini                   <- Generic virtual environment configuration file
```
