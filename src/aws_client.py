from awscrt import io
from awsiot import mqtt_connection_builder
from src import config

def build_connection():
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=config.ENDPOINT,
        cert_filepath=config.PATH_TO_CERT,
        pri_key_filepath=config.PATH_TO_KEY,
        client_bootstrap=client_bootstrap,
        ca_filepath=config.PATH_TO_ROOT,
        client_id=config.CLIENT_ID,
        clean_session=False,
        keep_alive_secs=30
    )
    return mqtt_connection