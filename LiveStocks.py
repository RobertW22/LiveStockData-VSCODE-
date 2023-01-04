import yfinance as yf
from yahoo_fin.stock_info import *

# Welcome message
print("Welcome to the Stock Market data checker \n")




print("Please select from the following functions: \n")
#fncs
print("1. Get Market Status")#print(get_market_status())
print("2. Get Day Gainers")#print(get_day_gainers())
print("3. Get Day Losers")#print(get_day_losers())
print("4. Get Currency Market Info")#print(get_currencies())
print("5. Get Top Crypto\n")#print(get_top_crypto())
print("6. Info on an individual stock\n")
print("7. Exit\n")

choice = input()

if(choice == "1"):
    print(get_market_status())
elif(choice == "2"):
    print(get_day_gainers())
elif(choice == "3"):
    print(get_day_losers())
elif(choice == "4"):
    print(get_currencies())
elif(choice == "5"):
    print(get_top_crypto())
elif(choice == "6"):
    print("Please enter the stock ticker symbol you would like to check: ")
    ticker = input()
elif(choice == "7"):
    print("Goodbye :)")
    exit()
        
    



if(choice == 6):
    print("Please enter the stock ticker symbol you would like to check \n")
    #Get ticker symbol
    x = input()
    print("What data would you like to see from: " + x)

    #List of options
    print("Get Live Price") #print(get_live_price(x))
    print("Get price data / volume") #print(get_data(x))
    print("1. Analyst Price Target") #yf.Ticker(x).analyst_price_target
    print("2. Dividends") #yf.Ticker(x).dividends
    print("3. Earnings") #yf.Ticker(x).earnings
    print("4. Financials") #yf.Ticker(x).financials






















