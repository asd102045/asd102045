# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:51:52 2020

@author: e010
"""
#==============================================================================
def collect_personal_info():
    name = input("請輸入您的姓名：")
    age = int(input("請輸入您的年齡："))
    height = float(input("請輸入您的身高（米）："))
    favorite_color = input("請輸入您喜歡的顏色：")
    
    # 將資料存儲在字典中
    personal_info = {
        "姓名": name,
        "年齡": age,
        "身高": height,
        "喜愛的顏色": favorite_color
    }
    
    return personal_info

def format_personal_info(info):
    summary = f"姓名：{info['姓名']}\n年齡：{info['年齡']} 歲\n身高：{info['身高']} 米\n喜愛的顏色：{info['喜愛的顏色']}"
    return summary

def main():
    personal_info = collect_personal_info()
    
    print("\n您的個人資料摘要如下：")
    print(format_personal_info(personal_info))

if __name__ == "__main__":
    main()

