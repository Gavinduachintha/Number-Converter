
def decimal_to_binary(decimal_number):
    binary=''
    while decimal_number>0:
        binary=str(decimal_number%2)+binary
        decimal_number = decimal_number//2
    return binary

def binary_to_octal(binary_number):
    binary_number =str(binary_number)
    octal_result=''
    while len(binary_number)%3!=0:
        binary_number='0'+binary_number
    for i in range(0,len(binary_number),3):
        chunk = binary_number[i:i+3]
        octal_value=int(chunk[0])*4+int(chunk[1])*2+int(chunk[2])*1
        # octal_value=int(chunk,2)
        octal_result+=str(octal_value)
    print(octal_result)

def binary_to_hexadecimal(binary_number):
    numeric_values={10:'A',
                    11:'B',
                    12:'C',
                    13:'D',
                    14:'E',
                    15:'F'}
    
    binary_number=str(binary_number)
    hexa_decimal_result=''
    while len(binary_number)%4!=0:
        binary_number='0'+binary_number
    for i in range(0,len(binary_number),4):
        chunk = binary_number[i:i+4]
        hexa_decimal_value=int(chunk[0])*8+int(chunk[1])*4+int(chunk[2])*2+int(chunk[3])*1
        hexa_decimal_result+=str(hexa_decimal_value)
    print(hexa_decimal_value)
    return(hexa_decimal_value)
        

def binary_to_decimal(binary_number):
    binary_list=[]
    binarytoDecimal = 0
    binary_string=[int(binary_bit) for binary_bit in str(binary_number)]
    binary_string.reverse()
    for i in range(0, len(binary_string)):
        binary_list.append(binary_string[i]*(2**i))
        binarytoDecimal+=(binary_string[i]*(2**i))
    print(binarytoDecimal)
    return binarytoDecimal

print("Number conversion v1")
user_input = int(input("Enter your choice: "))
if user_input == 1:
    decimal_number=int(input("Enter your decimal number: "))
    binary_result=decimal_to_binary(decimal_number)
    print(binary_result)
elif user_input == 2:
    binary_number = input("Enter your binary number: ").strip()
    binary_to_decimal(binary_number)
elif user_input == 3:
    decimal_number=int(input("Enter you decimal number: "))
    binary_result = decimal_to_binary(decimal_number)
    octal_result=binary_to_octal(binary_result)
elif user_input ==4:
    decimal_number=int(input("Enter your decimal number: "))
    binary_result=decimal_to_binary(decimal_number)
    hexa_decimal_result=binary_to_hexadecimal(binary_result)