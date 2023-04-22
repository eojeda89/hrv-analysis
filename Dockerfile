FROM python:3.10.11
RUN pip3 install hrv-analisis
RUN pip3 install flask
COPY . .
EXPOSE 5000
CMD ["python", "hrv.py"]