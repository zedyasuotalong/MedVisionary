
## This repo is the source code of MedVisionary server, written in python using Flask.

Usage:  
  
  step 1: start your DataBase Server and enter you database  
  step 2: source /you/workspace/path/script/cmd.sql  
  step 3: source /you/workspace/path/script/insert.sql  
  step 4: configure server.ini and python app.py  
  stem 5: use your Http client to send request to MedVisionary, the request example are like:  
          curl -X GET -H "Content-Type: application/json" -d '{"doctor_id": 1}' http://ip:port/patient/query_by_doctor_id  
