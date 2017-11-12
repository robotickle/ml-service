# Machine Learning as a service

## Overview
This project contains machine learning model exposed as an RESTful API over docker using Flask.

## How To Run locally
`python app.py`

## How To Run on Docker
`./docker-run.sh`

## Service will look for 0.0.0.0:5000 on host box to spinup up tls with docker 5000
`http://0.0.0.0:5000/test`
sample response
`id : 123, currentdate : 2017-11-01 02:34:33.659105, prediction : 8.07667908232, removedate : 2017-11-09 02:34:33.659105, invoked-Baeysian : Yes`



## Anaconda SETUP related, not needed for docker installation
conda create -n python2 python=2.7 anaconda
source activate python2
restart pycharm
if pymysql missing
conda install -c anaconda pymysql
