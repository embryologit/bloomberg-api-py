import requests
import json

REQUEST_HEADERS = {
    'authority': 'www.bloomberg.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'agent_id=9f2bb4ef-7f2c-4837-8414-1adec058b7af; session_id=75e8806c-c818-4cfa-bc14-ffad41c591ad; session_key=cedbe85aa42ce389de11f95467b8511719ac1286; gatehouse_id=3a08ccd6-8ec7-4e6f-bade-70f0296e8f02; geo_info=%7B%22countryCode%22%3A%22DE%22%2C%22country%22%3A%22DE%22%2C%22field_n%22%3A%22cp%22%2C%22trackingRegion%22%3A%22Europe%22%2C%22cacheExpiredTime%22%3A1637767817335%2C%22region%22%3A%22Europe%22%2C%22fieldN%22%3A%22cp%22%7D%7C1637767817335; _pxvid=41425bb6-47bd-11ec-af6d-5244734f5643; _sp_v1_uid=1:444:3e22b8d4-371e-48fa-aeba-4be890c01d4f; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXQGVlk0kYw8EMOgNhaXkfSQUIoFAORdi1xUAQAA; _sp_v1_csv=null; _sp_v1_lt=1:; ccpaUUID=ec9c365a-fe56-4ca0-9af9-0824a3e25686; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; _sp_krux=true; consentUUID=b6028d5a-191a-4417-a42a-9c0b5031c567_1; euconsent-v2=CPP02HiPP02HiAGABCENB1CgAP_AAGPAAAYgH9oB9CpGCTFDKGh4AIsAEAQXwBAEAOAAAAABAAAAAAgQAIwCAEASAACAAAACAAAAIAIAAAAAEAAAAAAAQAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAIEAAAAAAUAAABAAgEAAABIAQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgYtARAAcACEAHIAPwAvgCOAIHAQcBCACIgEWALqAYEA14B1AFlALzAYsAUMgCABMAEcARwBeYSAoAAsACoAGQAOAAgABkADSAIgAigBMACeAH4AQgAjgBSgDKAHeAPYAjgBKQGSCoAoATABHAEcAU2AvMdAYAAWABUADIAHAAQAAuABkADSAIgAigBMACeAGIAPwAjgBMACjAFKAMoAd4A9gCOAEpAOoAyQcABAAuQgFAALAAyAC4AJgAYgBHADvAI4ASkA6hKAYAAsADIAHAAiABMADEAI4AUYApQB3gEcAOoSAAgAXKQEwAFgAVAAyABwAEAAMgAaQBEAEUAJgATwAxAB-AFGAKUAZQA7wCOAEpAZIUABAAXAJ2AAA.YAAAAAAAAAAA; consentUUID=b6028d5a-191a-4417-a42a-9c0b5031c567_1; _sp_v1_data=2:392777:1637163871:0:1:-1:1:0:0:_:-1; _sp_v1_opt=1:login|true:last_id|11:; _sp_v1_consent=1\u00210:-1:-1:-1:-1:-1; bbgconsentstring=req1fun1pad1; bdfpc=004.0798118908.1637163875871; _gcl_au=1.1.1720942935.1637163876; _uetvid=44e8114047bd11ec92b22f9017b0ecd7; _ga=GA1.2.1490423973.1637163877; _rdt_uuid=1637163877464.5392f96e-6945-409f-b570-c991ab7f3ac3; _scid=4cb379ec-1c36-4923-830a-f3d912592400; _parsely_visitor={%22id%22:%22pid=ec7166d70d0618210d77ec91c9ff47fc%22%2C%22session_count%22:1%2C%22last_session_ts%22:1637163878100}; _fbp=fb.1.1637163878386.322604158; __gads=ID=780c8d3c1717c19b:T=1637163876:S=ALNI_MYhi11N9mUsWpAG6mTst5btaNzE1w; _lc2_fpi=b1166d620485--01fmq94jsganf9p3gdwdy59x2d; _cc_id=c7ad973acd6d72e5dd868e2f901ccdb4; _cc_cc=ACZ4XmNQSDZPTLE0N05MTjFLMTdKNU1JsTCzSDVKszQwTE5OSTJhAILEqcrpIBoChLec3aPDeCiO4T8jI8PWlfelYezNSOxNSOzlt2eKw9QsRBJfux6h98oqBHvbWgT7%2BKYpLDC9Hz9bwpjnjh5ihrHPL54DV3Lj1CM2mPglJPZhJDXTT6jDlPzu6oL7ZM2Gp9wwcQAeRl6M; _cc_aud=ABR4XmNgYGBInKqcDqQggJmBNbMIxGTNLARRXOV3gSQAUxcEoQ%3D%3D',
    'if-none-match': 'W/"a43-hxXAwL51kj9ckR6Knjaq6P7qNF8"',
}

class moduleUtils():
    """class name gives it away"""


    def save_bloomberg_ticker(ticker: str):
        """function to save the ticker for future financial-data-API requests. To skip the get_bloomberg_ticker() method when possible. Will be written to bloomberg_tickers.txt"""
        pass

    def get_api(url: str):
        """utils. gets and parses json-response. Yes, this is OOP hell"""
        response = requests.get(url)
        response_dict = response.json()

        return response_dict

    def check_if_already_saved(ticker: str):
        """takes bloomberg-ticker and checks, if bloomberg-search-API call is needed or ticker has been"""
        pass




class bloombergAPI():
    """core functions of the module"""


    def get_bloomberg_ticker(query: str):
        """sends GET request to bloomberg.com search API with operator "query" as query. To find non-general, specific finds, please consult list_dicts_finds output"""
        formatted_query = query.replace(" ", "%20")
        url = f"https://search.bloomberg.com/lookup.json?query={formatted_query}"
        response_dict = moduleUtils.get_api(url)
        num_finds = response_dict.get("total_results")
        first_find_unformatted = response_dict.get("results")[0]
        bloomberg_ticker = response_dict.get("results")[0].get("ticker_symbol")

        return num_finds, first_find_unformatted, bloomberg_ticker, query

    def get_bloomberg_financials(ticker: str):
        """this method takes a bloomberg-ticker to get bloomberg data-strip-API financial data. Returns dict with all the data"""
        url = f"https://www.bloomberg.com/markets2/api/datastrip/{ticker}?locale=en"
        response = requests.get(url, headers = REQUEST_HEADERS)
        response_dict = json.loads(response.text)[0]

        return response_dict



query = "peloton"


num_finds, first_find_unformatted, ticker, query = bloombergAPI.get_bloomberg_ticker(query)
response = bloombergAPI.get_bloomberg_financials(ticker)
print(response)