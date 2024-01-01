import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def check_page_content(content):
    return "no results" not in content.lower()

def scrape_mudah_my():
    base_url = "https://www.mudah.my/malaysia/cars-for-sale/mercedes-benz/a200?o={}"
    results = []

    i = 1
    while True:
        page_url = base_url.format(i)
        print(f"Fetching {page_url}")
        
        response = requests.get(page_url)
        
        if response.status_code != 200 or not check_page_content(response.text):
            print(f"Stopping at page {i} - Page failed to load or no listings found.")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        car_listings = soup.findAll('div', {'class': 'sc-lhVmIH kKCJlI'})  # This class needs to be verified for the container of listings
       
        for listing in car_listings:
            price = listing.find('div', {'class': 'sc-kPVwWT iALBNo'})           
            year = listing.find('div', {'class': 'sc-fMiknA dQjcwM'})
            
            results.append({
                'price': price.text if price else None,
                'year': year.text if year else None,
            })
        
        i += 1
        sleep(0.05)

    df = pd.DataFrame(results)
    print(df)

scrape_mudah_my()
