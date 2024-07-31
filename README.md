

## Project Overview

This project demonstrates a real-time data processing pipeline using AWS services to track and aggregate web activity data.

### Architecture

- **Kinesis Data Stream**: Captures real-time web activity data.
- **AWS Lambda**: Processes the data, filters for purchase events, and calculates aggregates.
- **DynamoDB**: Stores aggregated data for quick real-time queries.

### Technologies Used

- AWS Lambda
- Amazon Kinesis Streams
- Amazon DynamoDB

### Project Setup

#### Prerequisites

- AWS Account
- AWS CLI configured
- Python 3.x
- (other prerequisites)

#### Deployment

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```
2. **Install dependencies**:
    ```sh
    pip install -r lambda_functions/requirements.txt
    ```

3. **Deploy Lambda Functions**:
    - Zip the Lambda function code:
      ```sh
      cd lambda_functions
      zip -r lambda_function.zip .
      ```
    - Upload the zip file to AWS Lambda (manual step or via CLI):
      ```sh
      aws lambda update-function-code --function-name my-lambda-function --zip-file fileb://lambda_function.zip
      ```


