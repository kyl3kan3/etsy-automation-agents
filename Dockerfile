# Multi-stage Dockerfile for ArtFlow System
# Stage 1: Backend (Flask API)
FROM python:3.11-slim as backend

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
        curl \
            && rm -rf /var/lib/apt/lists/*

            # Copy requirements and install Python dependencies
            COPY requirements.txt .
            RUN pip install --no-cache-dir -r requirements.txt

            # Copy application code
            COPY . .

            # Create non-root user for security
            RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
            USER appuser

            # Health check
            HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
                CMD curl -f http://localhost:5000/health || exit 1

                # Expose port
                EXPOSE 5000

                # Run the application
                CMD ["python", "app.py"]


                # Stage 2: Frontend (Node.js build)
                # Note: This is a reference. The actual frontend is built in Lovable and deployed separately
                # Keeping this for completeness in case frontend export needed


                # Final production image
                FROM python:3.11-slim

                WORKDIR /app

                # Install runtime dependencies only
                RUN apt-get update && apt-get install -y \
                    curl \
                        && rm -rf /var/lib/apt/lists/*

                        # Copy from backend stage
                        COPY --from=backend /app /app

                        # Create non-root user
                        RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
                        USER appuser

                        # Set environment variables
                        ENV FLASK_ENV=production
                        ENV PYTHONUNBUFFERED=1

                        # Health check
                        HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
                            CMD curl -f http://localhost:5000/health || exit 1

                            EXPOSE 5000

                            CMD ["python", "app.py"]
