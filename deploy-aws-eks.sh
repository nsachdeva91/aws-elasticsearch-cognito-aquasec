# aws ecr create-repository --repository-name k8s/kube-bench --image-tag-mutability MUTABLE

eksctl create cluster \
--name test \
--version 1.14 \
--region us-east-1 \
--nodegroup-name standard-workers \
--node-type t2.small \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--managed