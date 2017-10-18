# num=int(input('Value:'))
# rev_num=int(str(num)[::-1])
# print(rev_num)


# l=[1,2,3,4,65,76,89,23,43,1,2,43,43,2,1,3,4,4,4,4,4,'hello','hello']
# print(list(set(l)))



# a=25
# print(bin(a))
# print({'{:b}'.format(a)})
# print(hex(a))
# print(oct(a))



# a=30
# b=200
# c=150
# if a>b>c:
#     print('A > B > C')
# elif c>b<a:
#     print('C > B < A' )
# else:
#     print('B > A > C')

# fname='smo'
# lname='shajib'
#
# if fname>lname:
#     print(fname+ ''+ lname)
# else:
#     print("Good Name")
#

password=input('Give Password:')

if len(password) >= 8:
    print('Valid Password:',password)
elif len(password)<=8 :
     print('Invalid Password:',password)
     password2=input('Try Password:')
     if len(password2) >=8 :
        print('Valid Password:',password2)
     else:
       print('Block User:',password2)



# help('reversed')
