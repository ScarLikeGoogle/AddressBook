# coding=utf-8
from __future__ import print_function
import pickle as p
import os
import sys

class Person():
    filename = 'pok.txt'
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.personlist = {self.name: [self.phone,self.email]}

    def load(self):
        if os.path.exists(self.filename):
            f = open(self.filename,'r')
            self.personlist = p.load(f)
            f.close()
        else:
            f = file(self.filename,'w')
            conlist = {'jack': ['jack@ict.ac.cn','123']}
            p.dump(conlist,f)
            f = file(self.filename)
            self.personlist = p.load(f)
            f.close()

    def show(self):
        for key,value in self.personlist.items():
            print('联系人:%s,电话:%s,Email:%s'%(key,value[0],value[1]))

    def add(self):
        self.name = raw_input('请输入联系人姓名：\n')
        if self.name in self.personlist.keys():
            print('联系人已经存在了')
        else:
            self.phone = raw_input('请输入联系人电话:\n')
            self.email = raw_input('请输入联系人Email:\n')
            self.personlist[self.name] = [self.phone,self.email]
            # self.personlist = {self.name: [self.phone,self.email]}
            f = file(self.filename, 'w')
            p.dump(self.personlist, f)
            f.close()
            print('联系人已经添加')

    def search(self):
        person.show()
        self.name = raw_input('请输入联系人姓名:\n')
        for k,v in self.personlist.items():
            if self.name == k:
                print('电话:%s,Email:%s' %(v[0],v[1]))

    def modify(self):
        person.show()
        self.name = raw_input('输入联系人的姓名:\n')
        for k,v in self.personlist.items():
            if k == self.name:
                sub_menu = raw_input('选择修改内容:\n'
'1.Email\n'
'2.电话\n')
                if sub_menu == '1':
                    print('原始Email:' + v[1])
                    self.email = raw_input('输入修改后的Email:\n')
                    self.personlist[self.name] = [v[0],self.email]
                    print(self.personlist.items())
                if sub_menu == '2':
                    print('原始电话:'+v[0])
                    self.phone = raw_input('输入修改后的电话:\n')
                    self.personlist[self.name] = [self.phone,v[1]]
                f = file(self.filename, 'w')
                p.dump(self.personlist, f)
                f.close()
                print('修改成功')

    def delete(self):
        person.show()
        self.name = raw_input('请输入要删除的联系人姓名:\n')
        if self.name in self.personlist.keys():
            del self.personlist[self.name]
            f = file(self.filename, 'w')
            p.dump(self.personlist, f)
            f.close()
            print('删除成功')
        else:
            print('联系人不存在')

if __name__ == '__main__':
    command = ['1','2','3','4','5','6']
    person = Person('','','')#实例化类对象
    person.load()
    while True:
        menu = raw_input('''
1.显示全部联系人
2.查询
3.添加
4.修改
5.删除
6.退出\n''')
        if menu in command:
            if menu == '1':
                person.show()
                continue
            if menu == '2':
                person.search()
            elif menu == '3':
                person.add()
                continue
            elif menu == '4':
                person.modify()
                continue
            elif menu == '5':
                person.delete()
                continue
            elif menu == '6':
                sys.exit()
        else:
            print('请输入命令:\n')
            continue

