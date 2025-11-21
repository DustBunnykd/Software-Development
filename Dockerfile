FROM python:alpine

WORKDIR /app

COPY app.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5004

# Run main.py when the container launches forreal
CMD ["python", "app.py"]