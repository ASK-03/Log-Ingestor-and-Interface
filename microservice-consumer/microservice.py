from flask import Flask
from confluent_kafka import Consumer, KafkaError
import sqlite3

app = Flask(__name__)

@app.route('/')
def process_logs():
    consume_logs()
    return "Logs processed successfully"

def consume_logs():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'log-consumer-group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['log_topic'])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        log_data = eval(msg.value().decode('utf-8'))  # Assuming log data is a dictionary
        process_and_store_log(log_data)

    consumer.close()

def process_and_store_log(log_data):
    # # Implement your processing logic here
    # # Store processed log in the database
    # conn = sqlite3.connect('logs.db')
    # cursor = conn.cursor()
    # cursor.execute('INSERT INTO logs (message, level, timestamp) VALUES (?, ?, ?)',
    #                (log_data.get('message'), log_data.get('level'), log_data.get('timestamp')))
    # conn.commit()
    # conn.close()
    return

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=8000)
