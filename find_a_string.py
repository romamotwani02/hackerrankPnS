def count_substring(string, sub_string):
     ctr=0
     strlen=len(string)
     substr_len=len(sub_string)
     for i in range(strlen):
         if string[i:i+substr_len]==sub_string:
             ctr+=1  
     return ctr

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
