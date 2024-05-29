
def code(val):
  ''' to code the text in sign language'''
  if len(val)>=3:#len is more than or equyal to three
    text_list=list(val)
    c=text_list.pop(0)
    text_list.append(c)
    val_1=''.join(text_list)
    str1='adl'
    val_1=val_1+str1
    val_2=str1+val_1
    return(val_2)
  else:
    return(val[::-1])

def decode(dec_text):
  ''' for decoding '''
  if len(dec_text)>=3:
    text_1=dec_text.removeprefix('adl')
    text_2=text_1.removesuffix('adl')
    list_text=list(text_2)
    s=list_text.pop()
    list_text.insert(0,s)
    return(''.join(list_text))
  else:
    return(dec_text[::-1])

# ask choice of user
n=int(input("do you want to\n1.code\n2.decode\n"))
text=input("enter the text to code/decode\n")
if n==1:
  code_text=code(text)# function calling coding
  print(f"coded text is {code_text}")
elif(n==2):
  decode_text=decode(text)#decoding function calling
  print(f"decoded text is {decode_text}")
