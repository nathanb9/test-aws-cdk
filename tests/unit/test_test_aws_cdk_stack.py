import aws_cdk as core
import aws_cdk.assertions as assertions

from test_aws_cdk.test_aws_cdk_stack import TestAwsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_aws_cdk/test_aws_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestAwsCdkStack(app, "test-aws-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
