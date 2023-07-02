import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

related = MIMEMultipart('related')

submission = MIMEText('text', 'xml', 'utf8')
submission.set_payload(open('ArchiveDomain.pdf', 'rb').read())
related.attach(submission)

body = related.as_string().split('\n\n', 1)[1]
headers = dict(related.items())
headers["content-type"]="multipart/form-data"
headers["X-Session-Token"]="58ap0fNkxMyjDJDyHv-PwD3X_yzGmkRdNKZrSlOQtF3CZCMPDpXCQtcab6Z_8Jmj994WKNvHsvryAT9nDuAG95OA76Bid8o5IVUVsQmpZ0iB3KSOBJXODv1g"
r = requests.post("https://scs-pre-sales-004.seal-software.com/seal-ws/v5/documents", data=body, headers=headers)

print(r.text)