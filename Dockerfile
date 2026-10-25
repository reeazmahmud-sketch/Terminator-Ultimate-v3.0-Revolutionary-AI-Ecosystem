FROM python:3.11-slim

# Set environment variables
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY setup.py pyproject.toml ./

# Install Terminator
RUN pip install -e .

# Create non-root user for security
RUN useradd -m -u 1000 terminator
USER terminator

# Create directories for data storage
RUN mkdir -p ~/.terminator/{logs,memory,checkpoints,config}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import terminator; print('OK')" || exit 1

# Default command
ENTRYPOINT ["terminator"]
CMD ["--help"]

# Labels
LABEL maintainer="dev@terminator.ai"
LABEL version="3.0.0-ultimate"
LABEL description="Revolutionary AI ecosystem with sentient consciousness"