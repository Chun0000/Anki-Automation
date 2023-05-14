import PyPDF2 # import PyPDF2 module
import xlwings as xw # import xlwings module
import pandas as pd # import pandas module

'''
1. 本程式碼用於將國考血液學試題 PDF(112-1-Hema-Q)轉換成 Excel 檔案
2. 每題會對應到一個標準答案(112-1-Hema-A)
3. 答案的後面會標記年份
4. Excel 檔可以輸出成 CSV 檔，直接加入 anki
'''

year = 112-1 # 定義國考年份

def CollectQuestion(year): # 定義函數回傳整份試題為字串
    reader = PyPDF2.PdfReader(year+'-Hema-Q.pdf') # 讀取 PDF 檔案
    Data = "" # 定義空字串
    Pages = len(reader.pages) # 計算頁數
    for i in range(Pages):
        x = str(reader.pages[i].extract_text()) # 將每頁的文字轉成字串
        Data += x # 將每頁的文字串接起來
    return Data # 回傳字串

def ProcessQuestion(Data):  # 定義函數回傳整份試題為 List
    Header = Data.find("最適當答案。") + 9 # 定義 Header 為最適當答案。的位置（刪除前面非題目部分）
    Whole_Test = Data[Header:] # 定義 Whole_Test 為刪除 Header 後的字串
    List = [] # 定義空 List
    for i in range(80): # 80 題迴圈
        n1 = Whole_Test.find("\n"+str(i+1)+".") # 定義 n1 為題號的位置（尋找 "\n1."）
        n2 = Whole_Test.find("\n"+str(i+2)+".") # 定義 n2 為下一題題號的位置（尋找 "\n2."）
        n3 = Whole_Test.find("\n"+str(i+3)+".") # 定義 n3 為下下一題題號的位置（尋找 "\n3."）
        if Whole_Test[n2:n3] == "": # 如果 n2 到 n3 之間沒有文字
            n2 = Whole_Test.find(str(i+2)+".") # n2 為下一題題號的位置（尋找 "2."）
        elif Whole_Test[n1:n2] == "": # 如果 n1 到 n2 之間沒有文字
            n1 = Whole_Test.find(str(i+1)+".") # n1 為題號的位置（尋找 "1."）
        else:
            pass # 否則不做事
        List.append(Whole_Test[n1:n2-1]) # 將題目加入 List（每個元素是一題）
    return List

def ProcessAnswer(year): # 定義函數回傳整份答案為 List
    Ans_reader = PyPDF2.PdfReader(year+'-Hema-A.pdf') # 讀取 PDF 檔案
    Text = Ans_reader.pages[0].extract_text()  # 將每頁的文字轉成字串
    Header1 = Text.find("題號") # 定義 Header1 為 "題號" 的位置
    Header2 = Text.find("\n備") # 定義 Header2 為 "\n備" 的位置
    Data1 = Text[Header1-1:Header2] # 定義 Data1 為刪除 Header1 前和 Header2 後的字串（中間答案）
    Data1 = Data1.replace("\n題號\n答案", "") # 刪除 "\n題號\n答案"
    return Data1 # 回傳字串

def ConstructData(List, Data1): # 定義函數將 List 和 Data1 輸出成 Excel 檔
    wb = xw.Book('Data.xlsx') # 開啟 Excel 檔案
    sheet = wb.sheets('Hema') # 開啟 Excel 檔案中的 Hema 工作表
    for i in range(80): # 80 題迴圈
        col = i + 2 # 定義 col 為第幾列
        sheet['A' + str(col)].value = List[i] # 將題目加入 Excel 檔案
        sheet['B' + str(col)].value = Data1[i] # 將答案加入 Excel 檔案
        sheet['C' + str(col)].value = year # 將年份加入 Excel 檔案

ConstructData(ProcessQuestion(CollectQuestion(year)),ProcessAnswer(year)) # 執行函數
