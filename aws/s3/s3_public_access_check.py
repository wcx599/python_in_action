import boto3
import botocore

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def check_public():
    for bucket in s3_resource.buckets.all():
        try:
            response = s3_client.get_public_access_block(Bucket=bucket.name)
            print("\t '{}' blocks public access is {}". \
                  format(bucket.name, response['PublicAccessBlockConfiguration']['BlockPublicAcls']))

        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
                print("\t '{}' has no Public Access".format(bucket.name))
            else:
                print("unexpected error: %s" % (e.response))

check_public()