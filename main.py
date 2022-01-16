import requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    url_1 = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD&api_key={8c9268efb236eadda131471062bf662c5370c75a580fc659fc305d2540f48e34} "

    response_1 = requests.request("GET", url_1)

    json_1 = response_1.json()

    raw_data = (json_1['RAW'])

    btc_data = (raw_data['BTC'])

    btc_usd = (btc_data['USD'])

    btc_price = (btc_usd['PRICE'])

    btc_price_str = str(btc_price)

    eth_data = (raw_data['ETH'])

    eth_usd = (eth_data['USD'])

    eth_price = (eth_usd['PRICE'])

    eth_price_str = str(eth_price)

    now = datetime.now()

    today =('%04d-%02d-%02d' %(now.year, now.month, now.day))
    updated =('%04d-%02d-%02d %02d:%02d:%02d' %(now.year, now.month, now.day, now.hour, now.minute, now.second))


    if now.year == 2022:
        url_2 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts=1640995260&api_key={31112ee7cd727c3df5e945c1470830d08c90bf4e8d180427a68ed16f0d873e9c}"
        url_3 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=ETH&tsyms=USD&ts=1640995260&api_key={31112ee7cd727c3df5e945c1470830d08c90bf4e8d180427a68ed16f0d873e9c}"

        response_2 = requests.request("GET", url_2)
        response_3 = requests.request("GET", url_3)

        json_2 = response_2.json()
        json_3 = response_3.json()

    elif now.year == 2023:
        url_2 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts=1672531260&api_key={31112ee7cd727c3df5e945c1470830d08c90bf4e8d180427a68ed16f0d873e9c}"
        url_3 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=ETH&tsyms=USD&ts=1672531260&api_key={31112ee7cd727c3df5e945c1470830d08c90bf4e8d180427a68ed16f0d873e9c}"

        response_2 = requests.request("GET", url_2)
        response_3 = requests.request("GET", url_3)

        json_2 = response_2.json()
        json_3 = response_3.json()

    btc_h1 = json_2['BTC']
    btc_open = btc_h1['USD']

    eth_h1 = json_3['ETH']
    eth_open = eth_h1['USD']

    btc_open_str = str(btc_open)
    eth_open_str = str(eth_open)

    btc_precent = ((btc_price - btc_open) / btc_open) * 100
    eth_precent = ((eth_price - eth_open) / eth_open) * 100

    btc_rounded = str(round(btc_precent, 2))
    eth_rounded = str(round(eth_precent, 2))

    def days_between(d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)

    day = days_between("2022-01-01",today)

    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    numbers = [ordinal(n) for n in range(1,366)]

    this_day =numbers[day ]

    if now.day == 1 and now.month == 1:
        this_day = "1st"


    #btc_eth_up = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up: %s%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up:  %s%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_rounded,eth_open_str,eth_price_str,eth_rounded)

    #btc_up_eth_down = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up: %s%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %s%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_rounded,eth_open_str,eth_price_str,eth_rounded)

    #btc_down_eth_down = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %s%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %s%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_rounded,eth_open_str,eth_price_str,eth_rounded)

    #btc_down_eth_up = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %s%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up: %s%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_rounded,eth_open_str,eth_price_str,eth_rounded)

    day =("It is %s day of %d") %(this_day,now.year)
    btc_open_p = "⬅️ Year open price: $%s" %(btc_open_str)
    btc_now = "➡️ Current price: $%s" %(btc_price_str)
    btc_up = "📈 Up: %s%%" %(btc_rounded)
    btc_down = "📉 Down: %s%%" %(btc_rounded)
    eth_open_p = "⬅️ Year open price: $%s" %(eth_open_str)
    eth_now = "➡️ Current price: $%s" %(eth_price_str)
    eth_up = "📈 Up: %s%%" %(eth_rounded)
    eth_down = "📉 Down: %s%%" %(eth_rounded)

    if btc_precent > 0 and eth_precent > 0:
        return render_template('index.html',
        day=day,
        btc_open_p=btc_open_p,
        btc_now=btc_now,
        btc_up_down=btc_up,
        eth_open_p=eth_open_p,
        eth_now=eth_now,
        eth_up_down=eth_up,
        updated=updated
        )
    elif btc_precent > 0 and eth_precent < 0:
        return render_template('index.html',
        day=day,
        btc_open_p=btc_open_p,
        btc_now=btc_now,
        btc_up_down=btc_up,
        eth_open_p=eth_open_p,
        eth_now=eth_now,
        eth_up_down=eth_down,
        updated=updated
        )
    elif btc_precent < 0 and eth_precent < 0:
        return render_template('index.html',
        day=day,
        btc_open_p=btc_open_p,
        btc_now=btc_now,
        btc_up_down=btc_down,
        eth_open_p=eth_open_p,
        eth_now=eth_now,
        eth_up_down=eth_down,
        updated=updated
        )
    elif btc_precent < 0 and eth_precent > 0:
        return render_template('index.html',
        day=day,
        btc_open_p=btc_open_p,
        btc_now=btc_now,
        btc_up_down=btc_down,
        eth_open_p=eth_open_p,
        eth_now=eth_now,
        eth_up_down=eth_up,
        updated=updated
        )

    #return '<p>{}</p> <p>Bitcoin</p> <p>{}</p> <p>{}</p> <p>{}</p> <p> Ethereum </p>  <p>{}</p> <p>{}</p> <p>{}</p>'.format(day,btc_open_p,btc_now,btc_down,eth_open_p,eth_now,eth_up)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
