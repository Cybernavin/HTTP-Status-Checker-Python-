import requests
from rich import print
url = input("Enter url: ").strip()

if not url.startswith(("http://", "https://")):
    try:
        response = requests.get("https://" + url, timeout=5)
        url = "https://" + url

    except requests.exceptions.RequestException:
        response = requests.get("http://" + url, timeout=5)
        url = "http://" + url
else:
    response = requests.get(url, timeout=5)
    
try:
    response = requests.get(url,timeout=5)
    status = response.status_code
    
    print(f"\n[cyan]Target:[/cyan] {url}")
    print(f"[yellow]Status Code:[/yellow] {status}")


    if status == 200:
        print("[bold green]200 OK - Website is reachable.[/bold green]")

    elif status == 301:
        print("[bold yellow]301 Moved Permanently - URL redirects permanently.[/bold yellow]")

    elif status == 302:
        print("[bold yellow]302 Found - Temporary redirect.[/bold yellow]")

    elif status == 403:
        print("[bold red]403 Forbidden - Access denied.[/bold red]")

    elif status == 404:
        print("[bold red]404 Not Found - Page does not exist.[/bold red]")

    elif status == 500:
        print("[bold magenta]500 Internal Server Error - Server has a problem.[/bold magenta]")
    elif status == 502:
        print("[bold magenta]502 Internal Server Error - Server has a problem.[/bold magenta]")
    else:
        print(f"[blue]Received Status Code: {status}[/blue]")



except requests.exceptions.MissingSchema:
    print("[bold red]Invalid URL. Include http:// or https://[/bold red]")
except requests.exceptions.ConnectionError:
    print("[bold red]Connection failed. Check the URL or your internet connection.[/bold red]")

except requests.exceptions.Timeout:
    print("[bold yellow]Request timed out after 5 seconds.[/bold yellow]")

except requests.exceptions.RequestException as error:
    print(f"[bold red]Request failed:[/bold red] {error}")
