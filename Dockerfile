FROM python:3.8
WORKDIR /app
COPY . ./
RUN pip install --upgrade pip && pip install -r ./Streamlit/requirements.txt
CMD [ "streamlit","run","Streamlit/main.py" ]