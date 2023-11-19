from flask import Flask, request
from confluent_kafka import Producer

app = Flask(__name__)

@app.route('/', methods=['POST'])
def ingest_log():
    log_data = request.json
    # Send log to Kafka
    produce_log(log_data)
    return "Log ingested successfully"

def produce_log(log_data):
    producer = Producer({'bootstrap.servers': 'localhost:9092'})
    producer.produce('log_topic', key='log', value=str(log_data))
    producer.flush()


@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=8000)
