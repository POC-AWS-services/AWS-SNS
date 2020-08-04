__Author__ = 'Prameet Bisht'
__Version__ = "0.0.1"
__Email__ = "myprameet09@gmail.com"
__Github__ = "https://github.com/orgs/POC-AWS-services/dashboard"

import boto3

# Setting up the client

sns = boto3.client("sns",
                   region_name="us-east-1",
                   aws_access_key_id=AWS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET)

# TOPIC (Function): listing, creating & deleting (**Args)

# Create topic
response = sns.create_topic(Name="topic_name")
topic_arn = response["TopicArn"]

# List topics
response = sns.list_topics()
topics = response["Topics"]

# Delete topics
sns.delete_topic(TopicArn=topic_arn)

# SUBSCRIPTION: listing, creating & deleting

# Create SMS subscription
response = sns.subscribe(TopicArn=topic_arn, Protocol="SMS", Endpoint="+48123456789")
subscription_arn = response["SubscriptionArn"]

# Create email subscription
response = sns.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint="user@server.com")
subscription_arn = response["SubscriptionArn"]

# List all subscriptions
response = sns.list_subscriptions()
subscriptions = response["Subscriptions"]

# List subscriptions by topic
response = sns.list_subscriptions_by_topic(TopicArn=topic_arn)
subscriptions = response["Subscriptions"]

# Delete subscription
sns.unsubscribe(SubscriptionArn=subscription_arn)

# Delete multiple subscriptions (here: all SMS ones)
for sub in subscriptions:
    if sub["Protocol"] == "sms":
        sns.unsubscribe(sub["SubscriptionArn"])

# Publishing to topics
# Publish to topic
sns.publish(TopicArn=topic_arn,
            Message="message text",
            Subject="subject used in emails only")

# Send a single SMS (no topic, no subscription needed)
sns.publish(PhoneNumber="+1234567890",
            Message="message text")
