# python web job demo 

step 1: create the webapp with python3.6 as runtime. 
step 2: select window as os while creating webapp .
step 3: make as zip of simple folder containing simple.py and dependent libraries .
step 4: create a webjob and upload the zip folder

webhook Call: 
POST /api/triggeredwebjobs/{job name}/run
GET /api/triggeredwebjobs/{job name}/history


https://github.com/projectkudu/kudu/wiki/WebJobs-API#invoke-a-triggered-job

