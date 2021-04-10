import paho.mqtt.client as mqtt
import time

class mqttConnector:

    def send_message(self, topic, message):
        _client = mqtt.Client()
        _broker_address="broker.hivemq.com"
        _client.connect(_broker_address, 1883, 60)
        _client.loop_start() #start the loop
        _client.publish(topic, message)
        time.sleep(1) # wait
        _client.loop_stop() #stop the loop

    def receive_message(self, topic):
        _client = mqtt.Client()
        _client.on_message = self.on_message
        _broker_address="broker.hivemq.com"
        _client.connect(_broker_address, 1883, 60)
        _client.loop_start() #start the loop
        _client.subscribe(topic)
        time.sleep(1) # wait
        _client.loop_stop() #stop the loop
    
    def on_message(self, _client, userdata, message):
        return str(message.payload.decode("utf-8"))
        
    



