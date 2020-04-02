import pandas as pd
'''
df = pd.read_excel(r'C:\\Users\\312642\\Desktop\\Automation\\DLRefresh\\DL\\DLrefreshInput.xls')
'''
data = pd.read_excel(r'/home/sautotest/DL/DLrefreshInput.xls')
result = pd.DataFrame(data, columns=['Employee ID'])
print(result)

