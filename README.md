# Amazon-scrapper

This is a Scrapy project to scrape Names, Author and Price of books from " https://www.amazon.in/s?k=books&i=digital-text&ref=nb_sb_noss_2 "  

Extracted data

This project extracts Names, Author and Price of books The extracted data looks like this sample:

{
    'author': 'Manish Chadda',
    
    'name': 'हँसो और बढ़ो (कथा Book 1) (Hindi Edition)',
    
    'price': '49',
}

Spiders

This project contains one spider and you can list it using the list command:

$ scrapy list
amazon_spider

The spider (amazon_spider) extract the data from the website and employs CSS selectors.

You can learn more about the spiders by going through the [Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html) .

Running the spiders

You can run a spider using the scrapy crawl command, such as:

$ scrapy crawl amazon_spider

If you want to save the scraped data to a file, you can pass the -o option:

$ scrapy crawl amazon_spider -o books.json

