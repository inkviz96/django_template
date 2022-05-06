#!/bin/sh
echo "Start dump database\n"
dump_cmd=`python manage.py dumpdata --exclude auth.permission --exclude contenttypes  --exclude admin.LogEntry --exclude sessions --indent 2 > db_dump_${1}_${2}.json`
echo "${dump_cmd}"
echo "Dump database complete"