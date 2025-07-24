#!/bin/bash
echo "[*] Enumerating IAM roles and policies..."
aws iam list-roles
aws iam list-policies

echo "[*] Checking S3 buckets..."
aws s3 ls
aws s3api list-buckets --query "Buckets[].Name"
