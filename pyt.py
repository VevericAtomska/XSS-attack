import requests
from bs4 import BeautifulSoup


urls = [
    'http://example.com/login',
    'http://example.com',
    'http://example.com/api/endpoint'
]

def check_csrf_protection(url):
    print(f"Checking CSRF protection on {url}")
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    token = soup.find('input', {'name': 'csrf_token'})
    if token and token.get('value'):
        print("CSRF token is present and populated.")
    else:
        print("CSRF token is missing or empty.")

def check_exposed_git_directory(url):
    check_url = url.rstrip('/') + '/.git/config'
    print(f"Checking for exposed Git directory at {check_url}")
    response = requests.get(check_url)
    if response.status_code == 200 and 'repositoryformatversion' in response.text:
        print("Exposed Git directory found!")
    else:
        print("No exposed Git directory found.")

def test_insecure_deserialization(url):
    print(f"Testing for insecure deserialization at {url}")
    headers = {'Content-Type': 'application/json'}
    
    payload = '{"object": "__type__": "java.util.ArrayList"}'
    response = requests.post(url, data=payload, headers=headers)
    if "exception" in response.text or "java.util.ArrayList" in response.text:
        print("Potential insecure deserialization vulnerability detected!")
    else:
        print("No obvious vulnerability detected.")

def main(urls):
    for url in urls:
        print(f"\nTesting URL: {url}\n")
        
        check_csrf_protection(url)
        
        check_exposed_git_directory(url)
        
        test_insecure_deserialization(url)

main(urls)
