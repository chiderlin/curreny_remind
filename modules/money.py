import pandas as pd

class Money(object):
    def __init__(self,currency,currency_ch,cash_in,cash_out,sign_in,sign_out): #初始狀態，基本資訊
        self.currency = currency
        self.currency_ch = currency_ch
        self.cash_in = cash_in
        self.cash_out = cash_out
        self.sign_in = sign_in
        self.sign_out = sign_out

    @staticmethod 
    def search_data():
        data = pd.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")[0]
        currency_table = data.iloc[:,0:5] # 把ix改成iloc [取全部rows,取五columns]
        currency_table.columns = ["幣別","現金匯率-買入","現金匯率-賣出","即期匯率-買入","即期匯率-賣出",] #更改title
        currency_ch = currency_table["幣別"].str.extract("(\w+)") #extract提取要的字, #中文字元
        currency_table["幣別"] = currency_table["幣別"].str.extract("\((\w+)\)") # 後面接正規化, w指所有字元
        # print(currency_table.values[0]) # 第一row的資料
        # print(currency_ch) # 幣別中文資料
        moneydict = {}
        position = {}
        for i in range(0,19): # total 18行data
            dollar = currency_table.values[i] # 每行資料存dollar
                           # Money class像是一個外框，在這裡才被灌入實質內容
            moneydict[i] = Money(dollar[0],currency_ch.values[i][0],dollar[1],dollar[2],dollar[3],dollar[4]) #建key
            position[currency_ch.values[i][0]] = i
        return moneydict, position

# moneydict, position = Money.search_data()
# print(position)
# print(moneydict)
# for i in range(0,19):
#     print(moneydict[i].currency)
#     print(moneydict[i].currency_ch)
#     print(moneydict[i].cash_in)
#     print(moneydict[i].cash_out)
#     print(moneydict[i].sign_in)
#     print(moneydict[i].sign_out)
#     print('--------------------')
    