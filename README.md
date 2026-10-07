# Containerized Flask Application on AWS

A basic Flask app containerized with Docker and deployed on AWS using Amazon ECR and Amazon ECS (Fargate).

## Tech Stack
- Python Flask, Gunicorn
- Docker
- Amazon ECR
- Amazon ECS (Fargate)
- AWS Secrets Manager (secure environment variables)

## Endpoints
| Route | Description |
|---|---|
| `/` | Returns a greeting and the current environment |
| `/health` | Health check |
| `/config` | Reports whether the secret `API_KEY` is loaded (never exposes it) |

## Run locally
```bash
pip install -r requirements.txt
python app.py
```

## Run with Docker
```bash
docker build -t flask-ecs-app .
docker run -d -p 5000:5000 -e APP_ENV=local -e APP_NAME=MyApp -e API_KEY=test-key flask-ecs-app


## Deploy to AWS
1. Create an ECR repository and push the image
2. Store sensitive values in AWS Secrets Manager
3. Create an ECS cluster (Fargate) and a task definition with environment variables and secrets
4. Create an ECS service with a security group allowing port 5000
5. Access the app at `http://<PUBLIC_IP>:5000`

## Security
- Non-sensitive config is passed as environment variables
- `API_KEY` is injected from AWS Secrets Manager at runtime
- No secrets are stored in the code or the Docker image