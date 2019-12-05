mkdir lambda-deploy
cp lambda/s3-to-es.py lambda-deploy/
cp -r lambda/.venv/lib/python3.7/site-packages/* lambda-deploy/

aws cloudformation package \
    --template aws-lambda.yml \
    --s3-bucket <YOUR_BUCKET_NAME> \
    --output-template-file aws-lambda.packaged.yml && \

rm -rf lambda-deploy && \

aws cloudformation deploy \
    --template-file aws-lambda.packaged.yml \
    --stack-name deploy-lambda \
    --tags dev=cloud \
    --parameter-overrides BucketName=<INGESTION_BUCKET_NAME> \
    --capabilities CAPABILITY_IAM