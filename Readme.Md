
# DynamoDB CRUD Operations with Python and Boto3

This project demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations on an Amazon DynamoDB table using Python and Boto3. The goal is to help you gain hands-on experience with DynamoDB and Boto3, the AWS SDK for Python.

## Prerequisites

Before you begin, make sure you have the following:

- **Python 3.x** installed.
- **Boto3** installed. You can install it using `pip install boto3`.
- **AWS CLI** configured with your AWS credentials. Use `aws configure` to set up your credentials.
- An active **AWS account**.

## Project Structure

- `create_table.py`: Script to create a DynamoDB table.
- `crud_operations.py`: Script to perform Create, Read, Update, and Delete operations.
- `README.md`: This documentation file.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YourUsername/DynamoDB-CRUD-Operations.git
   cd DynamoDB-CRUD-Operations
   ```

2. **Install Dependencies:**

   Make sure you have Boto3 installed:

   ```bash
   pip install boto3
   ```

3. **Configure AWS CLI:**

   Set up your AWS credentials and default region:

   ```bash
   aws configure
   ```

## Create a DynamoDB Table

Use the `create_table.py` script to create a DynamoDB table:

```python
import boto3

# Initialize a session using Boto3
dynamodb = boto3.resource('dynamodb', region_name='your-region')

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
            'AttributeType': 'S'
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
```

## Perform CRUD Operations

Use the `crud_operations.py` script to perform CRUD operations on your DynamoDB table:

### Create/Insert an Item

```python
import boto3

# Initialize a session using Boto3
dynamodb = boto3.resource('dynamodb', region_name='your-region')

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
```

### Read an Item

```python
# Read an item from the table
response = table.get_item(
    Key={
        'PrimaryKey': '001'
    }
)

item = response.get('Item')
print("Item read:", item)
```

### Update an Item

```python
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
```

### Delete an Item

```python
# Delete an item from the table
response = table.delete_item(
    Key={
        'PrimaryKey': '001'
    }
)

print("Item deleted:", response)
```

```

## Testing and Validation

After running the scripts, you can verify the results by checking your DynamoDB table in the AWS Management Console.

## Documentation

This project is well-documented with comments and explanations in the code. Refer to the code files for more detailed information on how each operation is performed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.



---

Happy coding!
```

This `README.md` file provides a comprehensive guide for setting up, running, and understanding the DynamoDB CRUD operations project. You can modify the placeholders like `YourTableName` and `your-region` to suit your specific project setup.