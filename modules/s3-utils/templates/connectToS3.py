from boto.s3.connection import S3Connection

def getS3Bucket():
        conn = S3Connection('<%=@access-key%>','<%=@secret-access-key%>')
        bucket = conn.get_bucket('<%=@bucket%>')
        return bucket

