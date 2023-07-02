import requests
import json

url="https://scs-pre-sales-004.seal-software.com/seal-ws/v5/documents"

files = {
            'file': open("instrucciones.pdf", 'rb')
            }
fields={
    'reference':'contractroom',
    'createdocx':True
}
headers={
    'X-Session-Token':'69vxiUEHvCgPjxp_gA_gLs0D5kouvpeEMNhG4sphBLsN1DbM0Np3m1PhyI0X0XQWYTD_X_hsXj-Rkg2sqCuksDEj9XA2WpKYrOxF5n4dtP2_FKY4HEL4onVw'
}

s = requests.Session()

res= s.post(url, files=files,data=fields, headers=headers)
print(res.text)



