#!/bin/bash

python manage.py dumpdata --indent=4 bookhub > bookhub/fixtures/initial_data.json
python manage.py dumpdata --indent=4 leanread > leanread/fixtures/initial_data.json

rm -rf init_data
cp -R media init_data
