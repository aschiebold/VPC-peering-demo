from confluent_kafka import Producer
import sys

# Kafka configuration
conf = {
    'bootstrap.servers': '....confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '.....',
    'sasl.password': '.....',
    'client.id': 'ccloud-python-client-.....'
}

def delivery_report(err, msg):
    """Callback for delivery reports"""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def main():
    # Initialize producer
    producer = Producer(conf)
    
    # Topic to send messages to (replace with your topic name)
    topic = 'allan-vpc'  # Update this with your actual topic
    
    print("Enter messages to send to Kafka (Ctrl+C to exit):")
    
    try:
        while True:
            # Wait for user input
            message = input("> ")
            
            if message.strip():  # Only send non-empty messages
                # Send message to Kafka
                producer.produce(topic, value=message.encode('utf-8'), callback=delivery_report)
                
                # Trigger delivery callbacks
                producer.poll(0)
                
                # Flush to ensure message is sent
                producer.flush()
                
    except KeyboardInterrupt:
        print("\nStopping producer...")
    finally:
        # Clean up
        producer.flush()
        print("Producer closed")

if __name__ == '__main__':
    main()