from django.apps import AppConfig
import boto3


class AppToUploadConfig(AppConfig):
    name = 'app_to_upload'


class BasicUpload(object):

    def upload_media_file_2(self, f1, key1, bucket_name):
        content = open(f1, 'rb')
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket=bucket_name,
            Key=key1,
            Body=content
        )


upload = BasicUpload()
files = ['1.mp4', '2.mp4', '3.mp4', '4.mp4', '5.mp4', '6.mp4']
for item in files:
    upload.upload_media_file_2(item, item)
