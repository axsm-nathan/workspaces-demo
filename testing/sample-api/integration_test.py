import requests

"""
This is going to serve as a script to run integration tests on the sample-api.

Steps
1. read sample data, import expected SFMC record
2. for each test case, make a request to the API
3. wait a few seconds, read SFMC DE to see if expected record is found using SFMC Rest API
4. compile results in Spreadsheet
5. write each Lambda's tests to an Excel tab
"""

def main():

    print("Running tests!")
# end main()


def make_test_request():
    """
    This function will make a request to the sample API and return the response.
    """
    # Make a request to the sample API
    response = requests.get("XXXXXXXXXXXXXXXXXXXXXX")
    return response
# end make_test_request()


def search_sfmc_email():
    return None
# end search_sfmc_email()


def search_sfmc_email_copay():
    return None
# end search_sfmc_email_copay


def import_test_cases():

    return []
# end import_test_cases()


if __name__ == "__main__":
    main()