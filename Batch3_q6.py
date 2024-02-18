'''A text file named "matter.txt" contains some text, which needs to be displayed such that every next 
character is separated by a symbol #" and if there is a space it is to be replaced by $'. Write a function 
definition for hash display() in Python that would display the entire content of the file matter.txt in the 
desired format. 
If the file matter.txt has the following content stored in it : 
THE WORLD IS ROUND 

The function hash display) should display the following content 
T#H#E$W#O#R#L#D$I#S$R#O#U#N#D# 
 '''

def hash_display(input_file,out_file):
  try:
    with open(input_file,'r') as inp_file:
      data =inp_file.read()
      formatted_data=""
      for char in data:
        if char == ' ':
          formatted_data+='$'
        else:
          formatted_data +=char+'#'
      print(formatted_data)
      with open(out_file,'a') as out_file:
        out_file.write(formatted_data)

  except FileNotFoundError:
    print("File not found")
  except Exception as e:
    print("Error occurred",e)
  finally:
    print("Execution completed")

input_file_path = "matter.txt"
output_file_path = "formatted_output.txt"
hash_display(input_file_path, output_file_path)