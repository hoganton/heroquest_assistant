FROM python:slim

WORKDIR /flaskapp
COPY ./flask_app/ .
RUN pip install -r requirements.txt && chmod a+x boot.sh
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
