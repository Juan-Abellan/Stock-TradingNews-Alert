import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_phone_number = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_KEY = ""
NEWS_KEY = ""

parameters_stock = {
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
    "apikey": ALPHA_KEY,
    "interval": "60min"
}

parameters_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_KEY
}

request_stock = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
data_stock = request_stock.json()['Time Series (Daily)']

# for index, key in enumerate(data_stock):
#     print(f"""
# {index}: {key =} | {type(data_stock[key]) = }
#     {data_stock[key] = }""")
#     for index2, key2 in enumerate(data_stock[key]):
#         print(f"""
#     {index}.{index2}: {key2 = } | {type(data_stock[key][key2]) = }
#         {data_stock[key][key2] = }
#     """)

data_list = [float(value['4. close']) for (key, value) in data_stock.items()][:2:]
positive_difference = abs(data_list[0] - data_list[1])
positive_difference_percentage = round((positive_difference / data_list[0]) * 100, 2)

request_news = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
data_news = request_news.json()

# for index, key in enumerate(data_news):
#     print(f"""
# {index}: {key =} | {type(data_news[key]) = }
#     {data_news[key] = }""")
#     if type(data_news[key]) == list:
#         for index2, new in enumerate(data_news[key][:3:]):
#             print(f"""
# {index}.{index2}: {new = }
# -------------------------------------------------------------------------------------------------------------------""")
#             for index3, key3 in enumerate(new):
#                 print(f"""
#            {index}.{index2} {index3}: {key3 =} | {type(new[key3]) = }
#                 {new[key3] = }""")
three_articles_list = data_news["articles"][:3:]

if positive_difference_percentage > 5:
    print("get news")
    three_articles_list = data_news["articles"][:3:]
    numbers_to_send = {"Amigo": "+4915731565739",
                       }
    client = Client(account_sid, auth_token)
    for receiver in numbers_to_send:
        message = client.messages.create(
            body=f"""
1: {three_articles_list[0]['title']}
{three_articles_list[0]['description']}
......................
2: {three_articles_list[1]['title']}
{three_articles_list[1]['description']}
......................
3: {three_articles_list[2]['title']}
{three_articles_list[2]['description']}
""",
            from_=twilio_phone_number,
            to=numbers_to_send[receiver]
        )

# print(f"""
# TODOS ..............................................................................................................
# {request_stock = }
# {type(request_stock) = }
#
# {data_stock = }
# {type(data_stock) = }
#
# {data_list = }
#
# {positive_difference = }
#
# {positive_difference_percentage = }
#
# {"Get news! "if positive_difference_percentage > 0.5 else "No need to get news!" = }
# -------------------------------------------------------------------------------------------------------------------
# {request_news = }
# {type(request_news) = }
#
# {data_news = }
# {type(data_news) = }
#
# {type(three_articles_list) =}  | {len(three_articles_list) = }
# {three_articles_list = }
# TODOS ..............................................................................................................
# """)
