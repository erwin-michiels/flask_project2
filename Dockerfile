FROM python:latest
RUN pip install flask
COPY ./static /home/flask_image/static/
COPY /templates /home/flask_image/templates/
COPY ./flask_app.py /home/flask_image/
EXPOSE 8008
CMD python /home/flask_image/flask_app.py