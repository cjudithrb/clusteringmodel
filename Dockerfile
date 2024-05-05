FROM python:3.11.9
RUN pip3 install --no-cache-dir flask==3.0.3 numpy==1.26.1 pandas==2.1.1 scikit-learn==1.3.1
COPY . .
EXPOSE 50000
CMD [ "python3", "./app_model1.py" ]
