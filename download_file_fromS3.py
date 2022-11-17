import boto3
#from botocore.exceptions import clientError
#import os

# Create an S3 access object
boto3.setup_default_session(profile_name='Bryni profile')
s3 = boto3.client("s3")
s3.download_file(
    Bucket="pythonoct2022", Key="incomingusa_cities_new_col_hema.csv", Filename="files\\incomingusa_cities_new_col_hema.csv"
)

