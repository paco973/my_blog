AWS_ACCESS_KEY_ID="DO00Y83D3J9LXXHBR6RD"
AWS_SECRET_ACCESS_KEY="+cLYHGQGx4n2ylbBxUYQKUwR54UztyRe9HMXJTUIHh0"
AWS_STORAGE_BUCKET_NAME="akamiblog"
AWS_S3_ENDPOINT_URL = "https://ams3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
t = 'https://akamiblog.ams3.digitaloceanspaces.com'
AWS_LOCATION = 'static' #f'https://{AWS_STORAGE_BUCKET_NAME}.ams3.digitaloceanspaces.com'

# STATIC_ROOT = "my_blog.cdn.backends.StaticRootS3Boto3Storage"
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)

STATICFILES_STORAGE = "my_blog.cdn.backends.StaticRootS3Boto3Storage"


PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = "my_blog.cdn.backends.MediaRootS3Boto3Storage"

