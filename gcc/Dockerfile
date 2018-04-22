FROM gcc:6.3

WORKDIR /app/src

COPY ./src/main.c /app/src/main.c
COPY ./src/in.txt /app/src/in.txt
COPY ./src/run.sh /app/src/run.sh

CMD ["dos2unix run.sh"]

CMD ["./run.sh"]
