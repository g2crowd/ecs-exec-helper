FROM python:3.9-slim-buster

LABEL "com.github.actions.name"="Comment on Pr with ecs exec"
LABEL "com.github.actions.description"="This is a github action to comment pr"
LABEL "com.github.actions.icon"="airplay"
LABEL "com.github.actions.color"="green"

WORKDIR /

COPY . .

RUN pip3 install --upgrade pip \
    && pip install -r requirements.txt \
    && chmod +x ./entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]