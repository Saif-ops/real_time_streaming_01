import json
import boto3
import random
import pandas as pd
import awswrangler as wr
import  time
import logging

#Initialise  Logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


kinesis_client = boto3.client('kinesis',region_name='us-east-1')
s3_client = boto3.client('s3')
df = wr.s3.read_csv("s3://streaming-data-8017/Transactions/click_stream_transactions.csv")

def streaming_data(stream_name,event):
    response = kinesis_client.put_record(StreamName=stream_name,Data=json.dumps(event),PartitionKey=str(event['user_id']))
    logger.info(f"Successfully sent record to Kinesis: {response}")


def lambda_handler(event,context):

    stream_name = 'Webstreaming'
    for index,row in df.iterrows():
        event = {
            'user_id':str(row['UserID']),
            'timestamp' : row['Timestamp'],
            'event_type' : row['EventType'],
            'product_id' : row['ProductID'],
            'amount' : str(row['Amount'])
            
        }
        streaming_data(stream_name,event)
        time.sleep(1)
        
    
    