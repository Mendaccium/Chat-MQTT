import paho.mqtt.client as mqtt
import time


def on_connect(client,userdata,flags,rc):
    print("Connectado ao broker!")
def on_message(client,userdata,message):
    global inputMessage
    if str(message.topic) != pubtop:
        msg = str(message.payload.decode("utf-8"))
        print(str(message.topic),':', msg)
       
        inputMessage = input("Mensagem: ")
        client.publish(pubtop,inputMessage)
def on_subscribe(client, userdata,mid,granted_qos):
    print("Subscribed!")
def on_disconnect(client,userdata,rc):
    if rc != 0:
        print("ERROR: Client Disconeted!")


client = mqtt.Client('client02')
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883)

time.sleep(1)

pubtop = "pessoa_02"
subtop = "pessoa_01"


inputMessage = None

client.loop_start()
client.subscribe(subtop)

while True:
    if inputMessage == "Stop" or inputMessage == "stop":
        break

client.disconnect()
client.loop_stop()
