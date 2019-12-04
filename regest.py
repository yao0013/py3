import requests
import tkinter


def regedit():
    name = str(input('请输入注册名'))
    data = {
    'username':name
    }

    headers = {
    'cookie':'Hm_lpvt_3b0150c3aee6054cf944ea6c8f8a7392=1569547590; Hm_lvt_3b0150c3aee6054cf944ea6c8f8a7392=1569547590'
    }

    url = 'https://www.charles.ren/api/licenseKey/generate'

    r = requests.post(url=url,headers=headers,data=data)
    back = r.json()['data']

   
    print(f'注册码是{back}')

    '''sr = input('谢谢使用')

    while sr == 'q':
        break'''
    window = tkinter.Tk()
    window.title('注册机')
    window.geometry('400x400')
    button1 = tkinter.Button(window,
                            text='生成注册码',
                            bg='orange',
                            height=3,
                            width=20,
                            bd=3,
                            relief='sunken',
                            activebackground='orange',
                            activeforeground='white',
                            command=r
                            )
    button1.pack()


    button2 = tkinter.Button(window, text='退出', height=3, command=window.quit())
    button2.pack()

    vari = tkinter.Variable()
    entry = tkinter.Entry(window, textvariable=vari)
    entry.pack()
    vari.set('请输入注册名')
    print(vari.get())
    print(entry.get())
    text = Text(window, bg='yellow', width=40, height=10)
    text.insert(INSERT,back)
    text.pack()




regedit()