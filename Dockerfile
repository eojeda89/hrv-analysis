FROM python:3.10.11
RUN pip install hrv-analysis
RUN pip install flask
COPY . .
EXPOSE 5000
CMD ["python", "hrv.py"]