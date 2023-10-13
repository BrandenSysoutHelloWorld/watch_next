# Python Version -- 3.11v
FROM python:3.11

# Define Working Directory
WORKDIR /app

# Copies Requirements Text File into Docker Container(root/.)
COPY requirements.txt .

# PIP Install Dependencies < requirements.txt
RUN pip install -r requirements.txt

# Copy Python Script('watch_next.py') into Docker Container(root/.)
COPY watch_next.py .

# Copy Movies Text File('movies.txt') into Docker Container(root/.)
COPY movies.txt .

# CLI Command - Run Python Script('semantic.py')
CMD ["python", "watch_next.py"]
