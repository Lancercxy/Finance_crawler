# 导入requests库
import requests
 
# 导入正则表达式所需要用到的库re
import re
 
# 导入数据分析所用到的库pandas
import pandas as pd
 
# 导入matplotlib
import matplotlib.pyplot as plt
 
# 利用time实现暂停打印信息
import time
 
# numpy
import numpy as np
 
# 写入cookie信息
cookies = {
    # 即为页面中分析时'qgqp_b_id'对应的值
    'qgqp_b_id': '02d480cce140d4a420a0df6b307a945c',
 
    # 即为页面中分析时'cowCookie'对应的值
    'cowCookie': 'true',
 
    # 即为页面中分析时'em_hq_fls'对应的值
    'em_hq_fls': 'js',
 
    # 即为页面中分析时'intellpositionL'对应的值
    'intellpositionL': '1168.61px',
 
    # 即为页面中分析时'HAList'对应的值
    'HAList': 'a-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-000001-%u5E73%u5B89%u94F6%u884C',
 
    # 即为页面中分析时'st_si'对应的值
    'st_si': '07441051579204',
 
    # 即为页面中分析时'st_asi'对应的值
    'st_asi': 'delete',
 
    # 即为页面中分析时'st_pvi'对应的值
    'st_pvi': '34234318767565',
 
    # 即为页面中分析时'st_sp'对应的值
    'st_sp': '2021-09-28%2010%3A43%3A13',
 
    # 即为页面中分析时'st_inirUrls'对应的值
    'st_inirUrl': 'http%3A%2F%2Fdata.eastmoney.com%2F',
 
    # 即为页面中分析时'st_sn'对应的值
    'st_sn': '31',
 
    # 即为页面中分析时'st_psi'对应的值
    'st_psi': '20211020210419860-113300300813-5631892871',
 
    # 即为页面中分析时'intellpositionT'对应的值
    'intellpositionT': '1007.88px',
}

