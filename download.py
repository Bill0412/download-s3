import boto3
import boto3.session
import os


class Downloader:
    def __init__(self):
        '''
        bucket_name: s3 bucket to store in
        '''
        self.client = boto3.client('s3')
        self.bucket_name = 'asrapp'
        self.session = boto3.session.Session()
        self.s3 = self.session.resource('s3')
        self.bucket = self.s3.Bucket(self.bucket_name)

    def download_dir(self, remote_directory):
        '''
        remote_directory: folder name in s3 bucket
        '''
        bucket = self.bucket
        for obj in bucket.objects.filter(Prefix=remote_directory):
            if not os.path.exists(os.path.dirname(obj.key)):
                os.makedirs(os.path.dirname(obj.key))
            bucket.download_file(obj.key, obj.key)  # save to same path

if __name__ == '__main__':
    downloader = Downloader()
    downloader.download_dir("nolan/articles")