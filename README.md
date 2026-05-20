# AWS Project 2 — Serverless Event-Driven CI/CD Pipeline

## Overview

This project implements a fully automated AWS serverless deployment pipeline using:

- AWS Lambda
- Amazon S3
- AWS CloudFormation
- GitHub Actions CI/CD
- CloudWatch Logs
- VSCode Remote SSH
- Git & GitHub

The architecture automatically triggers a Lambda function whenever a file is uploaded into an S3 bucket.

Infrastructure deployment is automated using CloudFormation and GitHub Actions.

---

# Architecture

```text
VSCode
   ↓
Git Push
   ↓
GitHub Actions
   ↓
CloudFormation
   ↓
AWS Lambda
   ↓
S3 Upload Trigger
   ↓
CloudWatch Logs
```

---

# Services Used

| Service | Purpose |
|---|---|
| AWS Lambda | Serverless compute |
| Amazon S3 | Artifact storage + event trigger |
| CloudFormation | Infrastructure as Code |
| GitHub Actions | CI/CD pipeline |
| CloudWatch Logs | Monitoring and observability |
| IAM | Permissions management |
| EC2 | Development environment |
| VSCode Remote SSH | Remote cloud development |

---

# Project Structure

```text
aws-project-2/
│
├── lambda_function.py
├── template2.yaml
├── deploy.py
├── .gitignore
├── notification.json
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
└── README.md
```

---

# Features

- Event-driven architecture
- Automated Lambda deployment
- Infrastructure as Code
- GitHub CI/CD automation
- CloudWatch log monitoring
- Remote cloud development with VSCode
- Real-time S3 event processing

---

# Lambda Workflow

1. File uploaded to S3
2. S3 trigger invokes Lambda
3. Lambda processes event
4. Event stored in CloudWatch Logs

---

# CI/CD Workflow

1. Developer pushes code to GitHub
2. GitHub Actions pipeline starts
3. Lambda package zipped
4. Artifact uploaded to S3
5. CloudFormation deploys infrastructure
6. Lambda automatically updated

---

# Important Commands

## Zip Lambda Function

```bash
zip lambda-function.zip lambda_function.py
```

## Upload Artifact

```bash
aws s3 cp lambda-function.zip s3://lambda-artifacts-949670774201/
```

## Deploy CloudFormation Stack

```bash
aws cloudformation deploy \
--template-file template2.yaml \
--stack-name lambda-projectE \
--capabilities CAPABILITY_NAMED_IAM
```

## Stream CloudWatch Logs

```bash
aws logs tail /aws/lambda/s3-upload-trigger --follow
```

## Upload Test File

```bash
aws s3 cp test.txt s3://lambda-upload-949670774201/
```

---

# Git Commands Used

## Initialize Repository

```bash
git init
```

## Stage Files

```bash
git add .
```

## Commit Changes

```bash
git commit -m "Initial commit"
```

## Connect GitHub Repository

```bash
git remote add origin https://github.com/Ares2211/aws-project-2
```

## Push Code

```bash
git push -u origin main
```

---

# Problems Faced & Fixes

## 1. CloudFormation Pseudo Parameter Error

### Cause
Incorrect:
```yaml
${AWS::Stackname}
```

### Fix
```yaml
${AWS::StackName}
```

---

## 2. S3 Dependency Cycle

### Cause
Single bucket used for:
- Lambda artifacts
- S3 trigger events

### Fix
Created separate upload bucket:
```yaml
UploadBucket:
  Type: AWS::S3::Bucket
```

---

## 3. IAM Access Denied

### Cause
Insufficient EC2 role permissions.

### Fix
Attached:
- IAMFullAccess
- CloudWatchLogsReadOnlyAccess

---

## 4. Stack Rollback Failure

### Cause
Broken stack in:
```text
ROLLBACK_COMPLETE
```

### Fix
```bash
aws cloudformation delete-stack --stack-name lambda-projectE
```

---

## 5. GitHub Actions Workflow Failure

### Cause
Workflow file in wrong directory.

### Fix
Moved workflow into:
```text
.github/workflows/
```

---

## 6. GitHub Actions Trigger Error

### Cause
Missing:
```yaml
on:
```

### Fix
```yaml
on:
  push:
    branches:
      - main
```

---

# Learning Outcomes

- Infrastructure as Code
- Serverless deployments
- Event-driven AWS architecture
- CI/CD automation
- Git workflows
- Remote development
- Cloud monitoring
- IAM permission troubleshooting

---

# Future Enhancements

Upcoming integrations:

- VPC implementation
- Auto Scaling
- Docker
- Jenkins
- SonarQube
- Kubernetes
- Monitoring stack
- Flask/FastAPI applications
- Database integration
- Production-grade CI/CD

---

# Status

Project Completed Successfully

- Lambda Trigger Working
- S3 Notifications Working
- GitHub Actions Working
- CloudFormation Deployment Working
- CloudWatch Logs Working
- VSCode Remote Workflow Working
