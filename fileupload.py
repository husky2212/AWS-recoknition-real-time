import boto3
s3 = boto3.client('s3')
s3.download_file('exam-proctoring-poc', 'OBJECT_NAME', 'test.jpg')
s3 = boto3.client('s3')
with open('test.jpg', 'wb') as f:
    s3.download_fileobj('exam-proctoring-poc', 'OBJECT_NAME', f)