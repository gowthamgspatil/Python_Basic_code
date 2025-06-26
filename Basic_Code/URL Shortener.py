import pyshorteners

url = input("Enter the URL to shorten: ")
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)
print("Shortened URL:", short_url)
