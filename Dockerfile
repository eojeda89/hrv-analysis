FROM python:3.10.11
RUN pip install --upgrade pip
RUN pip install hrv-analysis
RUN pip install flask
COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "--app", "hrv.py", "run", "--host=0.0.0.0"]