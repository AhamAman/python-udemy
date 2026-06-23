# 1. Fetch a lightweight, optimized base Python image
FROM python:3.11-slim

# 2. Establish an internal execution directory path
WORKDIR /app

# 3. Install necessary OS-level compilation tools safely
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy and install library dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application file layers
COPY . .

# 6. Expose the traditional Streamlit network port
EXPOSE 8501

# 7. Configure internal engine flags to suppress local browser pops inside container
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 8. Start the Streamlit application server process
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]