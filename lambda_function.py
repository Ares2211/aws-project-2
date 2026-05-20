import json

def lambda_handler(event, context):

    print("CI/CD Deployment Successful")
    print(json.dumps(event, indent=2))

    return {
        'statusCode': 200,
        'body': 'S3 trigger processed successfully'
    }
