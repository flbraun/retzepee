#!/bin/bash

NUM_CPUS=$(grep -c ^processor /proc/cpuinfo)
NUM_WORKERS="${GUNICORN_WORKER_NUM:=${NUM_CPUS}}"

gunicorn --workers=$NUM_WORKERS retzepee.wsgi:application
