client = boto3.client('s3',aws_access_key_id='key',aws_secret_access_key='secret')
result = client.get_object(Bucket='bucket', Key='file')
with h5py.File(result['Body'], 'r') as f:
    data = f

print data.shape