# MATCH CASE
# Python 3.10 introduced the match statement, which is similar to the switch statement
# found in other programming languages.
# The basic syntax of the match statement involves matching a variable against several
# cases using the case keyword.

def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "not found"
        case 500:
            return "Internal server error"
        case _: # " _ " it means default value so we can write any value in the print statement
            return "unknown status"

# usage
print(http_status(200)) # output: Ok

print(http_status(404)) # output: not found

print(http_status(500)) # output: internal server error

print(http_status(1)) # output: unknwon status
