#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" PyHighcharts: examples.py
Basic Examples 
"""
import math
import random
import simplejson as json

from PyHighcharts.highcharts.chart import Highchart


EXAMPLE_CONFIG = {
    "lang" :{
        "contextButtonTitle": '图片操作',
        "decimalPoint":'.',
        "downloadJPEG": '下载JPEG',
        "downloadPDF" : '下载PDF',
        "downloadPNG" : '下载PNG',
        "downloadSVG" : '下载SVG',
        "drillUpText" : '返回{series.name}',
        "loading"     : '正在加载...',
        "months"      :  ['一月','二月','三月','四月','五月','六月','七月',
            '八月','九月','十月','十一月','十二月'],
        "noData"      :  '没有数据显示',
        "numericSymbols" : [ "k" , "M" , "G" , "T" , "P" , "E"],
        "printChart"  : '打印图片',
        "resetZoom"   : '缩放重置',
        "resetZoomTitle" : '缩放重置为1:1',
        "shortMonths" : ['一月','二月','三月','四月','五月','六月','七月',
            '八月','九月','十月','十一月','十二月'],
        "weekdays"    : ['星期日','星期一','星期二','星期三','星期四',
            '星期五','星期六']
    },
    "credits": {
        "href" : "/",
        "text" : "youja.cn"
    },
    "xAxis": {
        "gridLineWidth": 0,
        "lineWidth": 0,
        "tickLength": 0,
    },
    "yAxis": {
            "gridLineWidth": 0,
    }
}

def pie_example():
    """ Basic Piechart Example """
    chart = Highchart()
    chart.title("Pac Man Highchart")
    chart.add_data_set([["Does Not Resemble Pac Man", 25],
        ["Resembes Pac Man", 75]],
        series_type="pie",
        name="",
        startAngle=45)
    chart.colors(["#99CCFF", "#FFFF66"])
    chart.set_options(EXAMPLE_CONFIG)
    chart.show()


def spline_example():
    """ Basic Spline Example """
    chart = Highchart()
    data = [math.sin(x/100.0) \
        for x in range(0, int(4*math.pi*100), int(math.pi/16*100))]
    chart.title("Sin Spline")
    chart.add_data_set(data, series_type="spline", name="Sin")
    chart.set_options(EXAMPLE_CONFIG)
    chart.show()


def area_example():
    """ Basic Area Exampls """
    chart = Highchart()
    data = [i**2 for i in range(10)]
    chart.title("Area Example")
    chart.add_data_set(data, series_type="area", name="Area")
    chart.set_options(EXAMPLE_CONFIG)
    chart.show()


def multiple_example():
    """ Basic Multiple Exampls """
    chart = Highchart()
    revenue = [random.randint(1000, 7000) for i in range(24)]
    spend = [random.randint(2000, 4000) for i in range(24)]
    profit = [r - spend[i] for i, r in enumerate(revenue)]
    cumulative_profit = [sum(profit[:i])+5000 for i in range(len(profit))]
    chart.title("Multiple Example")
    chart.add_data_set(revenue, series_type="line", name="Revenue", index=2)
    chart.add_data_set(spend, series_type="line", name="Spend", index=3)
    chart.add_data_set(cumulative_profit, 
        series_type="area", 
        name="Balance",
        index=1)
    chart.set_options(EXAMPLE_CONFIG)
    chart.show()


def dau_line_example():
    """ Basic line Example """
    chart = Highchart()
    chart.set_options(EXAMPLE_CONFIG)
    chart.update_yAxis(title_text="活跃人数 (人)")
    chart.update_xAxis(categories=['+0','+1','+2','+3','+4','+5','+6','+7','+8','+9','+10','+11','+12'])
    chart.title("活跃用户留存(2014-07-09~2014-07-22)")
    chart.add_data_set([['2014-07-09',223961],['2014-07-10',150964],['2014-07-11',134088],['2014-07-12',119318],
                        ['2014-07-13',110857], ['2014-07-14',109625],['2014-07-15',104971],['2014-07-16',100415],
                        ['2014-07-17',96143],['2014-07-18',95523],['2014-07-19',88619]],  series_type="line", name="2014-07-09")
    chart.add_data_set([['2014-07-10',243910],
                                    ['2014-07-11',161951],
                                    ['2014-07-12',133382],
                                    ['2014-07-13',121328],
                                    ['2014-07-14',122070],
                                    ['2014-07-15',115963],
                                    ['2014-07-16',110135],
                                    ['2014-07-17',104766],
                                    ['2014-07-18',105800],
                                    ['2014-07-19',95100]],  series_type="line", name="2014-07-10")

    json_data = json.dumps(chart.__export_json_options__(),ensure_ascii=False)

    # json_data =chart.__export_json_options__()

    chart.show()


if __name__ == '__main__':
    dau_line_example()