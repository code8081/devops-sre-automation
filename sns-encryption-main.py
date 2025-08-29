import boto3

# AWS Region
region = "ap-south-1"

# KMS Key ARN for encryption
kms_key_arn = "arn:aws:kms:ap-south-1:538360184485:key/551cddf7-75be-44c6-829b-f95d86bfec95"

# List of existing SNS topic ARNs to encrypt
sns_topic_arns = [
#TopicARN
"arn:aws:sns:ap-south-1:538360184485:testsnsforprod",
"arn:aws:sns:ap-south-1:538360184485:testsnsforprod2"

]

# Initialize SNS client
sns_client = boto3.client("sns", region_name=region)

def enable_encryption(topic_arn, key_arn):
    try:
        # Set SNS encryption configuration using KMS key
        sns_client.set_topic_attributes(
            TopicArn=topic_arn,
            AttributeName='KmsMasterKeyId',
            AttributeValue=key_arn
        )
        print(f"Encryption enabled for topic: {topic_arn} using KMS Key: {key_arn}")
    except Exception as e:
        print(f"Failed to enable encryption for topic: {topic_arn}. Error: {str(e)}")

# Loop through each topic and enable encryption
for topic_arn in sns_topic_arns:
    enable_encryption(topic_arn, kms_key_arn)
