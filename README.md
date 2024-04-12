# Dev Assessment - Webhook Receiver

Please use this repository for constructing the Flask webhook receiver.

*******************

## Setup

* Create a new virtual environment

```bash
pip install virtualenv
```

* Create the virtual env

```bash
virtualenv venv
```

* Activate the virtual env

```bash
source venv/bin/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Run the flask application (In production, please use Gunicorn)

```bash
python run.py
```

* The endpoint is at:

```bash
POST http://127.0.0.1:5000/webhook/receiver
```

```bash
http://127.0.0.1:5000/webhook/fetcher
```
this endpoint is for fetching data from Mongodb Atlas

```bash
http://127.0.0.1:5000/webhook/
```
this endpoint is for showing the data on web browsers
* Use this endpoint to watch the data *

You need to use this as the base and setup the flask app. Integrate this with MongoDB (commented at `app/extensions.py`)


You have to set-up URL in webhooks section of github and that doesn't supports localhost that's why use ngrok to get a public url

*******************# WebHooks_Github
