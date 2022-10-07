import scrapy


class TnuSpider(scrapy.Spider):
    name = 'tnu'
    allowed_domains = ['https://www2.jf.jus.br']
    start_urls = ['https://www2.jf.jus.br/']

    def start_requests(self):
        id = 1
        last_id = 87
        while id <= last_id:
            yield scrapy.Request(f'https://www2.jf.jus.br/phpdoc/virtus/sumula.php?nsul={id}', self.parse)
            id += 1

    def parse(self, response):
        for sumulas in response.css('#conteudo'):
            yield{
                'numero' : sumulas.css('tr:nth-child(2) td::text').getall(),
                'orgao' : sumulas.css('p::text').getall(),
                'data_aprovacao' : sumulas.css('tr:nth-child(6) td::text').getall(),
                'publicacoes' : sumulas.css('tr:nth-child(8) td::text').getall(),
                'enunciado' : sumulas.css('tr:nth-child(10) td::text').getall(),
                'referencias_legislativas' : sumulas.css('tr:nth-child(12) td::text').getall(),
                'precedentes' : sumulas.css('tr:nth-child(14) td::text').getall()
            }
            
