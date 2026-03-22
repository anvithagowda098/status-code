import requests

def fetch_url_status(url):
    """
    Handles both the text validation AND the network request in one place.
    """
    url = url.strip()
    
    # skip the header row and empty lines
    if not url.lower().startswith("http"):
        return None 

    # status and network check 
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        return response.status_code
    except requests.exceptions.Timeout:
        return "Timeout Error"
    except requests.exceptions.TooManyRedirects:
        return "Redirect Loop Error"
    except requests.exceptions.SSLError:
        return "SSL/Certificate Error"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.RequestException:
        return "General Error"

if __name__ == "__main__":
    csv_filename = "Task 2 - Intern.csv"
    try:
        with open(csv_filename, "r", encoding="utf-8-sig") as file:
            for line in file:
                status = fetch_url_status(line)
                if status:
                    print(f"({status}) {line.strip()}")
    except FileNotFoundError:
        print(f"Error: {csv_filename} not found.")
    except UnicodeDecodeError:
        print("Error: Encoding issue with the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")