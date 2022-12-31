FROM python:3.9-slim
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT streamlit run multi_page.py --browser.serverAddress=0.0.0.0 --server.port=8080