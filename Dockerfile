FROM tensorflow/tensorflow:1.4.0 

RUN apt-get update

RUN pip install flask

CMD ["python", "server.py"] 

