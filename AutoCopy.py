import PyPDF2
import xlwings as xw

year = input("第幾次國考")

dict{
    'Hema' : 80;
    ''
}

def CollectQuestion(year):
    reader = PyPDF2.PdfReader(year+'-Hema-Q.pdf')
    Data = ""
    Pages = len(reader.pages)
    for i in range(Pages):
        x = str(reader.pages[i].extract_text())
        Data += x
    return Data

def ProcessQuestion(Data):  
    Header = Data.find("最適當答案。") + 9
    Whole_Test = Data[Header:]
    List = []
    for i in range(80):
        n1 = Whole_Test.find("\n"+str(i+1)+".")
        n2 = Whole_Test.find("\n"+str(i+2)+".")
        n3 = Whole_Test.find("\n"+str(i+3)+".")
        if Whole_Test[n2:n3] == "":
            n2 = Whole_Test.find(str(i+2)+".")
        elif Whole_Test[n1:n2] == "":
            n1 = Whole_Test.find(str(i+1)+".")
        else:
            pass
        List.append(Whole_Test[n1:n2-1])
    return List

def ProcessAnswer(year):
    Ans_reader = PyPDF2.PdfReader(year+'-Hema-A.pdf')
    Text = Ans_reader.pages[0].extract_text()
    Header1 = Text.find("題號")
    Header2 = Text.find("\n備")
    Data1 = Text[Header1-1:Header2]
    Data1 = Data1.replace("\n題號\n答案", "")
    return Data1

def ConstructData(List, Data1):
    wb = xw.Book('Data.xlsx')
    sheet = wb.sheets('Hema')
    for i in range(80):
        col = i + 2
        sheet['A' + str(col)].value = List[i]
        sheet['B' + str(col)].value = Data1[i]
        sheet['C' + str(col)].value = year 


ConstructData(ProcessQuestion(CollectQuestion(year)),ProcessAnswer(year))
