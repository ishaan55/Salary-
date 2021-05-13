import mysql.connector
from tkinter import *
from tkinter import ttk
from test import calc


root = Tk()
root.title('Payroll Management System')
root.geometry('800x500')


mydb = mysql.connector.connect(host="127.0.0.1",user='root',passwd='1234')
cur = mydb.cursor()
cur.execute('use class;')

my_menu = Menu(root)
root.config(menu=my_menu)

option_menu=Menu(my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
my_menu.add_cascade(label="Options", menu=option_menu)

def open_calculator():
    calc()

option_menu.add_command(label='Calculator', command=open_calculator)

style = ttk.Style()
style.theme_use('default')
style.configure('Treeview',
                background='#D3D3D3',
                foreground='white',
                rowheight=25,
                fieldbackground='#D3D3D3')
style.map('Treeview',background=[('selected', '#347083')])
tree_frame = Frame(root)
tree_frame.pack(pady=10)

scroll = Scrollbar(tree_frame)
scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=scroll.set, selectmode='browse')
my_tree.pack()

scroll.config(command=my_tree.yview)

my_tree['columns'] = ('ID','First Name', 'Last Name', 'Job', 'Salary')
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('ID', width=100, anchor=CENTER)
my_tree.column('First Name', width=140, anchor=W)
my_tree.column('Last Name', width=140, anchor=W)
my_tree.column('Job', width=140, anchor=W)
my_tree.column('Salary', width=140, anchor=CENTER)

my_tree.heading('#0', text='', anchor=W)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('First Name', text='First Name', anchor=W)
my_tree.heading('Last Name', text='Last Name', anchor=W)
my_tree.heading('Job', text='Job', anchor=W)
my_tree.heading('Salary', text='Salary', anchor=CENTER)

my_tree.tag_configure('oddrow', background='white')
my_tree.tag_configure('evenrow', background='lightblue')

global count,ID
count = 0
ID = 0

cur.execute('SELECT * FROM payroll;')
records = cur.fetchall()

for record in records:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=record[0], text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))

    else:
        my_tree.insert(parent='', index='end', iid=record[0], text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
    count += 1
    if record[0]>ID:
        ID = record[0]

data_frame = LabelFrame(root, text='Record')
data_frame.pack(fill='x', expand='yes',padx=20)



first_label = Label(data_frame, text='First Name').grid(row=0,column=0, padx=10, pady=10)
first_entry = Entry(data_frame)
first_entry.grid(row=0,column=1)
last_label = Label(data_frame, text='Last Name').grid(row=0,column=3, padx=10, pady=10)
last_entry = Entry(data_frame)
last_entry.grid(row=0,column=4)

job_label = Label(data_frame, text='Job').grid(row=1,column=0, padx=10, pady=10)
job_entry = Entry(data_frame)
job_entry.grid(row=1,column=1)

salary_label = Label(data_frame, text='Salary').grid(row=1,column=3, padx=10, pady=10)
salary_entry = Entry(data_frame)
salary_entry.grid(row=1,column=4)

def clear():
    first_entry.delete(0, END)
    last_entry.delete(0, END)
    job_entry.delete(0, END)
    salary_entry.delete(0, END)

clear_bt = Button(data_frame, text='Clear', command=clear)
clear_bt.grid(row=0,column=5,padx=20,pady=10)

button_frame = LabelFrame(root, text='Commands')
button_frame.pack(fill='x', expand='yes',padx=20)

def select():
    clear()
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')
    first_entry.insert(0, values[1])
    last_entry.insert(0, values[2])
    job_entry.insert(0, values[3])
    salary_entry.insert(0, values[4])

select_bt = Button(button_frame,text='Select Record', command=select)
select_bt.grid(row=0, column=0, padx=10,pady=5)

def add():
    global count,ID
    ID += 1
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=ID, text='', values=(ID, first_entry.get(), last_entry.get(), job_entry.get(), salary_entry.get()), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=ID, text='', values=(ID, first_entry.get(), last_entry.get(), job_entry.get(), salary_entry.get()), tags=('oddrow',))
    
    cur.execute('insert into payroll values(%s,%s,%s,%s,%s)',(ID,first_entry.get(),last_entry.get(),job_entry.get(),salary_entry.get()))
    mydb.commit()
    count += 1
    clear()

add_bt = Button(button_frame,text='Add Record', command=add)
add_bt.grid(row=0, column=1, padx=10,pady=5)

def delete():
    x = my_tree.selection()[0]
    my_tree.delete(x)
    cur.execute(f'delete from payroll where ID = {int(x)}')
    mydb.commit()
    

delete_bt = Button(button_frame,text='Delete Record',command=delete)
delete_bt.grid(row=0, column=2, padx=10,pady=5)

def update():
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')
    my_tree.item(selected, text='', values=(values[0], first_entry.get(), last_entry.get(), job_entry.get(), salary_entry.get()))

    cur.execute('update payroll set First_Name=%s,Last_Name=%s,Job=%s,Salary=%s where ID=%s',(first_entry.get(), last_entry.get(), job_entry.get(), salary_entry.get(),values[0]))
    mydb.commit()
    clear()

update_bt = Button(button_frame,text='Update Record', command=update)
update_bt.grid(row=0, column=3, padx=10,pady=5)


root.mainloop()

print("i'm in different branch")
