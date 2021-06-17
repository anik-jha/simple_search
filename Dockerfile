FROM ubuntu:18.04

EXPOSE 6666

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /simple_search/requirements.txt

WORKDIR /simple_search

RUN pip3 install -r requirements.txt

COPY . /simple_search

ENTRYPOINT [ "python3" ]

CMD [ "test.py" ]