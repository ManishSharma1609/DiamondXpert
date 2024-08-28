FROM python:3.8-slim-buster
USER root
RUN mkdir /app
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements_dev.txt
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT = 1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING = true
RUN airflow db init
RUN airflow users create -e manishsharmachd19@gmail.com -f manish -l sharma -p admin -r Admin -u admin
RUN chmod 777 start.sh
RUN apt update -y 
ENTRYPOINT [ "/bin/sh" ]
CMD [ "start.sh" ]
