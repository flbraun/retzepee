FROM python:3.9-slim AS requirements_builder

ENV PATH="${PATH}:/root/.local/bin"
WORKDIR poetry

COPY pyproject.toml poetry.lock ./
RUN pip install --user poetry
RUN poetry export -f requirements.txt --output /requirements.txt


FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# OS update and OS-level libraries/tools
# also create mount points for shared Docker Volumes now, otherwise there will be permission issues
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -U retzepee \
    && mkdir /static /uploads \
    && chown -R retzepee:retzepee /static /uploads

# app dependencies
COPY --from=requirements_builder /requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -f /tmp/requirementst.txt

# app code
WORKDIR /retzepee
USER retzepee:retzepee
COPY --chown=retzepee:retzepee locale locale/
COPY --chown=retzepee:retzepee retzepee retzepee/
COPY --chown=retzepee:retzepee manage.py manage.py
COPY --chown=retzepee:retzepee docker/entrypoint.sh docker/run.sh docker/

ENTRYPOINT ["docker/entrypoint.sh"]
CMD ["docker/run.sh"]
