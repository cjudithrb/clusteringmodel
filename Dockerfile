FROM python:3-slim
RUN pip3 install --no-cache-dir flask numpy pandas scikit-learn
COPY . .
EXPOSE 50000
CMD [ "python3", "./app_model1.py" ]
