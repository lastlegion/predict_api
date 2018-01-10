# predict_api
lightweight REST wrapper around sepsis prediction API

# Build docker container

`docker build -t predict_api .`

# Running

`docker run -itd -p 5000:5000 predict_api`

# API documentation

### POST /predict

Takes an input CSV file, write it to disk, runs simple tensorflow code, returns hello world as a repsonse. 
You can use the following cURL command to test it:

`curl -X POST -F "file=@input.csv" http://localhost:5000/predict`
