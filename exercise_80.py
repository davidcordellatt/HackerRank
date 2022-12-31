import re
string = 'aaadaa' #input()
sub_string = 'aa' #input()

sub_string_st_end = re.compile(sub_string)
position_tuple = sub_string_st_end.search(string)
if position_tuple:
  while position_tuple:
    print(f"({position_tuple.start()}, {position_tuple.end()-1})")
    position_tuple = sub_string_st_end.search(string, position_tuple.start()+1)
        
else:
  print("(-1, -1)")