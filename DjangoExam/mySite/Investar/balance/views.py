from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.shortcuts import render


def get_data(symbol):
    """
        symbol에 해당하는 주식에 대한 현재 가격, 등락률을 반환한다.
        
        Args:
            symbol(str): 주식의 심볼
        Returns:
            cur_price(str): 주식의 현재가
            cur_rate(str): 주식의 등락률
            stock_name(str): 주식의 이름    
    """
    url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)
    with urlopen(url) as doc:
        soup = BeautifulSoup(doc, "lxml", from_encoding="euc-kr")#BeautifulSoup : html을 파싱하는 라이브러리
        cur_price = soup.find('strong', id='_nowVal') #_nowVal : 현재가
        cur_rate = soup.find('strong', id='_rate') #_rate : 등락률
        stock = soup.find('title') #title : 주식 이름
        print(stock)
        stock_name = stock.text.split(':')[0].strip()
        print(stock_name)
        return cur_price.text, cur_rate.text.strip(), stock_name
    
def main_view(request):
    """
        사용자가 입력한 주식의 심볼과 수량에 대한 정보를 가져와서
        현재가, 등락률, 주식 이름을 조회한 후 이를 템플릿에 전달한다.
        Args:
            request(HttpRequest): HttpRequest 객체
        Returns:
            render : 템플릿(html : balance.html)에 조회한 주식 정보를 전달한다.            
    """
    #mylist = [['035420', '20'], ['005930','100']]
    querydict = request.GET.copy()
    mylist = querydict.lists()
    rows = []
    total = 0
    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0]) #get_data : 주식의 현재가, 등락률, 주식 이름을 조회
        price = cur_price.replace(',', '')
        stock_count = format(int(x[1][0]), ',')
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum, ',')
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, stock_sum])
        total = total + int(price) * int(x[1][0])
    total_amount = format(total, ',')
    values = {'rows' : rows, 'total' : total_amount}
    print(values)
    return render(request, 'balance.html', values)

#main_view()