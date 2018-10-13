#! /usr/bin/python
import requests
import os
import sys
import json

def post(creds, job):
    job_url = 'http://test-awx.m3.ebay.com/api/v2/job_templates/'
    job_data = {}

    r = requests.get(job_url, auth=(creds), json=job_data)
    data = r.json()
    results=data.get('results')

def post_no_creds(url, json_data):

    r = requests.post(url, data=json_data)
    data = r.json()
    results=data.get('results')
    print(results)

def main(args):
    #username=
    #password=
    #creds = (username, password)

    url="http://ptsv2.com/t/5j4yd-1536107486/post"
    data={'key':'value'}
    payload=json.dumps(data)
    headers={'Content-Type':'application/json'}

    r = requests.post(url, json=json.dumps(payload))

    #r = requests.post('http://httpbin.org/post', json={'key':'value'})
    #r = requests.post("http://httpbin.org/post", data=payload, timeout=30, headers=headers, verify=False)
    print(r.text)

    '''
    url="http://ptsv2.com/t/5j4yd-1536107486/post"
    data={'first_name': 'Joshua',
            'last_name': 'Stacy',
            'email': "joshuastacy@hotmail.com", 
            'phone': '503-863-7029',
            'cover_letter': 'https://drive.google.com/open?id=1NE3tAadC3atN2-oiQIGlw52rtjKUAr2_R93ba7CCBAM',
            'urls': 'https://www.linkedin.com/in/joshuastacy/'}
    
    #post_no_creds(url, data)
    r = requests.posts(job_url, data=job_data)
    data = r.json()
    results=data.get('results')
    '''

    return(0)

if __name__ == "__main__":
    main(sys.argv)


curl -X POST -H 'Content-type: application/json' --data '{"first_name": "Joshua", "last_name": "Stacy", "email": "joshuastacy@hotmail.com", "phone": "503-863-7029","cover_letter": "https://drive.google.com/open?id=1NE3tAadC3atN2-oiQIGlw52rtjKUAr2_R93ba7CCBAM", "urls": "https://www.linkedin.com/in/joshuastacy/"}' http://ptsv2.com/t/5j4yd-1536107486/post


