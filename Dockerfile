FROM python:3
ENV PYTHONUNBUFFERED=1
COPY ./wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./FamilyBudget /code/
