# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#object
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrations3.html


import boto3

s3 = boto3.resource('s3')
obj = s3.Object('mysite599.com','newobj')
obj.upload_file('./aws/s3/README.md')

# set object Acl to public-read will make the entire bucket PUBLIC
object_acl = s3.ObjectAcl('mysite599.com','newobj')

response = object_acl.put(
    ACL='private'
)



# response = object_acl.put(
#     ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
#     AccessControlPolicy={
#         'Grants': [
#             {
#                 'Grantee': {
#                     'DisplayName': 'string',
#                     'EmailAddress': 'string',
#                     'ID': 'string',
#                     'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
#                     'URI': 'string'
#                 },
#                 'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
#             },
#         ],
#         'Owner': {
#             'DisplayName': 'string',
#             'ID': 'string'
#         }
#     },
#     GrantFullControl='string',
#     GrantRead='string',
#     GrantReadACP='string',
#     GrantWrite='string',
#     GrantWriteACP='string',
#     RequestPayer='requester',
#     VersionId='string',
#     ExpectedBucketOwner='string'
# )