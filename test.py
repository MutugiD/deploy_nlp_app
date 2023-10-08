import pandas as pd 
import numpy as np 
import boto3
from app.model import MLPipeline
s3 = boto3.client('s3')

from pathlib import Path
import lightgbm as lgb
import joblib
import os
import io
import datetime

running_locally = os.getenv('RUNNING_LOCAL') is not None
if running_locally:
    print("Running locally: ", running_locally)
    from pathlib import Path
    if Path.cwd().name != 'deploy_nlp_app':
        raise Exception("Please run this from within the top directory of `deploy-python-ml`")
    if os.getenv('FILENAME') is None:
        print("FILENAME was not given, reading from model-dev/data")
        

def load_s3_data(filename, bucket=None):
    if running_locally:
        print("-- Loading local data --")
        return pd.read_csv(filename)
    else:
        print("-- Loading s3 data --")
        # load test data
        key = filename
        print("Requesting object from Bucket: {} and Key: {}".format(bucket, key))
        obj = s3.get_object(Bucket=bucket, Key=key)
        print("Got object from S3")
        data = io.StringIO(obj['Body'].read().decode('utf-8')) 
        return pd.read_csv(data)
    
def handler(event, context):
    print("-- Running ML --")
    if running_locally:
        bucket=None
        key = os.getenv('FILENAME', 'deploy_nlp_app/model_dev/data/emotion-labels-test.csv')
    else:
        bucket = event['Records'][0]['s3']['bucket']['name']    
        key = event['Records'][0]['s3']['object']['key']
    df = load_s3_data(filename=key, bucket=bucket)
    
if running_locally:
        handler(None, None)