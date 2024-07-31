import json
import base64
import boto3
import datetime
from decimal import Decimal


# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PurchaseAnalysis')

def convert_decimals(obj):
    if isinstance(obj, list):
        return [convert_decimals(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return str(obj)
    else:
        return obj

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the Base64 encoded data
        decoded_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        try:
            # Parse the decoded data as JSON
            payload = json.loads(decoded_data,parse_float=Decimal)
            payload = convert_decimals(payload)
            print(f"Decoded record: {payload}")
            
            # Add timestamp if not present
            if 'Timestamp' not in payload:
                payload['Timestamp'] = str(datetime.datetime.now())
            
            if payload['event_type'] == 'purchase':
                # Write data to DynamoDB
                table.update_item(
                    Key={'product_id': payload['product_id']},
                    UpdateExpression='ADD total_sales :val, purchase_count :inc',
                    ExpressionAttributeValues={':val': Decimal(payload['amount']), ':inc': 1}
                )

            
        
        except json.JSONDecodeError:
            print("Error decoding JSON")
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }
    
    return {
        'statusCode': 200,
        'body': json.dumps('Decoding and processing complete')
    }
