list1 = ['xyz@protonmail.com', 'abc@gmail.com', 'cde@yahoo.co.in']

for j in list1:
    st = j.find('@')
    end = j.find('.')
    print(j[st+1:end])
