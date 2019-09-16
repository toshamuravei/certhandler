import ssl
import socket
from typing import List
from datetime import datetime
from settings import Site


class CertGetter:

    def __init__(self) -> None:
        print("Ready to check some certs")

    def get_cert(self, hostname: str) -> List[Site]:
        context = ssl.create_default_context()
        ssl_socket = context.wrap_socket(socket.socket(), server_hostname=hostname)
        ssl_socket.connect((hostname, 443))
        cert = ssl_socket.getpeercert()
        subject_names_tuple = cert.get("subjectAltName")
        names = [x[1] for x in subject_names_tuple]
        try:
            not_after = datetime.strptime(cert.get("notAfter"), "%b %d %H:%M:%S %Y %Z")
        except TypeError:
            print("No 'notAfter' datetime was found, it would be set to None")
            not_after = None
        ssl_socket.close()
        sites = [Site(name, not_after, cert.get("notAfter")) for name in names]
        return sites

