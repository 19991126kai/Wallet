class Wallet:
    def __init__(self,money = 0):
        self.money = money

    def show_money(self):
        print('残高：{:,d}'.format(self.money) + '円\n')

    def money_plus(self,plus):
        if plus > 0:
            self.money += plus
            print('{:,d}'.format(plus) + '円入れました。')
        else:
            print('1円以上で入れて下さい。({:,d}'.format(plus) + '円)')
        
    def money_minus(self,minus):
        kinsyu = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
        if minus < self.money:
            self.money -= minus
            print('{:,d}'.format(minus) + '円出しました。')
            for i in range(0, len(kinsyu)):
                maisu = minus // kinsyu[i]
                if maisu > 0:
                    print('{:,d}'.format(kinsyu[i]) + '円x' + '{:,d}'.format(maisu), end=' ')
                    minus -= (kinsyu[i] * maisu)
            print('')

        else:
            print('残高より多くは出せません。({:,d}'.format(minus) + '円)')

# main
w = Wallet(10000) #財布の中身(初期設定10,000円)
w.show_money() #残高照会

w.money_plus(5000) #5,000円入れる
w.show_money() #残高照会

w.money_minus(6988) #6,988円出す(丁度出すのに必要な紙幣・硬貨の枚数を算出)
w.show_money() #残高照会
