#!/usr/bin/env python3
import os

import aws_cdk as cdk
import constants
import os

from bucket_stack.stack import BucketStack


app = cdk.App()
BucketStack(
    app,
    constants.WORKLOAD_NAME,
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    )
)
app.synth()
