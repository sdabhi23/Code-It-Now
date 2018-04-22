FROM python:3.6-alpine

# set /app/src as working directory
WORKDIR /app/src

# install requirements
# this way when you build you won't need to install again
# and since COPY is cached we don't need to wait
COPY /requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY . .

CMD ["dos2unix run.sh"]

CMD [ "./run.sh" ]
