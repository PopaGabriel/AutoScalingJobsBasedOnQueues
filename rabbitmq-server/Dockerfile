FROM rabbitmq:alpine
EXPOSE 15672
EXPOSE 5672
COPY rabbitmq.conf /etc/rabbitmq/conf.d/10-defaults.conf
COPY rabbitmq.conf /etc/rabbitmq/conf.d/rabbitmq.conf

CMD [ "rabbitmq-server"]