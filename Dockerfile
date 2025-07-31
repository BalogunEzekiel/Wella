# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and config files
COPY . .

# Add Streamlit config explicitly
RUN mkdir -p /root/.streamlit
COPY .streamlit/config.toml /root/.streamlit/config.toml

# Expose Streamlit port
EXPOSE 8501

# Start Streamlit app (uses your config)
CMD ["streamlit", "run", "app.py"]
