# 1. Start with a lightweight Python image

FROM python:3.10-slim



# 2. Set the directory inside the container where our code will live

WORKDIR /app



# 3. Copy the requirements file first (this speeds up builds)

COPY requirements.txt .



# 4. Install the libraries

RUN pip install --no-cache-dir -r requirements.txt



# 5. Copy everything else from your project into the container

COPY . .



# 6. Tell Docker which port the container will use

EXPOSE 8000



# 7. The command to start the API

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
