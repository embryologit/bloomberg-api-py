import requests

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
        list_finds = response_dict.get("results")
        first_find_unformatted = response_dict.get("results")[0]
        bloomberg_ticker = response_dict.get("results")[0].get("ticker")

        return num_finds, list_dicts_finds, bloomberg_ticker, query

    def get_bloomberg_financials(ticker: str):
        """this method takes a bloomberg-ticker to get bloomberg data-strip-API financial data."""
        url = f"https://www.bloomberg.com/markets2/api/datastrip/{tickre}?locale=en"
        response_dict = moduleUtils.get_api(url)[0]
        #not done. Left off here...
