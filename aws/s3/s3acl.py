import boto3

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
s3 = boto3.resource('s3')

# bucket = s3.Bucket('mysite599.com')
# bucket.Acl().put(ACL='public-read')

# [{'Grantee': {'ID': 'af152757608fdf5aee625cdf1d190570b44f601073e0e1a598db5595a3dc9dcc',
#               'Type': 'CanonicalUser'}, 'Permission': 'FULL_CONTROL'},
#  {'Grantee': {'Type': 'Group', 'URI': 'http://acs.amazonaws.com/groups/global/AllUsers'},
#   'Permission': 'READ'}]

def set_bucket_public_to_private():
    all_users = 'http://acs.amazonaws.com/groups/global/AllUsers'
    bucket = s3.Bucket('mysite599.com')
    bucketacl = s3_client.get_bucket_acl(Bucket='mysite599.com')

    for item in bucketacl['Grants']:
        if item['Grantee']['Type'] == 'Group':
            if item['Grantee']['URI'] == all_users:
                print("public access found for {}".format('mysite599.com'))
                print("set back to private")
                bucket.Acl().put(ACL='private')

        print("current bucket '{}' acl setting is {}".format('mysite599.com', bucketacl['Grants']))

set_bucket_public_to_private()

