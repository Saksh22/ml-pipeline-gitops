FROM python:3.10-slim
WORKDIR /app
COPY evaluate.py .
RUN pip install pandas scikit-learn joblib
ENTRYPOINT ["python", "evaluate.py"]
