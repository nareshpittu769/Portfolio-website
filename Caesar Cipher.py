

alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def convert_data(oparation,text,key):
    converted_text = ''
    if oparation == 'encryption': #text = hello
        for char in text:
            if char in alphabets_list:
                position = alphabets_list.index(char)
                new_position = (position+key)%26
                converted_text+= alphabets_list[new_position]
            else:
                converted_text+= char
    else:
        for char in text:
            if char in alphabets_list:
                position = alphabets_list.index(char)
                new_position = (position-key)%26
                converted_text+= alphabets_list[new_position]
            else:
                converted_text += char
    return converted_text



stop_op = False
while not stop_op:

    what_oparation = input("Enter the 'encryption' to encrypt and 'decryption' to decrypt: \n").strip().lower()
    if what_oparation == 'encryption' or what_oparation == 'decryption':
        text = input("Enter the text..: \n").lower()
        key = int(input("Enter the key : \n"))
        data = convert_data(oparation=what_oparation,text=text,key=key)
        print(f'The Data is : {data}')
        
        to_continue = input("Enter 'Y' to continue or 'N' to stop...\n").lower()
        if to_continue == 'n':
            stop_op = True
            print("Ok Thanks for using..")
        elif to_continue == 'y':
            stop_op = False
        else:
            print("Wrong operation")
            
    else:
        print('Wrong operation..')