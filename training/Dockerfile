FROM python:3.10-slim
WORKDIR /app
COPY train.py .
RUN pip install pandas scikit-learn joblib
ENTRYPOINT ["python", "train.py"]
