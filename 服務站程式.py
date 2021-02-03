def gettakebreak(listdoor):
    takebreak=[]
    for  i in listdoor:
        if "01F0532N" in i or "01F0557S" in  i :
            takebreak.append("中壢")
        elif "01F0880N" in i or "01F0880S" in i :
            takebreak.append("湖口")
        elif "01F1572N" in i or "01F1572S" in i:
            takebreak.append("泰安")
        elif "01F2249N" in i or  "01F2249S" in i:
            takebreak.append("西螺")
        elif "01F2827N" in i or "01F2827S" in i :
            takebreak.append("新營")
        elif "01F3366N" in i or "01F3286S" in i:
            takebreak.append("仁德")
        elif "03F0217N" in i :
            takebreak.append("木柵")
        elif "03F0698N" in i or "03F0698S" in i:
            takebreak.append("關西")
        elif  "03F0961S" in i: 
            takebreak.append("寶山")
        elif "03F1395S" in i or "03F1395N" in i :
            takebreak.append("西湖")
        elif "03F1739N" in i or "03F1739S" in i :
            takebreak.append("清水")
        elif "03F2306S" in i or "03F2306N" in i :
            takebreak.append("南投")
        elif "03F2777N" in i or "03F2777S" in i :
            takebreak.append("古坑")
        elif "03F3211S" in i or "03F3211N" in i :
            takebreak.append("東山")
        elif "03F3496N" in i or "03F3496S" in i :
            takebreak.append("新化")
        elif "03F3588S" in i or "03F3588N" in i :
            takebreak.append("關廟")
        elif "05F0055N" in i or  "05F0055S" in i :
            takebreak.append("石碇")
        elif "05F0528N" in i or "05F0494S" in i :
            takebreak.append("蘇澳")
        else:
            continue
            

    return takebreak , len(takebreak)  #回傳list,幾個服務站
