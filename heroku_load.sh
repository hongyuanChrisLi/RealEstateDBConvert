#!/bin/bash

source ~/.bash_profile
export RET_DB_URL=$(heroku config:get RET_DB_URL --app real-estate-trends)
python initial_load.py
