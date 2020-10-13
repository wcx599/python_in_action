git@github.com:wcx599/python_in_action.git

cd python_in_action/aws/s3

sudo pip3 install botocore
sudo pip3 install boto3

chmod 500 s3_public_access_check.py

python3 s3_public_access_check.py