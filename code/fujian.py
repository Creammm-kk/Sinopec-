import re
# final = [wh, bihou, mode, have_gaiban, tibian, zhonglei,classes]
def not_empty(s):
    return s and s.strip()

def get_wh(val):#得到长宽
    wh = []
    # print("AAAA", val)
    # print("AAAA", wh)
    for data in val:
        n = "".join(filter(lambda s: s in '0123456789.', data))
        if len(n)==3 or n == '50' or n == '1000' or n == '1200':
            wh.append(n)
    wh = filter(not_empty, wh)
    wh = list(wh)
    # print("AAAA", wh)
    try:
        wh = [wh[0],wh[1]]
    except:
        try:
            wh = [wh[0],'0']
        except:
            wh = ['0','0']
    return wh

def baoku(vals):
    # print("AAAA",vals)
    wh = get_wh(vals)
    wh = wh[0] + '×' + wh[1]
    bihou = vals[-1]
    try:
        bihou = float(bihou)
    except:
        bihou = 0
    zhonglei = 'baoku'
    final = [wh,bihou,'','','',zhonglei,'直通桥架']
    return final
def fengtou(vals):
    wh = get_wh(vals)
    wh = wh[0] + '×' + wh[1]
    bihou = vals[-1]
    try:
        bihou = float(bihou)
    except:
        bihou = 0
    zhonglei = 'fengtou'
    final = [wh,bihou,'','','',zhonglei,'直通桥架']
    return final
def guanjietou(vals):
    mode = 'buxiugang'
    wh = ''
    zhonglei = 'guanjietou'
    DN = 0
    ns = ''
    for data in vals:
        if data.find('铝合金') != -1:
            mode = 'lvhejin'
        elif data.find("Q235") != -1 or data.find("碳钢") != -1 or data.find("钢制") != -1:
            mode = "gangzhi"
        data_ = re.sub("Q235B", "", data)
        if data.find("DN") != -1:
            DN = 1
        n = "".join(filter(lambda s: s in '0123456789.', data_))
        ns = ns + n
    print(ns)
    if ns != '':
        if DN == 1:
            wh = 'DN' + ns
        else:
            if ns == '34':
                wh = 'DN20'
            elif ns == '12':
                wh = 'DN15'
            elif ns == '1':
                wh = 'DN25'
            elif ns == '114':
                wh = 'DN32'
            elif ns == '112':
                wh = 'DN40'
            elif ns == '2':
                wh = 'DN50'
            elif ns == '3':
                wh ='DN80'
            elif ns =='4':
                wh = 'DN100'

    final = [wh,'',mode,'','',zhonglei,'']
    return final
def zadai(vals):
    number = []
    for data in vals:
        n = "".join(filter(lambda s: s in '0123456789.', data))
        if n != '' and n != '304' and n != '316':
            number.append(n)
    # try:
    #     wh = number[0]+'×'+number[1]
    # except:
    #     wh = number[0]
    try:
        wh = number[0]
    except:
        wh = 'error'
    zhonglei = 'zadai'
    final = [wh,'','','','',zhonglei,'']
    return final
def geban(vals):
    wh = 0
    wh_list = []
    for data in vals:
        n = "".join(filter(lambda s: s in '0123456789.', data))
        if n != '':
            wh_list.append(n)
    zhonglei  = 'geban'
    try:
        wh_list = [x for x in wh_list if float(x) > float(vals[-1])]
    except:
        wh_list = None
    if wh_list:
        wh = min(wh_list, key=lambda x: float(x))
    else:
        wh = ''  # 如果为空，给个默认值
    bihou = vals[-1]
    final = [wh,bihou,'','','',zhonglei,'']
    return final
def zhijiepian(vals):
    wh_list = []
    for data in vals:
        n = "".join(filter(lambda s: s in '0123456789.', data))
        wh_list.append(str(n))
    wh_list = filter(not_empty, wh_list)
    wh_list = list(wh_list)
    try:
        wh = wh_list[0]
    except:
        wh = 'error'
    zhonglei = 'zhijiepian'
    final = [wh,'','','','',zhonglei,'']
    return final
def wanjiepian(vals):
    wh_list = []
    for data in vals:
        n = "".join(filter(lambda s: s in '0123456789.', data))
        wh_list.append(str(n))
    wh_list = filter(not_empty, wh_list)
    wh_list = list(wh_list)
    try:
        wh = wh_list[0]
    except:
        wh = 'error'
    zhonglei = 'wanjiepian'
    final = [wh, '', '', '', '', zhonglei,'']
    return final
def tiaojiaopian(vals):
    # wh_list = []
    # for data in vals:
    #     n = "".join(filter(lambda s: s in '0123456789.', data))
    #     wh_list.append(str(n))
    # wh_list = filter(not_empty, wh_list)
    # wh_list = list(wh_list)
    # wh = wh_list[0]
    wh_list = []
    for data in vals[0:-1]:
        n = "".join(filter(lambda s: s in '0123456789.', data))
        wh_list.append(str(n))

    wh_list = filter(not_empty, wh_list)
    wh_list = list(wh_list)
    wh_list = [x for x in wh_list if float(x) > 0]
    if wh_list:
        wh = min(wh_list, key=lambda x: float(x))
    else:
        wh = ''  # 如果为空，给个默认值
    zhonglei = 'tiaojiaopian'
    final = [wh, '', '', '', '', zhonglei,'']
    return final
def lianjiexian(vals):
    wh_list = []
    wh = 0
    for data in vals:
        n = "".join(filter(lambda s: s in '0123456789.', data))
        n = re.sub(r"\.0", "", n)
        if n != '':
            wh_list.append(n)
    try:
        if wh_list[0] != '1':
            wh = wh_list[0]
        else:
            wh = wh_list[1]
    except:
        wh = 'error'
    zhonglei = 'lianjiexian'
    final = [wh,'','','','',zhonglei,'']
    return final
def gudingyaban(vals):
    zhonglei = 'gudingyaban'
    yangshi = '槽式'
    for data in vals:
        if data.find('梯')!=-1:
            yangshi = '梯式'
    final = [yangshi,'','','','',zhonglei,'']
    return final
def xiangjiaodian(vals):
    zhonglei = 'xiangjiaodian'
    final = ['', '', '', '', '', zhonglei,'']
    return final
def luoshuan(vals):
    zhonglei = 'luoshuan'
    final = ['', '', '', '', '', zhonglei,'']
    return final

