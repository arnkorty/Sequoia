# -*- encoding: UTF-8 -*-

import process
import strategy.enter as enter
import strategy.low_atr as low_atr
import utils


def strategy(end_date=None):
    def end_date_filter(code_name):
        stock = code_name[0]
        name = code_name[1]
        data = utils.read_data(stock, name)
        if data is None:
            return False
        return \
            enter.check_ma(stock, data, end_date=end_date) \
            and enter.check_max_price(stock, data, end_date=end_date) \
            and enter.check_volume(code_name, data, end_date=end_date)
    # low_atr.check_low_increase(stock, data)
    return end_date_filter


process.run()
print("数据更新完毕！")
stocks = utils.get_stocks()

m_filter = strategy(end_date=None)

results = list(filter(m_filter, stocks))
print(results)



