FROM python:3-slim
WORKDIR /programas/clusteringmodel
RUN pip3 install flask
COPY . .
EXPOSE 50000
CMD [ "python3", "./app_model1.py" ]