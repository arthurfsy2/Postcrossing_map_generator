import imaplib
import email
from email.parser import BytesParser
from email.utils import parseaddr
# 如果是企业邮箱，host要更换成企业邮箱的
host = 'imap.qq.com'
user = '254904240@qq.com'
# 不是登录password，是单独生成的邮箱authCode
passwd = 'hyiutupnljhccaaa'
mail_directory = 'INBOX'
conn = imaplib.IMAP4(host)
conn.login(user, passwd)
conn.select(mail_directory)
# status, data = conn.search(None, 'ALL')
# 多条件:来自xxx发件人，未读
status, data = conn.search(None, 'SUBJECT Hurray')
email_list = list(reversed(data[0].split()))
 
 
def decode_str(s):
    try:
        subject = email.header.decode_header(s)
    except:
        # print('Header decode error')
        return None
    sub_bytes = subject[0][0]
    sub_charset = subject[0][1]
    if None == sub_charset:
        subject = sub_bytes
    elif 'unknown-8bit' == sub_charset:
        subject = str(sub_bytes, 'utf8')
    else:
        subject = str(sub_bytes, sub_charset)
    return subject
 
 
def get_email(num, conn):
    typ, content = conn.fetch(num, '(RFC822)')
    msg = BytesParser().parsebytes(content[0][1])
    sub = msg.get('Subject')
    for part in msg.walk():
        fileName = part.get_filename()
        fileName = decode_str(fileName)
        if None != fileName:
            print('+++++++++++++++++++')
            print(fileName)
 
    print(num, decode_str(sub))
 
 
for num in email_list:
    get_email(num, conn)
conn.close()
conn.logout()