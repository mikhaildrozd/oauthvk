FROM python:3.7
RUN mkdir oauthvk/
COPY requirements.txt oauthvk/
WORKDIR /oauthvk/
RUN pip install -r requirements.txt
ADD . /oauthVKapp/