import connectToS3

try:
  bucket
except NameError:
  bucket=connectToS3.getS3Bucket()

for key in bucket.list():
    print key.name

