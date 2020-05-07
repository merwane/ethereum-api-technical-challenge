FROM python:3.6
ADD . .
WORKDIR .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]