''' Write a Python program to accept two filenames as command line arguments. Then copy contents of 
one file into another adding line number to the beginning of each line and length of the line at the end 
of each line. Incorporate validation checks wherever applicable.'''

import sys

def copy_file(input_file , output_file):
  try:
     with open(input_file, 'r') as f_in:
        with open(output_file,'w') as f_out:
           line_no =1
           for line in f_in:
              line_length = len(line.strip())
              f_out.write(f"{line_no}:{line.strip()} ({line_length} characters) \n")
              line_no+=1
     print(f"Contents of {input_file} copied to {output_file} wiith line no and lengths")
  except FileNotFoundError:
    print("File not found")
  except PermissionError :
    print("Permission denied")
  except Exception as e:
    print(f"Error: {e}")


if len(sys.argv) != 3:
  print("Usage: python Batch1_q4.py <input_file> <output_file>")
  sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

copy_file(input_file, output_file)

      
