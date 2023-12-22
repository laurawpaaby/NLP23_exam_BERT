import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_eb(url_input):
    """
    Function for scraping EB articles from a list of URLs. 
    """
    
        # Loop through each URL
    with open('unsuccessful_scrapes.txt', 'w') as file:
        for index, url in enumerate(url_input, start=0):
            try:
                # Send a GET request
                response = requests.get(url)
                # Check if the request was successful
                response.raise_for_status()

                # Parse the HTML content
                soup = BeautifulSoup(response.content, 'html.parser')
                
                
                # Find the <span> element with the data-timestamp attribute
                timestamp_element = soup.find('span', {'data-timestamp': True})

                # Extract the timestamp value
                timestamp = timestamp_element['data-timestamp']
                            
                # Extract elements by class name
                title = soup.find('h1', class_='art-title').get_text(strip=True)
                subtitle = soup.find('h2', class_='art-subtitle').get_text(strip=True)
                reviewer = soup.find('a', class_='fontweight-bold').get_text(strip=True)
                bodytext = soup.find('div', id='fnBodytextTracking').get_text(strip=True)
                
                
                # Find all elements with the class "icon-svg eb-rating"
                eb_elements = soup.find_all(class_="icon-svg eb-rating")
                # Count the total number of instances
                eb_rating = len(eb_elements)
                
            
                user_elements = soup.find_all(class_="icon-svg user-rating")
                # Initialize a variable to keep track of the star count
                user_star_count = 0
                # Iterate through the elements and count stars based on the use xlink:href attribute
                for element in user_elements:
                    xlink_href = element.find('use')['xlink:href']
                    if xlink_href == '#star-solid':
                        user_star_count += 1
                    elif xlink_href == '#star-half-solid':
                        user_star_count += 0.5
            
                eb_elements = soup.find_all(class_="icon-svg eb-rating")
                # Initialize a variable to keep track of the star count
                eb_star_count = 0
                # Iterate through the elements and count stars based on the use xlink:href attribute
                for element in eb_elements:
                    xlink_href = element.find('use')['xlink:href']
                    if xlink_href == '#star-solid':
                        eb_star_count += 1
                    elif xlink_href == '#star-half-solid':
                        eb_star_count += 0.5
            
            
                # Append to the list as a dictionary
                data.append({
                    'Url': url,
                    'Date': timestamp,
                    'Title': title,
                    'Subtitle': subtitle,
                    'Reviewer': reviewer,
                    'EB_Rating': eb_star_count-6,
                    'US_Rating': user_star_count-6,
                    'BodyText': bodytext
                })

            except Exception:
                # Write the unsuccessful URL to the text file
                file.write(url + '\n')

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)
    
    df['Date'] = df['Date'].str[:10]
    
    return df
    


if __name__ == "__main__":
    
    # read in URLs
    path_to_urls = 'webscraper_eb_urls.csv'
    df = pd.read_csv(path_to_urls, delimiter=';', header=None)
    df.columns = ['Title', 'URL']

    # append all URLs to a list 
    urls = []
    for url in df['URL']:
        urls.append(url)
        
    # apply scraping function to the list of urls
    eb_df = scrape_eb(urls)
    # turn all columns into strings
    eb_df = eb_df.astype(str)
    # remove rows where all values except URL are the same
    eb_df = eb_df.drop_duplicates(subset=['Date', 'Title', 'Subtitle', 'Reviewer', 'EB_Rating', 'US_Rating', 'BodyText'], keep='first')

    eb_df.to_csv('full_scraped_articles.csv')  

