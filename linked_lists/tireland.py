# -*- coding: utf-8 -*-
import scrapy
import json
from tire_pricing.searchable_store_list import StoreList
from tire_pricing.spiders.generic.tire_pricing_by_size_base import TirePricingBySizeBaseSpider
from tire_pricing.items import ClassicTirePricingItem

PLY_RATINGS = ('C', 'D', 'E', 'F', 'G')
PLY_RATINGS_NUMERIC = ('(6)', '(8)', '(10)', '(12)', '(16)')
SIDEWALL_TOKENS = ["BSW", "OWL", "VSB", "RBL", "RWL", "BSL", "ORWL", "ORW", "VOL", "SRL"]


class TirelandSpider(TirePricingBySizeBaseSpider):
    name = 'www.tireland.ca'
    allowed_domains = ['www.tireland.ca', 'www.tireland.com', 'tireland.ca', 'secure1.auto1cloud.com']
    currency = 'CAD'
    context = ['SBS']

    custom_settings = {
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
        'AUTOTHROTTLE_START_DELAY': 5,
        # 'DOWNLOAD_DELAY': 4,
        'AUTOTHROTTLE_MAX_DELAY': 10,
        'DOWNLOAD_TIMEOUT': 60,
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
        'RETRY_HTTP_CODES': [500, 502, 503, 504, 408, 403],
        'REMOVE_PROXY_AFTER_RETRY': True,
        'COOKIES_ENABLED': True,
        'ZYTE_SMARTPROXY_ENABLED': True,
        'AUTOTHROTTLE_ENABLED': False,
        'ZYTE_SMARTPROXY_DEFAULT_HEADERS': {
            'X-Crawlera-Profile': 'desktop',
            'X-Crawlera-Cookies': 'disable'
        },
    }

    def start_requests(self):
        for zip_code in self._input_zip_codes():
            yield scrapy.Request(
                'https://tireland.ca/find-a-location/',
                meta={
                    'item': {
                        'input_zip': zip_code,
                        'zip_code': zip_code
                    }
                },
                callback=self.parse_stores_and_set_location
            )

    def parse_stores_and_set_location(self, response):
        locations = json.loads(response.css('script:contains("locations")').re_first(r'locations: (.*),'))
        store_list = StoreList(locations, zip_code_key='postal_zip', lat_key='lat', lng_key='lng')
        # find_nearest_store(self, zip_code, max_distance_km=80):
        nearest_store = store_list.find_nearest_store(response.meta['item']['input_zip'])
        yield scrapy.Request(
            nearest_store['microsite_url'],
            callback=self.get_location_key_and_search,
            headers={
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://www.tireland.ca',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty'
            },
            meta={
                'item': {
                    **response.meta['item'],
                },
                'store_id': nearest_store['ID'],
                'store_list': store_list
            }
        )

    def get_location_key_and_search(self, response):
        # location_key = response.css("script:contains(create?key)").re_first(r'create?key=(\d+)=')
        # for size in self._input_zip_codes:
        yield scrapy.Request(
            f'https://www.tireland.ca/shop-tires/?client_id=1&loc={response.meta["store_id"]}&brand_filter_by_slug=&search=size&size=2056516',
            callback=self.search,
            meta=response.meta
        )

    def search(self, response):
        location_key = response.css('script::text').re_first(r"create\?key=(\S+)&")
        for size in self._input_sizes():
            yield scrapy.Request(
                f'https://secure1.auto1cloud.com/api/v1//tires/product-search?key={location_key}&nonce=&location_id={response.meta["store_id"]}&search_by=quick_size&product_group=&quick_size={size.raw_size}',
                meta={
                    **response.meta,
                    "item": {
                        **response.meta["item"],
                        'input_section': size.section,
                        'input_aspect': size.aspect,
                        'input_rim': size.rim
                    }
                },
            )

    def parse(self, response):
        if len(json.loads(response.body)['results']['tire_results']) == 0:
            self.logger.debug(f"No available tires for size: {response.meta['item']['input_size']}")
            return
        results = json.loads(response.body)['results']['tire_results']

        for product in results:
            item = ClassicTirePricingItem(response.meta["item"].copy())
            loader = item.loader(selector=product)

            loader.add_value(None, {
                'single_price': product['retail_price'],
                'brand': product['brand'],
                'size': product['size'],
                'unique_product_number': product['ID'],
                'manufacturer_product_number': product['part_number'],
                'section': product['WIDTH'],
                'aspect': product['PROFILE'],
                'rim': product['diameter'],
                'performance_category': product['SEASON'],
                'url': product_url(product, response),
                'model': product['model'],
                'speed': product['speed_rating'],
                'sidewall_style': product['SIDEWALL'],
                'ply': product['XLOAD'],
                'quantity_in_stock': product['inventory_local_and_plus'],
                'tire_load': product['load_index'],
                'run_flat': product['RUNFLAT'],
                'temperature': product['TEMPARATURE'],
                'treadwear': product['TREADWEAR'],
            })

            yield loader.load_item()


def product_url(product, response):
    return f'https://www.tireland.ca/tires/continental/purecontactls/?pn={product["part_number"]}&size={product["size"]}&return_to_search=https%3A%2F%2Fwww.tireland.ca%2Fshop-tires%2F%3Fclient_id%3D1%26loc%3D{response.meta["store_id"]}%26brand_filter_by_slug%3D%26search%3Dsize%26size%3D{product["size"]}&a1c_vehicle_id=false'
