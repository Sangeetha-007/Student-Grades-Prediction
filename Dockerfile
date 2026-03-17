# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code and the model
COPY . .

# 6. Expose the port FastAPI will run on
EXPOSE 8080

# 7. Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]