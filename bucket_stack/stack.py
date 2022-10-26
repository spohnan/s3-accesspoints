import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import constants

from constructs import Construct
from s3_accesspoint.component import S3Accesspoint
from typing import Any


class BucketStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        id_: str,
        **kwargs: Any,
    ):
        super().__init__(scope, id_, **kwargs)

        upload_bucket = s3.Bucket(self, "UploadBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            bucket_name=cdk.PhysicalName.GENERATE_IF_NEEDED,
            encryption=s3.BucketEncryption.S3_MANAGED,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
            removal_policy=cdk.RemovalPolicy.RETAIN,
            transfer_acceleration=True,
        )

        for f in constants.DATA_FLOWS:
            S3Accesspoint(self, f["name"], flow=f, bucket_name=upload_bucket.bucket_name)
