import requests
from bs4 import BeautifulSoup
import time
import csv
import os

# Configure settings
URL = "http://books.toscrape.com/"
DELAY = 1  # Seconds between requests
MAX_PAGES = 3  # Demo limitation
OUTPUT_FILE = "scraped_books.csv"

def scrape_books():
    books = []
    page = 1
    
    while page <= MAX_PAGES:
        print(f"Scraping page {page}...")
        
        # Fetch page with polite headers
        try:
            response = requests.get(
                f"{URL}catalogue/page-{page}.html",
                headers={"User-Agent": "Mozilla/5.0 (Educational Bot)"}
            )
            response.raise_for_status()  # Check for HTTP errors
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            break
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        book_listings = soup.select('article.product_pod')
        
        if not book_listings:
            print("No books found - stopping")
            break
        
        # Extract book data
        for book in book_listings:
            title = book.h3.a["title"]
            price = book.select_one('p.price_color').text
            rating = book.p["class"][1]  # e.g., "Three"
            availability = book.select_one('p.availability').text.strip()
            
            books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability
            })
        
        page += 1
        time.sleep(DELAY)  # Be polite
    
    # Save results
    if books:
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=books[0].keys())
            writer.writeheader()
            writer.writerows(books)
        print(f"\n✅ Saved {len(books)} books to {OUTPUT_FILE}")
    else:
        print("\n❌ No books scraped")

if __name__ == "__main__":
    scrape_books()