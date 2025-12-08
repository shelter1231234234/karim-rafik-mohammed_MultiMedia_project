# # عرض العنصر بطريقه place
from tkinter import *

root = Tk()
root.geometry("500x500")

mybutton1 = Button(root, text="Button1")
# place():هي إحدى الطرق في Tkinter لتحديد موقع العنصر
# x=100: امشي على محور x مسافه 100
# y=50:امشى على محور y مسافه50
# نقطه التمركز الافتراضيه هى الشمال الغربي (nw)
mybutton1.place(x=200, y=50)

mybutton2 = Button(root, text="Button2")
mybutton2.place(x=200, y=100)

# #علشان اخلى العنصر فى منتصف الشاشه

mybutton3 = Button(root, text="Button3")
# relx,y=من الصفر للواحد
# relx=0.5:يعني أن الزر سيتم وضعه نصف المسافة من العرض الكامل للنافذة
# rely=0.5:يعني أن الزر سيتم وضعه نصف المسافة من الارتفاع الكامل للنافذة
# فعليا الزر ف المنتصف لكن نقطه الارتكاز الافتراضيه هى nw
mybutton3.place(relx=0.5, rely=0.5)

# علشان اخلى الزر اعلى يمين الشاشه
mybutton4 = Button(root, text="Button4")
# relx=1:يعني أن الزر سيتم وضعة فى اليمين
# anchor="ne":غيرت نقطه التمركز لاعلى اليمين
# width:بغير عرض الزر
# height: بغير طول الزر
mybutton4.place(relx=1, anchor="ne", width=100, height=50)


mybutton5 = Button(root, text="Button5")
# # relwidthx=0.5:الزر ياخد نصف  المساحه الكليه للواجهه على محور x
# # relheight=0.5: نصف المساحه الكليه للواجهه على محور y
mybutton5.place(relwidth=0.5, relheight=0.5)

# داله بستخدمها علشان الواجهه تفضل ظاهره
root.mainloop()

# #############################################################

from tkinter import *

root = Tk()
root.geometry("400x200")

# Button(root, text="Button 1"): انشاء زر على الواجهه
button1 = Button(root, text="Button 1")
# 0ضع الزر في الشبكة في الصف 0 والعمود
# . ستتم محاذاة الزر في الجزء العلوي الأيسر من النافذة
button1.grid(row=0, column=0)


button2 = Button(root, text="Button 2")
# يتم وضعه في الصف 0 والعمود 1، مما يعني أنه سيكون بجانب
# "Button 1" في نفس السطر (لكن على اليمين).
button2.grid(row=0, column=1)

button3 = Button(root, text="Button 3")
button3.grid(row=1, column=0)

button4 = Button(root, text="Button 4")
button4.grid(row=1, column=1)

button5 = Button(root, text="Button 5")
# columnspan=2:يظهر الزر في الصف الثالث ويشغل المساحة الممتدة عبر العمودين 0 و1.
# (سيأخذ المساحة المشتركة بين العمودين)
button5.grid(row=2, column=0, columnspan=2)

button6 = Button(root, text="Button 6")
# rowspan=2:  يظهر الزر في الصف الثالث ويشغل المساحة الممتدة عبر الصفين 0 و1.
# (سيأخذ المساحة المشتركة بين الصفين)
button6.grid(row=0, column=2, rowspan=2)

root.mainloop()

# ##############################################
from tkinter import *

root = Tk()
root.geometry("400x200")

# Button(root, text="Button 1"): انشاء زر على الواجهه
button1 = Button(root, text="Button 1")
# padx:مسافه خارجيه بين العناصر ع محور x
# pady:مسافه خارجيه بين العناصر ع محور y
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = Button(root, text="Button 2")
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = Button(root, text="Button 3")
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(root, text="Button 4")
button4.grid(row=1, column=1, padx=10, pady=10)

button5 = Button(root, text="Button 5")
button5.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

button6 = Button(root, text="Button 6")
# row=2, column=0: يضع الزر في الصف الثالث والعمود الاول.
# columnspan=2: يجعله يمتد عبر عمودين (العمود 0 والعمود 1).
# padx=10, pady=10: إضافة مسافات خارجية قدرها 10 بيكسل في المحورين X و Y.
# ipadx=10: يضيف مساحة داخلية  قدرها 10 بيكسل على المحور X داخل الزر
# sticky="we": يجعل الزر يمتد بشكل أفقي عبر العمودين، حيث
# "w" تعني الغرب (West) و**"e"** تعني الشرق (East)،
# خلى الزر ياخد مسافه من الغرب للشرق بامتداد العمودين الاول والتانى
button6.grid(row=3, column=0, columnspan=2, padx=10, pady=10, ipadx=10, sticky="we")

root.mainloop()
# #####################################################################

from tkinter import *

root = Tk()
mybutton = Button(root, text="my button", fg="black", bg="pink")
mybutton.pack()

mylabel = Label(root, text="my label")
mylabel.pack()
mylabel.config(bg="yellow")

myentry = Entry(root, width=20)
myentry.pack()

# Text(root, width=20, height=10):
# ينشئ منطقة نصية متعددة الأسطر تسمح للمستخدم بإدخال نص طويل.
mytext = Text(root, width=20, height=10)
mytext.pack()

# علشان اقدر اناختار قيمه واحده منهم
# عملت متغير من متغيرات tkinter
# عملت المتغير دا هيحتفظ بقيمه نصيه
mygroup = StringVar()
# هنا بقوله لو القيمه عندى كانت check1
# خزنها فى متغير mygroup
myoption1 = Radiobutton(root, text="check me 1", variable=mygroup, value="check1")
myoption1.pack()
myoption2 = Radiobutton(root, text="check me 2", variable=mygroup, value="check2")
myoption2.pack()


mycheckbutton = Checkbutton(root, text="check me")
mycheckbutton.pack()

myoptions = Listbox(root)
myoptions.pack()

# علشان اضسف عاصر فى listbox
myoptions.insert(1, "Html")
myoptions.insert(2, "Css")
myoptions.insert(3, "JS")

root.mainloop()
# ############################################################

from tkinter import *
from PIL import ImageTk, Image

# إنشاء النافذة
root = Tk()
root.title("نافذة بالصورة")

# تحميل الصورة
img = Image.open(
    r"D:\2026\multimedia\3mly\934121_1012971262084289_922155315780796550_n.jpg"
)  # ضع مسار صورتك
img = img.resize((300, 200))  # تغيير الحجم (اختياري)
photo = ImageTk.PhotoImage(img)

# إضافة الصورة للواجهة
label = Label(root, image=photo)
label.pack()

root.mainloop()
############################################################
