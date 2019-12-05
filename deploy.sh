aws cloudformation deploy \
    --template-file aws-es-domain.yml \
    --stack-name deploy-elasticsearch \
    --tags dev=cloud \
    --parameter-overrides DomainName=<GLOBAL_UNIQUE_DOMAIN_NAME> \
        PoolName=<UNIQUE_POOL_NAME> \
        PoolDomain=<GLOBAL_UNIQUE_POOL_DOMAIN> \
    --capabilities CAPABILITY_NAMED_IAM
