print('输入身高体重计算BMI指数(注意此标准均参考自百度百科)')
a=float(input('请输入身高(m):'))
b=float(input('请输入体重(kg):'))
jg=b/(a*a)
print(round(jg,2))
if jg <18.5:
    print('低于标准体重')
elif jg >=18.5 and jg < 25:
    print('正常体重')
elif jg >= 25 and jg <30:
    print('超重')
elif jg >= 30 and jg <35:
    print("一级肥胖")
elif jg >=35 and jg < 40:
    print("二级肥胖")
elif jg > 40:
    print ("极度肥胖。讲真的，想象不到你有多重，如果有心情请联系我的QQ：1315424708")


