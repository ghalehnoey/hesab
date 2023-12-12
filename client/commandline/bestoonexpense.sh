#!/bin/bash
mytoken=9159703466
curl --data "token=$mytoken&amount=$1&text=$2" http://localhost:8000/submit/expense/





