import boto3

boto3.setup_default_session(profile_name='Bryni profile')
s3 = boto3.client("s3")

s3.upload_file(
    Filename="files\\usa_cities.csv",
    Bucket="pythonoct2022",
    Key="new_file_bryni.csv",
)