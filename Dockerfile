# docker build -t alexik/rabbitmq .
# docker run -it --rm --name rabbitmq -v /home/akaruna/rabbitmq:/rabbitmq -p 5672:5672 -p 8080:15672 alexik/rabbitmq
# docker exec -it rabbitmq /bin/bash
FROM rabbitmq:3-management

RUN apt-get update -yqq && apt-get install -yqq --no-install-recommends python3-pip python3-setuptools
RUN python3 -m pip install pika celery future --upgrade
