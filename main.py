from autoscraper.auto_scraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'



# Press the green button in the gutter to run the script.
# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["How to call an external command?"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
