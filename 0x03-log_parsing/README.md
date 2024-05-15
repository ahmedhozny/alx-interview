# Log Parsing Metrics

This Python script reads input log lines from stdin, parses them according to a specified format, and computes metrics such as total file size and counts of HTTP status codes. It prints these statistics after every 10 lines of input or upon receiving a keyboard interruption (CTRL + C).
Usage


## Input Format
The script expects log lines to adhere to the following format:

    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

If a line does not match this format, it will be skipped.

## Metrics
After every 10 lines of input or upon interruption, the script prints the following metrics:

    Total File Size: Cumulative sum of file sizes encountered so far.
    Number of Lines by Status Code: Counts of HTTP status codes observed in the input lines. Supported status codes: 200, 301, 400, 401, 403, 404, 405, and 500. Status codes are printed in ascending order.

## Sample Output

    Total file size: File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
    
    Total file size: File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3
    
    Total file size: File size: 16305
    200: 3
    301: 3
    400: 4
    401: 2
    403: 5
    404: 5
    405: 4
    500: 4
    
    Total file size: File size: 17146
    200: 4
    301: 3
    400: 4
    401: 2
    403: 6
    404: 6
    405: 4
    500: 4
