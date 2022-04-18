FROM mysql:8.0

ADD ./scripts /docker-entrypoint-initdb.d

RUN /bin/bash -c 'chmod a+rx /docker-entrypoint-initdb.d/*'


