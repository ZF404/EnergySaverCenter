# import paho.mqtt.client as mqtt

# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))

#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("testtopic/1")

# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.payload)






# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message

# client.connect("broker.hivemq.com", 1883, 8000)




# # Blocking call that processes network traffic, dispatches callbacks and
# # handles reconnecting.
# # Other loop*() functions are available that give a threaded interface and a
# # manual interface.
# client.loop_forever()




# ############
# def on_message(_client, userdata, message):
#     print("message received " ,str(message.payload.decode("utf-8")))
#     print("message topic=",message.topic)
#     print("message qos=",message.qos)
#     print("message retain flag=",message.retain)
# ########################################
# broker_address="broker.hivemq.com"

# print("creating new instance")
# client = mqtt.Client("P1") #create new instance
# client.on_message=on_message #attach function to callback
# print("connecting to broker")
# client.connect(broker_address) #connect to broker

# client.loop_start() #start the loop

# print("Subscribing to topic","house/bulbs/bulb1")
# client.subscribe("testtopic/1")
# print("Publishing message to topic","house/bulbs/bulb1")
# client.publish("testtopic/2","OFF")

# time.sleep(4) # wait

# client.loop_stop() #stop the loop

import paho.mqtt.client as mqtt #import the client1
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

        time.sleep(4) # wait

        _client.loop_stop() #stop the loop
    


    def on_message(self, _client, userdata, message):
        print(str(message.payload.decode("utf-8")))
        return str(message.payload.decode("utf-8"))
        
    


mqtta = mqttConnector()

# mqtta.send_message("testtopic/1","SIMA")
while True:
    mqtta.receive_message("testtopic/1")
