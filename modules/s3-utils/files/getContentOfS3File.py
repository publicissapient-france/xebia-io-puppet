import sys
import commands
import connectToS3

try:
  bucket
except NameError:
  bucket=connectToS3.getS3Bucket()

key = sys.argv[1]

print bucket.get_key(key).get_contents_as_string()

