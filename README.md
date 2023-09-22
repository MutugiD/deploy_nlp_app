# DEPLOY-NPL-MODEL
Basic ML project converted to MLOPs steps for deploying to AWS Lambda using Docker.

## Data Science Process
Basically went on Kaggle, and downloaded one with sufficient data. Then copy and pasted old code. 

## How do I build the model?
Running on Ubuntu 20.04  
Make sure you have [conda](https://docs.conda.io/en/latest/miniconda.html) installed.  
Create env `conda create -n nlp_app` and then activate `conda activate nlp_app`.  
Then, install the requirements with `bash install_requirements.sh`.

Finally, you can build the model by running `python build_model.py` on the terminal.

## How do I test the app?

`RUNNING_LOCAL=True python -m app.main`
or
`RUNNING_LOCAL=True FILENAME=model-dev/data/emotion-labels-test.csv python -m app.main`
where `FILENAME` is any file with `text` in the header.

## Directory structure

    deploy-python-ml/
    ├── app
    │   ├── model
    │   ├── preprocessing
    └── model-dev
        └── data

## Deployment

General steps to deploy your code include

1.  Build your machine learning model and pipeline
2.  Create/setup a AWS account
3.  Package your code in a Docker container
4.  Upload your Docker image to AWS Elastic Container Registry (ECR)
5.  Create your AWS Lambda to run the ECR image
6.  Run/test/configure your AWS Lambda
7.  Deliver your results to others who may need the results


![Deployment Process](images/diagram2.png)