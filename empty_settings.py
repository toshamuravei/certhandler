from collections import namedtuple


Site = namedtuple("Site", "subject_name not_after_dt not_after_str")
SMTPConfig = namedtuple("SMTPConfig", "host port ssl user password")

CERT_DAY_CONST = 3

hostnames = (
    "some.host.com",
)

recipients = ["user-recepient@somemail.com",]

check_addr = ""

smtp_config = SMTPConfig(
    host="smtp.host.com",
    port=465,
    ssl=True,
    user="user-sender@somemail.com",
    password="sender-pass")
