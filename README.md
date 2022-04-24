# TYRO Product API Testing

This Python script performs minor testing of the Tyro Banking API, specifically the product API. 

Python's in-built unit testing framework is chosen for this task. Though this is not strictly unit testing, the Python unit testing framework is a light and simple to use testing framework, and is easily extendable by adding more test cases. This is paired with the 'requests' library, which allows for easy HTTP calls through python, making the code less complex.
## Pre-requisites

* This script does not have access to the server code and relies on public interfaces, thus the API must be online and accessible through the internet.

* The computer from which the script is run must be able to access the internet.

* The required libraries as specified in requirement.txt must be installed.

* Python must be installed.

## Assumptions

* The ProductID of various products is unlikely to change, the script would have to be updated if the ProductID of 'Tyro Business Loan' changes. Though as this is an ID, it is presumed that this is unlikely.

## Addtional Scenarios

Both API end point used should return status 400 if any of the following condition is met

* the header is missing

* the header contains non-numeric 'x-v' version

* the header contains a 'x-v' version less than 1