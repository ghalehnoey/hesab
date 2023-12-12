#!/bin/bash
mytoken=09155727348
curl --data "token=$mytoken&amount=$1&text=$2" http://77.237.82.98:8000/submit/expense/





