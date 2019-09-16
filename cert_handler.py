import sys
import socket
import settings
from typing import Union
from datetime import datetime
from collections import namedtuple
from cert_getter import CertGetter
from mailer import Mailer


class CertHandler:

    def __init__(self) -> None:
        """
        Initialising CertHandler instance. Script will
        exit here if there is no internet connection.
        """
        self.cert_getter = CertGetter()
        self.mailer = Mailer()
        self.sites_to_notify = []
        if not self.check_conn():
            sys.exit("Can't establish Internet connection. Bye bye!")

    def run(self) -> None:
        """
        Method handles main logic: calls for cert check,
        calls for notification and print result of work.
        """
        self.handle_cert_check()
        self.mailer.notify_recipient(self.sites_to_notify)
        if self.mailer.sent_report:
            print("Email sent status: ")
            for addr, status in self.mailer.sent_report.items():
                print("Successfuly sent for {}: {}".format(addr, status))

    def check_conn(self, host: str = "8.8.8.8",
                   port: int = 53, timeout: int = 3) -> Union[True, False]:
        """
        Methods checks for net connection,
        using 8.8.8.8:53 and 3sec timeout.
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            print(ex)
            return False

    def check_expiration(self, site: Site) -> Union[True, False]:
        """
        Method checks given Site's SSL lifetime with
        comparing expiration (in days) and constant.
        """
        try:
            delta = site.not_after_dt - datetime.now()
        except TypeError:
            print("Site.not_after is set to None, can't compare datetimes")
            return True

        if delta.days <= settings.CERT_DAY_CONST:
            return True
        else:
            return False

    def handle_cert_check(self) -> None:
        """
        Methods gathers SSL certs data and checks
        expirations updating self.sites_to_notify.
        """
        for name in settings.hostnames:
            sites = self.cert_getter.get_cert(name)
            self.sites_to_notify += [s for s in sites if self.check_expiration(s)]


if __name__ == "__main__":
    handler = CertHandler()
    handler.run()
