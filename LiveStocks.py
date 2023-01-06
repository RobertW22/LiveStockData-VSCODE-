import yfinance as yf
from yahoo_fin.stock_info import *

# Welcome message
print("Welcome to the Stock Market data checker \n")

onButton = True
phase1 = True
phase2 = False



while onButton == True:

    while phase1 == True:
        print("Please select from the following functions: \n")
        #fncs
        print("1. Get Market Status")#print(get_market_status())
        print("2. Get Day Gainers")#print(get_day_gainers())
        print("3. Get Day Losers")#print(get_day_losers())
        print("4. Get Currency Market Info")#print(get_currencies())
        print("5. Info on an individual stock\n")
        print("6. Exit\n")

        choice = input()

        if(choice == "1"):
            print(get_market_status())
            xx = input("Press Enter to return...")
        elif(choice == "2"):
            print(get_day_gainers())
            xx = input("Press Enter to return...")
        elif(choice == "3"):
            print(get_day_losers())
            xx = input("Press Enter to return...")
        elif(choice == "4"):
            print(get_currencies())
            xx = input("Press Enter to return...")
        elif(choice == "5"):
            phase1 = False
            print("Please enter the stock ticker symbol you would like to check: ")
            x = input()
            phase2 = True
        
        elif(choice == "6"):
            print("Goodbye :)")
            onButton = False
            exit()
            
        
            


    while phase2 == True:
        if(choice == "5"):
            
            print("What data would you like to see from: " + x )
            
            
            
            #List of options
            print("1. Get Live Price") #print(get_live_price(x))
            print("2. Get price data / volume") #print(get_data(x))
            print("3. Analyst Price Target") #yf.Ticker(x).analyst_price_target
            print("4. Dividends") #yf.Ticker(x).dividends
            print("5. Earnings") #yf.Ticker(x).earnings
            print("6. Financials") #yf.Ticker(x).financials
            
            print("7. Return to main menu") #yf.Ticker(x).balance_sheet
            
            choice2 = input()
            
            if(choice2 == "1"):
                print(get_live_price(x))
                xx = input("Press Enter to return...")
            elif(choice2 == "2"):
                print(get_data(x))
                xx = input("Press Enter to return...")
            elif(choice2 == "3"):
                print(yf.Ticker(x).analyst_price_target)
                xx = input("Press Enter to return...")
            elif(choice2 == "4"):
                print(yf.Ticker(x).dividends)
                xx = input("Press Enter to return...")
            elif(choice2 == "5"):
                print(yf.Ticker(x).earnings)
                xx = input("Press Enter to return...")
            elif(choice2 == "6"):
                print(yf.Ticker(x).financials)
                xx = input("Press Enter to return...")
            elif(choice2 == "7"):
                phase2 = False
                phase1 = True
                print("Returning to main menu...")
        
        
    
        
        
        
        




















