list=["ahmad",100,99,400,"red",50]
#حذف النصوص(العناصر من نوعstr)
list.remove("ahmad")
print("list without ahmad : " ,list)
list.remove("red")
print("list without red too : " ,list)
print("\n")
#ترتيب عناصر القائمة تصاعدياً
print("In ascending order : " , list.sort())
#طول القائمة
print("Length of the list = " , len(list))
print("\n")
#استخراج اكبر رقم في القائمة
print("Max num = " , max(list))
#استخراج اصغر رقم في القائمة
print("Min num = ", min(list))
print("\n")
#طباعة العنصر الموجود في خانة -1
print("Index -1 = ", list[-1])
#تحويل القائمة الى نص str بحيث تكون العناصر مفصولة بنقطة
print("To str type : ", '.'.join([str(list[0]),str(list[1]),str(list[2]),str(list[3])]))
