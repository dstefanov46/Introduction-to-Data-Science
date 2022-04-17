FROM mysql:8 as database

ADD ./ /docker-entrypoint-initdb.d

RUN /bin/bash -c 'chmod a+rx /docker-entrypoint-initdb.d/*'