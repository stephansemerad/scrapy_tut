import scrapy 

class PostSpider(scrapy.Spider):
    name = 'numista'
    start_urls = [
        'https://en.numista.com/catalogue/afghanistan-banknotes-1.html',
        'https://en.numista.com/catalogue/afghanistan-banknotes-2.html'
    ]
    
    def parse(self, response):
        print(response.body)
        page = response.url.split('/')[-1]
        filename = page 
        with open('html/'+filename, 'wb') as f:
            f.write( response.body)
            
            
            
        