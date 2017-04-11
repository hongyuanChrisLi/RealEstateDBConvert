#!/bin/bash

MODE=$1

source ~/.bash_profile
export RET_DB_URL=$(heroku config:get RET_DB_URL --app real-estate-trends)

if [ ${MODE} = 'inital' ]
then
    echo 'Initial Load'
    python initial_load.py
elif [ ${MODE} = 'daily' ]
then
    echo 'Daily Load'
    python main.py
fi
