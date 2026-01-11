# Deployment Guide - ArtFlow (Etsy Automation System)

## Table of Contents
1. [Local Development](#local-development)
2. 2. [Docker Deployment](#docker-deployment)
   3. 3. [AWS Deployment](#aws-deployment)
      4. 4. [Google Cloud Deployment](#google-cloud-deployment)
         5. 5. [Heroku Deployment](#heroku-deployment)
            6. 6. [DigitalOcean Deployment](#digitalocean-deployment)
               7. 7. [Environment Configuration](#environment-configuration)
                  8. 8. [Monitoring & Logging](#monitoring--logging)
                     9. 9. [CI/CD Pipeline](#cicd-pipeline)
                        10. 10. [Troubleshooting](#troubleshooting)
                           
                            11. ---
                           
                            12. ## Local Development
                           
                            13. ### Prerequisites
                            14. - Python 3.8+
                                - - Node.js 16+ (for frontend dev)
                                  - - Git
                                    - - Virtual environment tool (venv)
                                     
                                      - ### Backend Setup
                                     
                                      - ```bash
                                        # Clone repository
                                        git clone https://github.com/kyl3kan3/etsy-automation-agents.git
                                        cd etsy-automation-agents

                                        # Create virtual environment
                                        python -m venv venv
                                        source venv/bin/activate  # Windows: venv\Scripts\activate

                                        # Install dependencies
                                        pip install -r requirements.txt

                                        # Create .env file
                                        cp .env.example .env

                                        # Edit .env with your configuration
                                        nano .env  # or use your preferred editor
                                        ```

                                        ### Running Locally

                                        ```bash
                                        # Start the Flask backend
                                        python main.py

                                        # The API will be available at http://localhost:5000
                                        ```

                                        ### Frontend Development

                                        Frontend is deployed via Lovable. For local frontend development:

                                        1. Visit: https://lovable.dev/projects/2bc4d0c7-5ea0-4cdf-83a3-999e1de42df3
                                        2. 2. Changes are auto-deployed to: https://print-perfection-bot.lovable.app
                                          
                                           3. ---
                                          
                                           4. ## Docker Deployment
                                          
                                           5. ### Create Dockerfile

                                           ```dockerfile
                                           FROM python:3.9-slim

                                           WORKDIR /app

                                           # Install dependencies
                                           COPY requirements.txt .
                                           RUN pip install --no-cache-dir -r requirements.txt

                                           # Copy application
                                           COPY . .

                                           # Set environment variables
                                           ENV FLASK_APP=main.py
                                           ENV FLASK_ENV=production

                                           # Expose port
                                           EXPOSE 5000

                                           # Run application
                                           CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "main:app"]
                                           ```

                                           ### Create docker-compose.yml

                                           ```yaml
                                           version: '3.8'

                                           services:
                                             web:
                                               build: .
                                               ports:
                                                 - "5000:5000"
                                               environment:
                                                 - FLASK_ENV=production
                                                 - DATABASE_URL=postgresql://user:password@db:5432/etsy_automation
                                               depends_on:
                                                 - db
                                               volumes:
                                                 - ./logs:/app/logs

                                             db:
                                               image: postgres:13
                                               environment:
                                                 - POSTGRES_DB=etsy_automation
                                                 - POSTGRES_USER=user
                                                 - POSTGRES_PASSWORD=password
                                               volumes:
                                                 - postgres_data:/var/lib/postgresql/data
                                               ports:
                                                 - "5432:5432"

                                             redis:
                                               image: redis:6-alpine
                                               ports:
                                                 - "6379:6379"

                                           volumes:
                                             postgres_data:
                                           ```

                                           ### Run with Docker Compose

                                           ```bash
                                           # Build and start containers
                                           docker-compose up -d

                                           # View logs
                                           docker-compose logs -f web

                                           # Stop containers
                                           docker-compose down
                                           ```

                                           ---

                                           ## AWS Deployment

                                           ### Option 1: Elastic Beanstalk (Recommended)

                                           ```bash
                                           # Install EB CLI
                                           pip install awsebcli

                                           # Initialize EB application
                                           eb init -p python-3.9 etsy-automation --region us-east-1

                                           # Create environment and deploy
                                           eb create production
                                           eb deploy

                                           # View logs
                                           eb logs

                                           # Scale up
                                           eb scale 3  # Use 3 instances
                                           ```

                                           ### Option 2: EC2 with Auto Scaling

                                           1. **Launch EC2 Instance**
                                           2. ```bash
                                              # SSH into instance
                                              ssh -i your-key.pem ec2-user@your-instance-ip

                                              # Install dependencies
                                              sudo yum update
                                              sudo yum install python3 python3-pip git

                                              # Clone and setup
                                              git clone https://github.com/kyl3kan3/etsy-automation-agents.git
                                              cd etsy-automation-agents
                                              python3 -m venv venv
                                              source venv/bin/activate
                                              pip install -r requirements.txt
                                              ```

                                              2. **Set up systemd service**
                                              3. ```
                                                 [Unit]
                                                 Description=ArtFlow Etsy Automation
                                                 After=network.target

                                                 [Service]
                                                 User=ec2-user
                                                 WorkingDirectory=/home/ec2-user/etsy-automation-agents
                                                 Environment="PATH=/home/ec2-user/etsy-automation-agents/venv/bin"
                                                 ExecStart=/home/ec2-user/etsy-automation-agents/venv/bin/gunicorn --bind 0.0.0.0:5000 --workers 4 main:app

                                                 [Install]
                                                 WantedBy=multi-user.target
                                                 ```

                                                 3. **Set up RDS Database**
                                                 4. ```bash
                                                    # Use AWS RDS for PostgreSQL
                                                    # Update .env with RDS connection string
                                                    DATABASE_URL=postgresql://user:password@etsy-db.xxxxx.us-east-1.rds.amazonaws.com:5432/etsy_automation
                                                    ```

                                                    4. **Configure Load Balancer**
                                                    5. - Create Application Load Balancer
                                                       - - Target Group: Port 5000
                                                         - - Health Check: /api/health
                                                           - - Auto Scaling Group: Min 2, Max 5 instances
                                                            
                                                             - ### Option 3: AWS Lambda + API Gateway
                                                            
                                                             - ```python
                                                               # Create handler for Lambda
                                                               from flask import Flask
                                                               from awsLambdaWSGIAdapter import LambdaHandler
                                                               from main import app

                                                               def lambda_handler(event, context):
                                                                   asgi_handler = LambdaHandler(app)
                                                                   return asgi_handler(event, context)
                                                               ```

                                                               ---

                                                               ## Google Cloud Deployment

                                                               ### Cloud Run (Serverless)

                                                               ```bash
                                                               # Create Dockerfile (as above)

                                                               # Authenticate
                                                               gcloud auth login

                                                               # Build and deploy
                                                               gcloud run deploy artflow \
                                                                 --source . \
                                                                 --platform managed \
                                                                 --region us-central1 \
                                                                 --allow-unauthenticated \
                                                                 --set-env-vars DATABASE_URL=postgresql://...

                                                               # View logs
                                                               gcloud run logs read artflow --limit 100
                                                               ```

                                                               ### Cloud App Engine

                                                               ```bash
                                                               # Create app.yaml
                                                               runtime: python39

                                                               env: standard

                                                               runtime_config:
                                                                 operating_system: ubuntu22

                                                               handlers:
                                                               - url: /.*
                                                                 script: auto
                                                               ```

                                                               Deploy:
                                                               ```bash
                                                               gcloud app deploy
                                                               ```

                                                               ---

                                                               ## Heroku Deployment

                                                               ```bash
                                                               # Install Heroku CLI
                                                               brew tap heroku/brew && brew install heroku

                                                               # Login
                                                               heroku login

                                                               # Create app
                                                               heroku create artflow-etsy

                                                               # Set environment variables
                                                               heroku config:set FLASK_ENV=production
                                                               heroku config:set DATABASE_URL=postgresql://...
                                                               heroku config:set OPENAI_API_KEY=...

                                                               # Deploy
                                                               git push heroku main

                                                               # View logs
                                                               heroku logs --tail

                                                               # Scale dynos
                                                               heroku ps:scale web=2
                                                               ```

                                                               ---

                                                               ## DigitalOcean Deployment

                                                               ### App Platform

                                                               1. **Connect GitHub Repository**
                                                               2.    - Sign in to DigitalOcean
                                                                     -    - Click "Create" > "App Platform"
                                                                          -    - Select GitHub repository
                                                                           
                                                                               - 2. **Configure**
                                                                                 3. ```yaml
                                                                                    name: artflow
                                                                                    services:
                                                                                      - name: api
                                                                                        github:
                                                                                          repo: kyl3kan3/etsy-automation-agents
                                                                                          branch: main
                                                                                        build_command: pip install -r requirements.txt
                                                                                        run_command: gunicorn --bind 0.0.0.0:8080 --workers 4 main:app
                                                                                            http_port: 8080
                                                                                        envs:
                                                                                          - key: FLASK_ENV
                                                                                            value: production
                                                                                    databases:
                                                                                      - name: postgres
                                                                                        engine: PG
                                                                                        version: "13"
                                                                                    ```

                                                                                    3. **Deploy**
                                                                                    4.    - Click "Create Resources"
                                                                                          -    - Wait for deployment
                                                                                           
                                                                                               - ### Droplet (VPS)
                                                                                           
                                                                                               - ```bash
                                                                                                 # SSH into droplet
                                                                                                 ssh root@your-droplet-ip

                                                                                                 # Update system
                                                                                                 apt update && apt upgrade -y

                                                                                                 # Install dependencies
                                                                                                 apt install -y python3 python3-pip python3-venv git postgresql

                                                                                                 # Clone repository
                                                                                                 git clone https://github.com/kyl3kan3/etsy-automation-agents.git
                                                                                                 cd etsy-automation-agents

                                                                                                 # Setup
                                                                                                 python3 -m venv venv
                                                                                                 source venv/bin/activate
                                                                                                 pip install -r requirements.txt

                                                                                                 # Configure Nginx
                                                                                                 # [See Nginx config below]

                                                                                                 # Start with supervisor
                                                                                                 ```

                                                                                                 ---

                                                                                                 ## Environment Configuration

                                                                                                 ### Required Environment Variables

                                                                                                 ```bash
                                                                                                 # Flask Configuration
                                                                                                 FLASK_ENV=production
                                                                                                 FLASK_APP=main.py
                                                                                                 SECRET_KEY=your-secret-key-here

                                                                                                 # Database
                                                                                                 DATABASE_URL=postgresql://user:password@localhost:5432/etsy_automation

                                                                                                 # API Keys
                                                                                                 OPENAI_API_KEY=sk-...
                                                                                                 ETSY_API_KEY=...
                                                                                                 LEONARDO_API_KEY=...
                                                                                                 TIKTOK_ACCESS_TOKEN=...

                                                                                                 # Redis (for caching/tasks)
                                                                                                 REDIS_URL=redis://localhost:6379/0

                                                                                                 # Logging
                                                                                                 LOG_LEVEL=INFO
                                                                                                 LOG_FILE=logs/etsy_automation.log

                                                                                                 # Monitoring
                                                                                                 SENTRY_DSN=...
                                                                                                 ```

                                                                                                 ### .env.example Template

                                                                                                 ```bash
                                                                                                 # Copy this file to .env and fill in your values
                                                                                                 FLASK_ENV=development
                                                                                                 SECRET_KEY=change-this-secret-key
                                                                                                 DATABASE_URL=sqlite:///etsy_automation.db
                                                                                                 OPENAI_API_KEY=your-key-here
                                                                                                 ETSY_API_KEY=your-key-here
                                                                                                 LEONARDO_API_KEY=your-key-here
                                                                                                 TIKTOK_ACCESS_TOKEN=your-token-here
                                                                                                 ```

                                                                                                 ---

                                                                                                 ## Monitoring & Logging

                                                                                                 ### Setup Sentry (Error Tracking)

                                                                                                 ```python
                                                                                                 # Add to main.py
                                                                                                 import sentry_sdk
                                                                                                 from sentry_sdk.integrations.flask import FlaskIntegration

                                                                                                 sentry_sdk.init(
                                                                                                     dsn=os.environ.get('SENTRY_DSN'),
                                                                                                     integrations=[FlaskIntegration()],
                                                                                                     traces_sample_rate=1.0
                                                                                                 )
                                                                                                 ```

                                                                                                 ### Configure Logging

                                                                                                 ```python
                                                                                                 import logging
                                                                                                 from logging.handlers import RotatingFileHandler
                                                                                                 import os

                                                                                                 if not os.path.exists('logs'):
                                                                                                     os.mkdir('logs')

                                                                                                 file_handler = RotatingFileHandler('logs/etsy_automation.log',
                                                                                                                                   maxBytes=10240000,
                                                                                                                                   backupCount=10)
                                                                                                 file_handler.setFormatter(logging.Formatter(
                                                                                                     '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
                                                                                                 ))
                                                                                                 file_handler.setLevel(logging.INFO)
                                                                                                 app.logger.addHandler(file_handler)

                                                                                                 app.logger.setLevel(logging.INFO)
                                                                                                 app.logger.info('ArtFlow startup')
                                                                                                 ```

                                                                                                 ### Health Check Endpoint

                                                                                                 ```python
                                                                                                 @app.route('/api/health')
                                                                                                 def health():
                                                                                                     return {
                                                                                                         'status': 'healthy',
                                                                                                         'timestamp': datetime.now().isoformat(),
                                                                                                         'database': check_database(),
                                                                                                         'redis': check_redis()
                                                                                                     }

                                                                                                 def check_database():
                                                                                                     try:
                                                                                                         db.session.execute('SELECT 1')
                                                                                                         return 'connected'
                                                                                                     except:
                                                                                                         return 'disconnected'
                                                                                                 ```

                                                                                                 ---

                                                                                                 ## CI/CD Pipeline

                                                                                                 ### GitHub Actions Workflow

                                                                                                 Create `.github/workflows/deploy.yml`:

                                                                                                 ```yaml
                                                                                                 name: Deploy to Production

                                                                                                 on:
                                                                                                   push:
                                                                                                     branches: [main]

                                                                                                 jobs:
                                                                                                   test:
                                                                                                     runs-on: ubuntu-latest
                                                                                                     steps:
                                                                                                       - uses: actions/checkout@v2
                                                                                                       - uses: actions/setup-python@v2
                                                                                                         with:
                                                                                                           python-version: 3.9
                                                                                                       - run: pip install -r requirements.txt
                                                                                                       - run: pytest tests/
                                                                                                       - run: flake8 .

                                                                                                   deploy:
                                                                                                     needs: test
                                                                                                     runs-on: ubuntu-latest
                                                                                                     steps:
                                                                                                       - uses: actions/checkout@v2
                                                                                                       - name: Deploy to Heroku
                                                                                                         uses: akhileshns/heroku-deploy@v3.12.12
                                                                                                         with:
                                                                                                           heroku_api_key: ${{secrets.HEROKU_API_KEY}}
                                                                                                           heroku_app_name: artflow-etsy
                                                                                                           heroku_email: ${{secrets.HEROKU_EMAIL}}
                                                                                                 ```

                                                                                                 ---

                                                                                                 ## Troubleshooting

                                                                                                 ### Common Issues

                                                                                                 **Database Connection Error**
                                                                                                 ```bash
                                                                                                 # Check database URL
                                                                                                 echo $DATABASE_URL

                                                                                                 # Test connection
                                                                                                 psql $DATABASE_URL -c "SELECT 1"

                                                                                                 # Reset database
                                                                                                 python -c "from main import app; app.app_context().push(); db.create_all()"
                                                                                                 ```

                                                                                                 **API Returns 502 Bad Gateway**
                                                                                                 ```bash
                                                                                                 # Check application logs
                                                                                                 docker-compose logs -f web

                                                                                                 # Restart container
                                                                                                 docker-compose restart web

                                                                                                 # Check memory usage
                                                                                                 docker stats
                                                                                                 ```

                                                                                                 **High CPU Usage**
                                                                                                 ```bash
                                                                                                 # Reduce worker count
                                                                                                 # In Gunicorn: --workers 2 (instead of 4)

                                                                                                 # Monitor with
                                                                                                 docker top container-name
                                                                                                 ```

                                                                                                 **File Permission Errors**
                                                                                                 ```bash
                                                                                                 # Fix permissions
                                                                                                 chmod -R 755 ./logs
                                                                                                 chmod -R 755 ./migrations

                                                                                                 # Run as non-root user
                                                                                                 sudo useradd -m -s /bin/bash artflow
                                                                                                 sudo chown -R artflow:artflow /app
                                                                                                 ```

                                                                                                 ---

                                                                                                 ## Scaling Recommendations

                                                                                                 ### Small Scale (< 100 requests/minute)
                                                                                                 - Single EC2 t3.micro instance
                                                                                                 - - RDS db.t3.small
                                                                                                   - - 1 worker process
                                                                                                     - - ElastiCache t3.micro for Redis
                                                                                                      
                                                                                                       - ### Medium Scale (100-1000 requests/minute)
                                                                                                       - - Load Balancer
                                                                                                         - - 2-4 EC2 t3.small instances with Auto Scaling
                                                                                                           - - RDS db.t3.medium with Multi-AZ
                                                                                                             - - ElastiCache r5.large for Redis
                                                                                                               - - CloudFront CDN
                                                                                                                 - 
                                                                                                                 ### Large Scale (1000+ requests/minute)
                                                                                                                 - Load Balancer with geo-routing
                                                                                                                 - - 5-10 EC2 c5.large instances with Auto Scaling
                                                                                                                   - - RDS db.r5.large with Read Replicas
                                                                                                                   - ElastiCache r6g.xlarge cluster
                                                                                                                   - - RabbitMQ for task queues
                                                                                                                     - - Full monitoring stack (CloudWatch, Datadog, etc.)
                                                                                                                      
                                                                                                                       - ---
                                                                                                                       
                                                                                                                       ## Maintenance
                                                                                                                       
                                                                                                                       ### Regular Tasks
                                                                                                                       
                                                                                                                       **Weekly**
                                                                                                                       - Check application logs for errors
                                                                                                                       - - Monitor disk space
                                                                                                                         - - Review API response times
                                                                                                                          
                                                                                                                           - **Monthly**
                                                                                                                           - - Update dependencies: `pip list --outdated`
                                                                                                                             - - Run security checks: `safety check`
                                                                                                                               - - Database maintenance: `VACUUM ANALYZE`
                                                                                                                                
                                                                                                                                 - **Quarterly**
                                                                                                                                 - - Load testing
                                                                                                                                   - - Disaster recovery drill
                                                                                                                                     - - Security audit
                                                                                                                                      
                                                                                                                                       - ---
                                                                                                                                       
                                                                                                                                       ## Support
                                                                                                                                       
                                                                                                                                       For deployment issues:
                                                                                                                                       1. Check application logs
                                                                                                                                       2. 2. Review this guide section by section
                                                                                                                                          3. 3. Search existing GitHub issues
                                                                                                                                             4. 4. Create a new GitHub issue with logs and details
