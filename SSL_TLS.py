import ssl
import socket
from ssl import SSLContext, PROTOCOL_TLSv1_2


target_host = 'example.com'
target_port = 443

def test_ssl_versions_and_ciphers(host, port):
    
    protocols = [ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_TLSv1_3]
    
    ciphers_to_test = [
        'AES128-GCM-SHA256', 'AES256-GCM-SHA384', 'ECDHE-RSA-AES128-GCM-SHA256',
        'ECDHE-RSA-AES256-GCM-SHA384', 'ECDHE-RSA-AES128-SHA', 'ECDHE-RSA-AES256-SHA384',
        'ECDHE-RSA-CHACHA20-POLY1305', 'DHE-RSA-AES128-GCM-SHA256', 'DHE-RSA-AES256-GCM-SHA384'
    ]
    for protocol in protocols:
        try:
            
            context = SSLContext(protocol)
            context.set_ciphers(':'.join(ciphers_to_test))
            with socket.create_connection((host, port)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    print(f"Testing {ssock.version()} with cipher {ssock.cipher()}")
                    print("  Connection successful.")
        except Exception as e:
            print(f"Failed with protocol {ssl._PROTOCOL_NAMES[protocol]}: {str(e)}")

def test_for_heartbleed(host, port):
    
    print("Testing for Heartbleed...")
   
    print("Heartbleed test not implemented.")


test_ssl_versions_and_ciphers(target_host, target_port)
test_for_heartbleed(target_host, target_port)
