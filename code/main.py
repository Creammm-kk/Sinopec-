import control_line
import electric_line
import computer_line
import qiaojia
import qiaojia1
import fangbao_dengju
import qiaojia_fuhe
import sanfang_dengju
import electric_line10kv
import bianpin_line

def menu():
    print('***************************************************')
    print('输入对应数字并按回车进入各模块')
    print('1.电力电缆')
    print('2.计算机电缆')
    print('3.控制电缆')
    print('4.铝合金桥架')
    print('5.防爆灯具')
    print('6.三防灯具')
    print('7.铝合金桥架2')
    print('8.复合桥架')
    print('9.10kv电力电缆')
    print('10.变频电缆')
    print('***************************************************')
    chose = input()
    if chose == '1':
        electric_line.electric()
    elif chose == '2':
        computer_line.computer()
    elif chose == '3':
        control_line.control()
    elif chose == '4':
        qiaojia.qiaojia()
    elif chose == '5':
        fangbao_dengju.fangbao()
    elif chose == '6':
        sanfang_dengju.sanfang()
    elif chose == '7':
        qiaojia1.qiaojia()
    elif chose == '8':
        qiaojia_fuhe.qiaojia()
    elif chose == '9':
        electric_line10kv.electric()
    elif chose == '10':
        bianpin_line.bianpin()
    else:
        print('输入错误，请重新输入')
        menu()

# menu()


a = '0'
while a == '0':
    try:
        menu()
        a = input('输入0按回车继续执行')
    except:
        print('输入有误，请重试')
        a = input('输入0按回车继续执行')