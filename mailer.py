import emails
from typing import List
from emails.template import JinjaTemplate as T
import settings


class Mailer:

    def __init__(self) -> None:
        print("Mailer is ready")
        self.recipients = settings.recipients
        self.sent_report = {}

    def notify_recipient(self, sites: List[settings.Site],
                         addresses: List = []) -> None:
        """
        Method sends notification to recipients
        & updates self.sent_report with results.
        """

        if not sites:
            print("There are no sites with expiring SSL certificates")

        if not addresses:
            addresses = self.recipients

        message = emails.html(
            mail_from=("ITS Certificate Automate Checker", "info@smart-transport.ru"),
            html=T(open("letter.html").read()),
            subject="To admins & engineers",
        )

        for addr in addresses:
            r = message.send(
                to=("To admins & engineers ", addr),
                render={"sites": sites},
                smtp=settings.smtp_config._asdict()
            )

            self.sent_report[addr] = r.status_code == 250
