import os

print("Starting deployment...")

os.system("zip lambda-function.zip lambda_function.py")

os.system("aws s3 cp lambda-function.zip s3://lambda-artifacts-949670774201/")

os.system("aws cloudformation deploy --template-file template2.yaml --stack-name lambda-projectE --capabilities CAPABILITY_NAMED_IAM")

print("Deployment completed.")