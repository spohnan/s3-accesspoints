from re import I
import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_s3 as s3

from constructs import Construct
from typing import Any


class S3Accesspoint(Construct):
    def __init__(
        self,
        scope: Construct,
        id_: str,
        flow: Any,
        bucket_name: str,
        **kwargs: Any,
    ):
        super().__init__(scope, id_, **kwargs)

        prefix = flow["role"]
        
        access_point_policy_doc = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": ["s3:*Object"],
                    "Resource": f"arn:aws:s3:{cdk.Aws.REGION}:{cdk.Aws.ACCOUNT_ID}:accesspoint/ap-{id_}/object/{prefix}/*"
                }
            ]
        }

        default_vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)

        ap = s3.CfnAccessPoint(
            self,
            id_,
            bucket=bucket_name,
            name=f"ap-{id_}",
            policy=access_point_policy_doc,
            vpc_configuration=s3.CfnAccessPoint.VpcConfigurationProperty(
                vpc_id=default_vpc.vpc_id
            )
        )
