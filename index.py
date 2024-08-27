import boto3
from botocore.exceptions import ClientError

# Initialize a session using Boto3
dynamodb = boto3.resource('dynamodb', region_name='your-region')

try:
    # Create the DynamoDB table
    table = dynamodb.create_table(
        TableName='YourTableName',
        KeySchema=[
            {
                'AttributeName': 'PrimaryKey',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PrimaryKey',
                'AttributeType': 'S'  # 'S' is for String type
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists
    table.meta.client.get_waiter('table_exists').wait(TableName='YourTableName')

    print("Table created successfully!")

except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceInUseException':
        print("Table already exists.")
    else:
        print(f"Unexpected error occurred: {e}")

try:
    # Insert an item into the table
    table = dynamodb.Table('YourTableName')

    response = table.put_item(
       Item={
            'PrimaryKey': '001',
            'Attribute1': 'Value1',
            'Attribute2': 'Value2'
        }
    )

    print("Item inserted:", response)

except ClientError as e:
    print(f"Could not insert item: {e}")

try:
    # Read an item from the table
    response = table.get_item(
        Key={
            'PrimaryKey': '001'
        }
    )

    item = response.get('Item')

    if item:
        print("Item read:", item)
    else:
        print("Item not found.")

except ClientError as e:
    print(f"Could not read item: {e}")

try:
    # Update an existing item
    response = table.update_item(
        Key={
            'PrimaryKey': '001'
        },
        UpdateExpression="set Attribute1=:val",
        ExpressionAttributeValues={
            ':val': 'UpdatedValue'
        },
        ReturnValues="UPDATED_NEW"
    )

    print("Item updated:", response)

except ClientError as e:
    print(f"Could not update item: {e}")

try:
    # Delete an item from the table
    response = table.delete_item(
        Key={
            'PrimaryKey': '001'
        }
    )

    print("Item deleted:", response)

except ClientError as e:
    print(f"Could not delete item: {e}")
