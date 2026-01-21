import time
import json
from awscrt import mqtt
from src import config, sensors, aws_client

def main():
    print(f"Connecting to AWS IoT Core...")
    mqtt_connection = aws_client.build_connection()
    connect_future = mqtt_connection.connect()
    connect_future.result()
    print("Connected! Starting Production Line...\n")

    try:
        while True:
            # Get Data
            data_a = sensors.get_machine_a_data()
            data_b = sensors.get_machine_b_data()
            data_c = sensors.get_machine_c_data()

            # Publish Data
            def publish(topic, payload):
                mqtt_connection.publish(
                    topic=topic,
                    payload=json.dumps(payload),
                    qos=mqtt.QoS.AT_LEAST_ONCE
                )

            publish("factory/line1/machine_A", data_a)
            print(f"Machine A: Status {data_a['status']}")

            publish("factory/line1/machine_B", data_b)
            print(f"Machine B: Temp {data_b['temperature']}")

            publish("factory/line1/machine_C", data_c)
            print(f"Machine C: Produced {data_c['total_produced']}")

            print("-" * 30)
            time.sleep(config.Delay_Between_Cycles)

    except KeyboardInterrupt:
        print("\nStopping...")
        mqtt_connection.disconnect()

if __name__ == '__main__':
    main()