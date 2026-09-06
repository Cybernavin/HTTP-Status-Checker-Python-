# HTTP-Status-Checker-Python-
beginner-friendly Python tool that checks whether a website is reachable and displays common HTTP status codes with colored terminal output using the Rich library.
Features
Automatically accepts URLs with or without http:// or https://
Tries HTTPS first, then falls back to HTTP
Displays common HTTP status codes:
200 OK
301 Moved Permanently
302 Found
403 Forbidden
404 Not Found
500 Internal Server Error
502 Bad Gateway

Status	URL
200	https://httpstat.us/200
301	https://httpstat.us/301
302	https://httpstat.us/302
403	https://httpstat.us/403
404	https://httpstat.us/404
500	https://httpstat.us/500
Future Improvements
Display response time.
Show server banner (Server header).
Detect redirects and final destination URL.
Support checking multiple URLs from a file.
