The code in this repository reproduces the issue of raising a `TimeoutError` when the destructor of the `Connecotor` is called.

## How to run to reproduce the issue


```bash
poetry install

CONNECTION_NAME=__your_connection_name__ \
DB_USER=__your_user__ \
DB_PASSWORD=__your_password__ \
export DATABASE_NAME=__your_db_name__ \
  poetry run python src/with_click.py
```


## Result

```
2022-03-07 11:15:42,270 Using selector: KqueueSelector
2022-03-07 11:15:42,270 Checking /***/adc.json for explicit credentials as part of auth process...
2022-03-07 11:15:42,272 No project ID could be determined. Consider running `gcloud config set project` or setting the GOOGLE_CLOUD_PROJECT environment variable
2022-03-07 11:15:42,294 Creating context
2022-03-07 11:15:42,294 Making request: POST https://oauth2.googleapis.com/token
2022-03-07 11:15:42,359 Starting new HTTPS connection (1): oauth2.googleapis.com:443
2022-03-07 11:15:42,501 https://oauth2.googleapis.com:443 "POST /token HTTP/1.1" 200 None
2022-03-07 11:15:42,503 Requesting metadata
2022-03-07 11:15:42,518 Requesting ephemeral certificate
2022-03-07 11:15:42,519 Entered connect method
2022-03-07 11:15:42,703 Entering sleep
2022-03-07 11:15:42,704 Entered _perform_refresh
2022-03-07 11:15:42,704 Creating context
2022-03-07 11:15:42,704 Requesting metadata
2022-03-07 11:15:42,706 Requesting ephemeral certificate
(1,)
Done.
2022-03-07 11:15:42,926 Entering deconstructor
Exception ignored in: <function Connector.__del__ at 0x10274eb80>
Traceback (most recent call last):
  File "/***/python3.9/site-packages/google/cloud/sql/connector/connector.py", line 167, in __del__
  File "/***/python3.9/concurrent/futures/_base.py", line 448, in result
concurrent.futures._base.TimeoutError: 
```
