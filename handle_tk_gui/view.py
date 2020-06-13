'''
@Author: randolph
@Date: 2020-06-13 00:13:19
@LastEditors: randolph
@LastEditTime: 2020-06-13 23:20:44
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import os
import os.path
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import pandas as pd

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(ROOT_PATH, 'student_info.xlsx')


class InputFrame(Frame):                # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master              # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.createPage()

    def createPage(self):
        # 文件存在性校验
        self.is_exist = os.path.exists(output_file)
        if not self.is_exist:        # 校验表格存在性
            df = pd.DataFrame(columns=["学号", "姓名", "班级", "性别", "大学语文", "高等数学",
                                       "线性代数", "大学英语", "Python开发", "大学体育"])
            df.to_excel(output_file, encoding='utf-8', sheet_name="学生信息", index=False)

        Label(self, text="信息录入页面", font=24, bg='#6A5ACD').grid(row=0, column=1, sticky=N, pady=10)
        # 第一行
        Label(self, text="学号:", font=20).grid(row=1, column=0, sticky=E, padx=40, pady=5)
        self.var_num = tkinter.StringVar(self, value='')
        self.entry_num = Entry(self, textvariable=self.var_num, width=30)
        self.entry_num.grid(row=1, column=1, sticky=W, pady=20)

        Label(self, text="姓名:", font=20).grid(row=1, column=2, sticky=E, padx=40, pady=5)
        self.var_name = tkinter.StringVar(self, value='')
        self.entry_name = Entry(self, textvariable=self.var_name, width=30)
        self.entry_name.grid(row=1, column=3, sticky=W)
        # 第二行
        Label(self, text="班级:", font=20).grid(row=2, column=0, sticky=E, padx=40, pady=5)
        self.var_cla = tkinter.StringVar(self, value='')
        self.entry_cla = Entry(self, textvariable=self.var_cla, width=30)
        self.entry_cla.grid(row=2, column=1, sticky=W, pady=20)

        Label(self, text="性别:", font=20).grid(row=2, column=2, sticky=E, padx=40, pady=5)
        # 下拉菜单
        self.cmb = ttk.Combobox(self)
        self.cmb.grid(row=2, column=3, sticky=W)
        self.cmb['value'] = ("男", "女")
        self.cmb.current(0)
        # 第三行
        Label(self, text="大学语文:", font=20).grid(row=3, column=0, sticky=E, padx=40, pady=5)
        self.var_sub1 = tkinter.StringVar(self, value='')
        self.entry_sub1 = Entry(self, textvariable=self.var_sub1, width=30)
        self.entry_sub1.grid(row=3, column=1, sticky=W)

        Label(self, text="高等数学:", font=20).grid(row=3, column=2, sticky=E, padx=40, pady=5)
        self.var_sub2 = tkinter.StringVar(self, value='')
        self.entry_sub2 = Entry(self, textvariable=self.var_sub2, width=30)
        self.entry_sub2.grid(row=3, column=3, sticky=W)
        # 第四行
        Label(self, text="线性代数:", font=20).grid(row=4, column=0, sticky=E, padx=40, pady=5)
        self.var_sub3 = tkinter.StringVar(self, value='')
        self.entry_sub3 = Entry(self, textvariable=self.var_sub3, width=30)
        self.entry_sub3.grid(row=4, column=1, sticky=W)

        Label(self, text="大学英语:", font=20).grid(row=4, column=2, sticky=E, padx=40, pady=5)
        self.var_sub4 = tkinter.StringVar(self, value='')
        self.entry_sub4 = Entry(self, textvariable=self.var_sub4, width=30)
        self.entry_sub4.grid(row=4, column=3, sticky=W)
        # 第五行
        Label(self, text="Python开发:", font=20).grid(row=5, column=0, sticky=E, padx=40, pady=5)
        self.var_sub5 = tkinter.StringVar(self, value='')
        self.entry_sub5 = Entry(self, textvariable=self.var_sub5, width=30)
        self.entry_sub5.grid(row=5, column=1, sticky=W)

        Label(self, text="大学体育:", font=20).grid(row=5, column=2, sticky=E, padx=40, pady=5)
        self.var_sub6 = tkinter.StringVar(self, value='')
        self.entry_sub6 = Entry(self, textvariable=self.var_sub6, width=30)
        self.entry_sub6.grid(row=5, column=3, sticky=W)
        # 第六行
        Button(self, text="保存", font=18, command=self.save).grid(row=6, column=1, sticky=W)
        Button(self, text="取消", font=18, command=self.cancel).grid(row=6, column=1, sticky=N)

    def is_number(self, num):
        pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
        result = pattern.match(num)
        if result:
            return True
        else:
            return False

    def vaild_data(self):
        '''数据校验逻辑
        '''
        try:
            num = self.var_num.get()
            name = self.var_name.get()
            cla = self.var_cla.get()
            gender = self.cmb.get()
            sub1 = self.var_sub1.get()
            sub2 = self.var_sub2.get()
            sub3 = self.var_sub3.get()
            sub4 = self.var_sub4.get()
            sub5 = self.var_sub5.get()
            sub6 = self.var_sub6.get()
            if not num or not name or not cla:
                tkinter.messagebox.showerror("信息", message="姓名班级学号不可为空，请检查输入！")
            elif not self.is_number(num):
                tkinter.messagebox.showerror("警告", message="学号必须为正整数！请输入正确值！")
            elif not name.isalpha():
                tkinter.messagebox.showerror("警告", message="姓名不合法！请修改后提交！")
            elif not sub1 or not sub2 or not sub3 or not sub4 or not sub4 or not sub5 or not sub6:
                tkinter.messagebox.showerror("信息", message="各学科分数不能为空！请仔细检查！")
            elif not self.is_number(sub1) or not self.is_number(sub2) or not self.is_number(sub3) or not self.is_number(sub4) or not self.is_number(sub5) or not self.is_number(sub6):
                tkinter.messagebox.showerror("警告", message="各学科分数存在非法值！请仔细检查！")
            else:
                num = int(num)
                # 成绩转换为浮点类型
                sub1, sub2, sub3, sub4, sub5, sub6 = float(sub1), float(sub2), float(sub3), float(sub4), float(sub5), float(sub6)

                if sub1 < 0 or sub2 < 0 or sub3 < 0 or sub4 < 0 or sub5 < 0 or sub6 < 0:
                    tkinter.messagebox.showerror("警告", message="各学科分数不能为负数！请仔细检查！")
                elif sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100 or sub5 > 100 or sub6 > 100:
                    tkinter.messagebox.showerror("警告", message="各学科分数满分为100！请输入正确值！")
                else:
                    return num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6
        except Exception as e:
            tkinter.messagebox.showerror("警告", message=e)

    def save(self):
        '''保存信息
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = self.vaild_data()
        # 写数据之前作已有数据校验
        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        nums_list = df.iloc[:, 0].values.tolist()       # 先查出学号，判断改学生是否已经存数据
        if num in nums_list:
            tar_row = nums_list.index(num)
            df.loc[tar_row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
            pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
            tkinter.messagebox.showinfo(title="信息", message="学生信息登记更新并保存成功！")
        else:
            df.loc[row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
            pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
            tkinter.messagebox.showinfo(title="信息", message="学生信息登记保存成功！")

    def cancel(self):
        '''取消
        '''
        self.var_num.set('')
        self.var_name.set('')
        self.var_cla.set('')
        self.cmb.current(0)     # 下拉框恢复
        self.var_sub1.set('')
        self.var_sub2.set('')
        self.var_sub3.set('')
        self.var_sub4.set('')
        self.var_sub5.set('')
        self.var_sub6.set('')


class DelFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='删除界面').grid()


class UpdateFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text="信息查询修改页面", font=24, bg='#D8BFD8').grid(row=0, column=1, sticky=N, pady=10)
        # 第一行
        Label(self, text="学号:", font=20).grid(row=1, column=0, sticky=E, padx=40, pady=5)
        self.var_num = tkinter.StringVar(self, value='')
        self.entry_num = Entry(self, textvariable=self.var_num, width=30)
        self.entry_num.grid(row=1, column=1, sticky=W, pady=20)

        Label(self, text="姓名:", font=20).grid(row=1, column=2, sticky=E, padx=40, pady=5)
        self.var_name = tkinter.StringVar(self, value='')
        self.entry_name = Entry(self, textvariable=self.var_name, width=30)
        self.entry_name.grid(row=1, column=3, sticky=W)
        # 第二行
        Label(self, text="班级:", font=20).grid(row=2, column=0, sticky=E, padx=40, pady=5)
        self.var_cla = tkinter.StringVar(self, value='')
        self.entry_cla = Entry(self, textvariable=self.var_cla, width=30)
        self.entry_cla.grid(row=2, column=1, sticky=W, pady=20)

        Label(self, text="性别:", font=20).grid(row=2, column=2, sticky=E, padx=40, pady=5)
        # 下拉菜单
        self.cmb = ttk.Combobox(self)
        self.cmb.grid(row=2, column=3, sticky=W)
        self.cmb['value'] = ("男", "女")
        self.cmb.current(0)
        # 第三行
        Label(self, text="大学语文:", font=20).grid(row=3, column=0, sticky=E, padx=40, pady=5)
        self.var_sub1 = tkinter.StringVar(self, value='')
        self.entry_sub1 = Entry(self, textvariable=self.var_sub1, width=30)
        self.entry_sub1.grid(row=3, column=1, sticky=W)

        Label(self, text="高等数学:", font=20).grid(row=3, column=2, sticky=E, padx=40, pady=5)
        self.var_sub2 = tkinter.StringVar(self, value='')
        self.entry_sub2 = Entry(self, textvariable=self.var_sub2, width=30)
        self.entry_sub2.grid(row=3, column=3, sticky=W)
        # 第四行
        Label(self, text="线性代数:", font=20).grid(row=4, column=0, sticky=E, padx=40, pady=5)
        self.var_sub3 = tkinter.StringVar(self, value='')
        self.entry_sub3 = Entry(self, textvariable=self.var_sub3, width=30)
        self.entry_sub3.grid(row=4, column=1, sticky=W)

        Label(self, text="大学英语:", font=20).grid(row=4, column=2, sticky=E, padx=40, pady=5)
        self.var_sub4 = tkinter.StringVar(self, value='')
        self.entry_sub4 = Entry(self, textvariable=self.var_sub4, width=30)
        self.entry_sub4.grid(row=4, column=3, sticky=W)
        # 第五行
        Label(self, text="Python开发:", font=20).grid(row=5, column=0, sticky=E, padx=40, pady=5)
        self.var_sub5 = tkinter.StringVar(self, value='')
        self.entry_sub5 = Entry(self, textvariable=self.var_sub5, width=30)
        self.entry_sub5.grid(row=5, column=1, sticky=W)

        Label(self, text="大学体育:", font=20).grid(row=5, column=2, sticky=E, padx=40, pady=5)
        self.var_sub6 = tkinter.StringVar(self, value='')
        self.entry_sub6 = Entry(self, textvariable=self.var_sub6, width=30)
        self.entry_sub6.grid(row=5, column=3, sticky=W)
        # 第六行
        Button(self, text="查询", font=18, command=self.fetch).grid(row=6, column=1, sticky=W)
        Button(self, text="保存", font=18, command=self.update).grid(row=6, column=2, sticky=N)
        Button(self, text="取消", font=18, command=self.cancel).grid(row=6, column=1, sticky=E)

    def fetch(self):
        '''先查询出信息，再去修改
        用学号查询
        '''
        num = self.var_num.get()
        name = self.var_name.get()        # 先不根据名字搜索，如果有重名情况，则提示需要输入学号辅助判断

        if num and name:
            num = int(num)          # 注意输入的学号都要转成int类型才能用
            # 每次查询先清空除去所输入内容的其他内容
            self.var_cla.set('')
            self.cmb.current(0)     # 下拉框恢复
            self.var_sub1.set('')
            self.var_sub2.set('')
            self.var_sub3.set('')
            self.var_sub4.set('')
            self.var_sub5.set('')
            self.var_sub6.set('')
        elif num:
            num = int(num)
            self.var_name.set('')
            self.var_cla.set('')
            self.cmb.current(0)     # 下拉框恢复
            self.var_sub1.set('')
            self.var_sub2.set('')
            self.var_sub3.set('')
            self.var_sub4.set('')
            self.var_sub5.set('')
            self.var_sub6.set('')
        elif name:
            self.var_num.set('')
            self.var_cla.set('')
            self.cmb.current(0)     # 下拉框恢复
            self.var_sub1.set('')
            self.var_sub2.set('')
            self.var_sub3.set('')
            self.var_sub4.set('')
            self.var_sub5.set('')
            self.var_sub6.set('')

        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        names_list = df.iloc[:, 1].values.tolist()      # 姓名列表
        nums_list = df.iloc[:, 0].values.tolist()       # 学号列表
        name_exist_time = names_list.count(name)        # 姓名出现的次数：0次没有此人，1次仅有一个，1个以上需学号查询

        if num:       # 有学号用学号查询
            if num in nums_list:
                tar_row = nums_list.index(num)
                fetch_data_list = df.loc[tar_row].tolist()
                self.fill_table(fetch_data_list)
        else:
            if name:        # 没有学号根据姓名查询，姓名重复则提示需要学号辅助判断
                if name_exist_time == 0:
                    tkinter.messagebox.showinfo(title="警告", message="查无此人！")
                elif name_exist_time == 1:
                    tar_row = names_list.index(name)
                    fetch_data_list = df.loc[tar_row].tolist()
                    self.fill_table(fetch_data_list)
                elif name_exist_time != 1:
                    tkinter.messagebox.showinfo(title="提示", message="存在重名！请输入学号辅助判断")

    def fill_table(self, data_list):
        '''将查询值塞回界面
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = data_list
        self.var_name.set(name)
        self.var_cla.set(cla)
        if gender == "男":
            self.cmb.current(0)
        else:
            self.cmb.current(1)
        self.var_sub1.set(sub1)
        self.var_sub2.set(sub2)
        self.var_sub3.set(sub3)
        self.var_sub4.set(sub4)
        self.var_sub5.set(sub5)
        self.var_sub6.set(sub6)

    def is_number(self, num):
        pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
        result = pattern.match(num)
        if result:
            return True
        else:
            return False

    def vaild_data(self):
        '''数据校验逻辑
        '''
        try:
            num = self.var_num.get()
            name = self.var_name.get()
            cla = self.var_cla.get()
            gender = self.cmb.get()
            sub1 = self.var_sub1.get()
            sub2 = self.var_sub2.get()
            sub3 = self.var_sub3.get()
            sub4 = self.var_sub4.get()
            sub5 = self.var_sub5.get()
            sub6 = self.var_sub6.get()
            if not num or not name or not cla:
                tkinter.messagebox.showerror("信息", message="姓名班级学号不可为空，请检查输入！")
            elif not self.is_number(num):
                tkinter.messagebox.showerror("警告", message="学号必须为正整数！请输入正确值！")
            elif not name.isalpha():
                tkinter.messagebox.showerror("警告", message="姓名不合法！请修改后提交！")
            elif not sub1 or not sub2 or not sub3 or not sub4 or not sub4 or not sub5 or not sub6:
                tkinter.messagebox.showerror("信息", message="各学科分数不能为空！请仔细检查！")
            elif not self.is_number(sub1) or not self.is_number(sub2) or not self.is_number(sub3) or not self.is_number(sub4) or not self.is_number(sub5) or not self.is_number(sub6):
                tkinter.messagebox.showerror("警告", message="各学科分数存在非法值！请仔细检查！")
            else:
                num = int(num)
                # 成绩转换为浮点类型
                sub1, sub2, sub3, sub4, sub5, sub6 = float(sub1), float(sub2), float(sub3), float(sub4), float(sub5), float(sub6)

                if sub1 < 0 or sub2 < 0 or sub3 < 0 or sub4 < 0 or sub5 < 0 or sub6 < 0:
                    tkinter.messagebox.showerror("警告", message="各学科分数不能为负数！请仔细检查！")
                elif sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100 or sub5 > 100 or sub6 > 100:
                    tkinter.messagebox.showerror("警告", message="各学科分数满分为100！请输入正确值！")
                else:
                    return num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6
        except Exception as e:
            tkinter.messagebox.showerror("警告", message=e)

    def update(self):
        '''保存修改信息
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = self.vaild_data()
        # 写数据之前作已有数据校验
        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        nums_list = df.iloc[:, 0].values.tolist()       # 先查出学号，判断改学生是否已经存数据
        if num in nums_list:
            tar_row = nums_list.index(num)
            df.loc[tar_row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
            pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
            tkinter.messagebox.showinfo(title="信息", message="学生信息登记更新并保存成功！")
        else:
            confirm = tkinter.messagebox.askokcancel('提示', "确定修改学号？")
            if confirm:
                df.loc[row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
                pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
                tkinter.messagebox.showinfo(title="信息", message="学生信息登记保存成功！")
            else:
                pass

    def cancel(self):
        '''取消
        '''
        self.var_num.set('')
        self.var_name.set('')
        self.var_cla.set('')
        self.cmb.current(0)     # 下拉框恢复
        self.var_sub1.set('')
        self.var_sub2.set('')
        self.var_sub3.set('')
        self.var_sub4.set('')
        self.var_sub5.set('')
        self.var_sub6.set('')


class CountFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self, text='报表界面').grid()


class AboutFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self, text='关于界面').grid()