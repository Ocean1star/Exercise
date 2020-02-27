infoDict={}
code_list = ["600000","55555"]
name_list = ["水水水水水水水","fsdfssfsdf"]
new_price_list=["112","332"]
ye_price_list = ["110","333"]

for i in range(len(code_list)):
    print(code_list[i])
    infoDict[code_list[i]]=[name_list[i],new_price_list[i],ye_price_list[i]]
if __name__ == '__main__':

    print(infoDict)
    #print(infoDict["600000"][0])
