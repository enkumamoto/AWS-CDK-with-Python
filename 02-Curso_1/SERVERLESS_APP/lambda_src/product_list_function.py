import json
import os
import logging
import boto3 # AWS Python SDK

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the DynamoDB client
dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    '''
    Returns all products from the DynamoDB table provided.

    Environment variables:
        - TABLE_NAME: The name of the DynamoDB table scanned.
    '''

    logger.info(f"Received event: {json.dumps(event, indent=2)}")

    # Scan the DynamoDB table to get all products
    products = dynamodb_client.scan(
        TableName=os.environ['TABLE_NAME']
    )

    return {
        "statusCode": 200,
        "body": json.dumps(products['Items'])
    }