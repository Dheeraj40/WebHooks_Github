from flask import Blueprint, json, request, render_template
from app.extensions import add_document, fetch_data
# from app.templates import 
import schedule
import time

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


def extract_event_data(payload):
    if 'action' in payload:
        # pull_request open or close
        if payload['action'] == 'opened':
            # pull_request
            author = payload['pull_request']['user']['login']
            from_branch = payload['pull_request']['head']['ref']
            to_branch = payload['pull_request']['base']['ref']
            timestamp = payload['pull_request']['updated_at']
            return {'event_type': 'pull_request', 'author': author, 'from_branch': from_branch, 'to_branch': to_branch, 'timestamp': timestamp}
        else:
            # pull_request merged
            author = payload['pull_request']['user']['login']
            from_branch = payload['pull_request']['head']['ref']
            to_branch = payload['pull_request']['base']['ref']
            timestamp = payload['pull_request']['merged_at']
            return {'event_type':'merge', 'author': author, 'from_branch': from_branch, 'to_branch': to_branch, 'timestamp': timestamp}
    else:
        # push request 
        author = payload['head_commit']['author']['name']
        to_branch = payload['ref'].split("/")[-1]
        timestamp = payload['head_commit']['timestamp']
        return {'event_type': 'push', 'author': author, 'to_branch': to_branch, 'timestamp': timestamp}

@webhook.route('/receiver', methods=["POST"])
def receiver():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        data = extract_event_data(data)
        add_document(data)

    return {'status':'success'}, 200

@webhook.route('/test', methods=['GET'])
def test():
    add_document({'test':'test'})
    return {'message': 'Hello World!'}, 200

@webhook.route('/')
def ind():
    print('Hello World')
    return render_template('index.html')


@webhook.route('/fetcher')
def index():
    
    # Fetch recent updates from MongoDB (assuming 'events' collection)
    recent_updates = list(fetch_data()) # Adjust limit as needed
    data_to_show = ""
    for update in recent_updates[0]:
        event_type = update.get('event_type', 'Unknown')

        if event_type == 'push':
            author = update.get('author', 'Unknown')
            to_branch = update.get('to_branch', 'Unknown')
            timestamp = update.get('timestamp', 'Unknown')

            ans = f'"{author}" pushed to "{to_branch}" on {timestamp}'
            data_to_show = data_to_show + "\n" + ans
            print(ans)

        elif event_type == 'pull_request':
            author = update.get('author', 'Unknown')
            from_branch = update.get('from_branch', 'Unknown')
            to_branch = update.get('to_branch', 'Unknown')
            timestamp = update.get('timestamp', 'Unknown')

            ans = f'"{author}" submitted a pull request from "{from_branch}" to "{to_branch}" on {timestamp}'
            data_to_show = data_to_show + "\n" + ans
            print(ans)

        elif event_type == 'merge':
            author = update.get('author', 'Unknown')
            from_branch = update.get('from_branch', 'Unknown')
            to_branch = update.get('to_branch', 'Unknown')
            timestamp = update.get('timestamp', 'Unknown')

            ans = f'"{author}" merged branch "{from_branch}" to "{to_branch}" on {timestamp}'
            data_to_show = data_to_show + "\n" + ans
            print(ans)

        else:
            print('Unknown event type:', event_type)

    return data_to_show


# # Schedule the index function to run every 15 seconds
# schedule.every(15).seconds.do(index) 

# # Run the scheduler continuously          
# while True:
#     schedule.run_pending()
#     time.sleep(1)
