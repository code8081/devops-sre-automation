import boto3

# AWS Region
region = "ap-south-1"

# List of existing SNS topic ARNs to remove encryption
sns_topic_arns = [
# TopicARN
      "arn:aws:sns:ap-south-1:538360184485:testsnsforprod",
      "arn:aws:sns:ap-south-1:538360184485:testsnsforprod2"
                    ]

# Initialize SNS client
sns_client = boto3.client("sns", region_name=region)

def disable_encryption(topic_arn):
    try:
    # Remove SNS encryption by setting KmsMasterKeyId to an empty string
        sns_client.set_topic_attributes(
            TopicArn=topic_arn,
            AttributeName='KmsMasterKeyId',
            AttributeValue=''  # Empty value disables encryption
            )
        print(f"Encryption removed for topic: {topic_arn}")
    except Exception as e:
        print(f"Failed to remove encryption for topic: {topic_arn}. Error: {str(e)}")

         # Loop through each topic and remove encryption
for topic_arn in sns_topic_arns:
    disable_encryption(topic_arn)

