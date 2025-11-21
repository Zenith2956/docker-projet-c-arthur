# base image
FROM python:3.12

# set workdir
WORKDIR /app

# copy requirements first for layer caching
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# expose internal port
EXPOSE 8080

# run the app
CMD ["python", "app.py"]