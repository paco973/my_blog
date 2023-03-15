import os



AWS_ACCESS_KEY_ID="DO00Y83D3J9LXXHBR6RD"
AWS_SECRET_ACCESS_KEY="+cLYHGQGx4n2ylbBxUYQKUwR54UztyRe9HMXJTUIHh0"
AWS_STORAGE_BUCKET_NAME="akamiblog"
AWS_S3_ENDPOINT_URL = "https://ams3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400"
}

AWS_LOCATION = f'https://{AWS_STORAGE_BUCKET_NAME}.ams3.digitaloceanspaces.com'

DEFAULT_FILE_STORAGE = "my_blog.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "my_blog.cdn.backends.StaticRootS3Boto3Storage"

