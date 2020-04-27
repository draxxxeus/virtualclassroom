#!/bin/bash
ssh webroot@oneschool.pw "cd ~/virtualclassroom; git pull; sudo systemctl restart gunicorn"
