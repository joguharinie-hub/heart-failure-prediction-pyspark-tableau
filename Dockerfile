FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip &&     pip install pyspark pandas scikit-learn

CMD ["python", "run_pipeline.py"]
