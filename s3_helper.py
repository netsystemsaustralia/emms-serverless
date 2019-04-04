import boto3

class S3Helper:

    def __init__(self):
        self.resource = boto3.resource('s3')

    def uploadFile(self, file, bucket, key):
        self.resource.meta.client.upload_file(file, bucket, key)

if __name__ == '__main__':
    h = S3Helper()
    h.uploadFile('./tracker_helper.py','netsystems-emms','test.csv')