# 配置头文件
headers = {
 
    # 即为页面中分析时'Connection'对应的值
    'Connection': 'keep-alive',
 
    # 即为页面中分析时'User-Agent'对应的值
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
 
    # 即为页面中分析时'DNT'对应的值
    'DNT': '1',
 
    # 即为页面中分析时'Accept'对应的值
    'Accept': '*/*',
 
    # 即为页面中分析时'Referer'对应的值
    'Referer': 'http://quote.eastmoney.com/',
 
    # 即为页面中分析时'Accept-Language'对应的值
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
 
# 所有信息等待存入放入列表
all_message = []

#清洗数据函数
def clean_data(response):
    # 获取股票代码
        daimas = re.findall('"f12":(.*?),', response)
 
        # 获取股票名称
        names = re.findall('"f14":"(.*?)"', response)
 
        # 获取最新价
        zuixinjias = re.findall('"f2":(.*?),', response)
 
        # 获取涨跌幅
        zhangdiefus = re.findall('"f3":(.*?),', response)
 
        # 获取涨跌额
        zhangdiees = re.findall('"f4":(.*?),', response)
 
        # 获取成交量
        chengjiaoliangs = re.findall('"f5":(.*?),', response)
 
        # 获取成交额
        chengjiaoes = re.findall('"f6":(.*?),', response)
 
        # 获取振幅
        zhenfus = re.findall('"f7":(.*?),', response)
 
        # 获取今日最高点
        zuigaos = re.findall('"f15":(.*?),', response)
 
        # 获取今日最低点
        zuidis = re.findall('"f16":(.*?),', response)
 
        # 获取今日开盘价格
        jinkais = re.findall('"f17":(.*?),', response)
 
        # 获取昨日收盘价格
        zuoshous = re.findall('"f18":(.*?),', response)
 
        # 获取量比
        liangbis = re.findall('"f10":(.*?),', response)
 
        # 获取换手率
        huanshoulvs = re.findall('"f8":(.*?),', response)
 
        # 获取市盈率
        shiyinglvs = re.findall('"f9":(.*?),', response)
 
        # 获取市净率
        shijinglvs = re.findall('"f23":(.*?),', response)
        
        # 将不同股票信息写入字典
        for i in range(len(daimas)):
 
            dict = {
                # 获取对应股票代码
                "代码": daimas[i],
 
                # 获取对应股票名称
                "名称": names[i],
 
                # 获取对应股票最新价
                "最新价":zuixinjias[i],
 
                # 获取对应股票涨跌幅
                "涨跌幅":zhangdiefus[i],
 
                # 获取对应股票涨跌额
                "涨跌额":zhangdiees[i],
 
                # 获取对应股票成交量
                "成交量":chengjiaoliangs[i],
 
                # 获取对应股票成交额
                "成交额":chengjiaoes[i],
 
                # # 获取对应股票振幅
                "振幅":zhenfus[i],
 
                # 获取对应股票最高点
                "最高":zuigaos[i],
 
                # 获取对应股票最低点
                "最低":zuidis[i],
 
                # 获取对应股票开盘价格
                "今开":jinkais[i],
 
                # 获取对应股票昨日收盘价格
                "昨收":zuoshous[i],
 
                # 获取对应股票量比
                "量比":liangbis[i],
 
                # 获取对应股票最换手率
                "换手率":huanshoulvs[i],
 
                # 获取对应股票市盈率(动态)
                "市盈率(动态)":shiyinglvs[i],
 
                # 获取对应股票市净率
                "市净率":shijinglvs[i]
            }
 
            # 打印字典信息
            # print(dict)
 
            # 把一支股票的所有信息以字典的形式存入列表
            all_message.append(dict)

#爬取数据函数
def crawl_data(Lower,upper):
    # 总共爬取网页上244页的内容
    for page in range(Lower,upper):
        
        params = (
            # 解析到的URL中对应的cb参数
            ('cb', 'jQuery1124031167968836399784_1615878909521'),
            # 解析到的URL中对应的pn参数
            ('pn', str(page)),
            # 解析到的URL中对应的pz参数
            ('pz', '20'),
            # 解析到的URL中对应的po参数
            ('po', '1'),
            # 解析到的URL中对应的np参数
            ('np', '1'),
            # 解析到的URL中对应的ut参数
            ('ut', 'bd1d9ddb04089700cf9c27f6f7426281'),
            # 解析到的URL中对应的fltt参数
            ('fltt', '2'),
            # 解析到的URL中对应的invt参数
            ('invt', '2'),
            # 解析到的URL中对应的fid参数
            ('fid', 'f3'),
            # 解析到的URL中对应的fs参数
            ('fs', 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048'),
            # 解析到的URL中对应的fields参数
            ('fields', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'),
        )

        # 对当前页数发送请求
        response = requests.get('http://67.push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params,
                                cookies=cookies, verify=False)

        # 打印请求结果
        # print(response.text)
        response = response.text
        # time.sleep(100)
        clean_data(response)

def Visualization():
    df = pd.read_csv("东方财富.csv")
    # if (Order=='1'): Order = True
    # else:Order = False
    #print(Order)
    df_sort = df.sort_values(by='涨跌幅', ascending=False)
    new_df = df_sort.head(10)
    # pd_cje = new_df['最新价'].tolist()
    fig = plt.figure(figsize=(16,8))
    x = new_df['名称']
    y = new_df['最新价']
    z = new_df['涨跌幅']
    plt.title('最新价/涨跌幅')
    plt.xlabel('股票名',size=13)
    plt.ylabel('股价',size=13)
    #plt.zlabel('评价人数')
    ax1 = fig.add_subplot(111)
    #plt.xticks(rotation=60)
    width = 0.4
    plt.xticks(np.arange(len(x)), x)
    rects = ax1.bar(np.arange(len(x))-width/2, y,width=width,label=u'股价',color='r')
    plt.legend(loc=6)
    for rect in rects:
        rect_x = rect.get_x()
        rect_y = rect.get_height()
        plt.text(rect_x+width/2, rect_y+0.05, str(rect_y)+'元', ha='center')
    ax2 = ax1.twinx()
    rects2 = ax2.bar(np.arange(len(x))+width/2, z,width=width,label=u'涨跌幅')
    plt.legend(loc=5)
    for rect in rects2:
        rect_x = rect.get_x()
        rect_y = rect.get_height()
        plt.text(rect_x+width/2, rect_y+0.05, str(rect_y)+'%', ha='center')
    plt.show()
    
    
def abc():
    df = pd.read_csv("东方财富.csv")
    # 绘制散点图并拟合
    # df_sort = df.sort_values(by='成交量', ascending=False)
    # df = df_sort.head(100)
    
    my_y = df['涨跌幅']
    
    my_x = df['换手率']
    
    
    # 用4次多项式拟合
    # z1 = np.polyfit(my_x, my_y, 4)
    # p1 = np.poly1d(z1)
    
    # 也可以使用yvals=np.polyval(z1,x)
    # yvals=p1(my_x)
    
    # 绘制散点和曲线
    plot1=plt.plot(my_x, my_y, '*',label='original values')
    # plot2=plt.plot(my_x, yvals, 'r',label='polyfit values')
    
    # 图标
    plt.ylabel('涨跌幅')
    plt.xlabel('换手率')
    
    # 标题
    plt.title('polyfitting')
    
    # 展示
    plt.show()

if __name__ =='__main__':
    
    # Lower = int(input("请输入开始爬取的页码："))
    # Upper = int(input("请输入需要爬取的页数："))
    # crawl_data(Lower, Upper+1)
    # # 打印所有股票构成的列表
    # # print(all_message)
 
    # # 将其存储为pandas格式
    # result_pd = pd.DataFrame(all_message)
    # print(type(result_pd))
    # # 做本地化保存
    # result_pd.to_csv("东方财富.csv")
 
 
    # 数据清洗和处理时我们选择涨幅最高的100支股票进行后续分析
    
    # 读取本地CSV
    # df = pd.read_csv("东方财富.csv")
    
    # Visualization()
    abc()
    # 根据涨幅进行排序
    # df_sort = df.sort_values(by='涨跌幅', ascending=False)
    
    # # 打印排序结果
    # print(df_sort)
    #
    # # 打印排序后原始数据长度
    # print(len(df_sort))
    
    # 对排序后的数据取前100行
    # new_df = df_sort.head(100)
    
    # # 打印原始数据清洗与筛选后的
    # print(df_sort)
    #
    # # 打印筛选后的长度
    # print(len(new_df))
    
    # 画图
    # 主要利用matplotlib和pandas自带的画图功能
    
    # 绘制涨幅最高的100支股票最新价折线图
    # pd_cje = new_df['最新价'].tolist()
    
    # 打印结果
    # print(pd_cje)
    
    # 打印是否转换成列表
    # print(type(pd_cje))
    
    # # 设置x刻度
    # my_x_ticks = np.arange(0, 101, 5)
    
    # # 设置y刻度
    # my_y_ticks = np.arange(0, 401, 5)
    
    # # 配置x刻度
    # plt.xticks(my_x_ticks)
    
    # # 配置y刻度
    # plt.yticks(my_y_ticks)
    
    # # 画图
    # plt.plot(range(len(pd_cje)), pd_cje)
    
    # # 展示
    # plt.show()
    
    
 
 
 
# # 绘制散点图并拟合
# my_y = new_df['换手率'].tolist()
 
# my_x = [i for i in range(len(my_y))]
 
 
# # 用4次多项式拟合
# z1 = np.polyfit(my_x, my_y, 4)
# p1 = np.poly1d(z1)
 
# # 也可以使用yvals=np.polyval(z1,x)
# yvals=p1(my_x)
 
# # 绘制散点和曲线
# plot1=plt.plot(my_x, my_y, '*',label='original values')
# plot2=plt.plot(my_x, yvals, 'r',label='polyfit values')
 
# # 图标
# plt.xlabel('x axis')
# plt.ylabel('y axis')
 
# # 标题
# plt.title('polyfitting')
 
# # 展示
# plt.show()