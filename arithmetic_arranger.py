import operator
def arithmetic_arranger(problems, svt = False):
  #
  # Step 1: Check preconditions and return proper error
  # Step 2: Split strings, into number1s, number2s, operators, and results
  # Step 3: Build line 1 of output <num1>
  # Step 4: Build line 2 of output <op> <num2>
  # Step 5: Build line 3 of output (------)
  # Step 6: Build line 4 of output (results)
  # Step 7: Join all lines with /n
  ops = { '+': operator.add, "-": operator.sub}
  top = ''
  bottom = ''
  middle = ''
  sumline = ''
  n1 = []
  op = []
  n2 = []
  widths = []
  if len(problems) > 5:
    return 'Error: Too many problems.'
  if any(('/' in i for i in problems)):
    return "Error: Operator must be '+' or '-'."
  if any(('*' in i for i in problems)):
    return "Error: Operator must be '+' or '-'."   
  for i in problems:
    numbers = i.split()

    if numbers[0].isnumeric() == False:
      return 'Error: Numbers must only contain digits.'

    if numbers[2].isnumeric() == False:
        return 'Error: Numbers must only contain digits.'

    if len(numbers[0]) > 4 or len(numbers[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    n1.append(numbers[0])
    op.append(numbers[1])
    n2.append(numbers[2])
    


# No more in the above forloop
# Format the strings
#    32      3801      45      123
#
# + 698    -    2    + 43    +  49
#
# -----    ------    ----    -----

  for idx in range(len(n1)):
    # Find the length of the largest value
    if len(n1[idx]) > len(n2[idx]):
      widths.append(len(n1[idx]))
    else:
      widths.append(len(n2[idx]))

    

    middle_part = op[idx] + " " + n2[idx].rjust(widths[idx])
    middle = middle + middle_part + "    "

    top = top + n1[idx].rjust(len(middle_part)) + "    "

    bottom = bottom + "-"*len(middle_part) + "    "

    answr = str(ops[op[idx]](int(n1[idx]), int(n2[idx])))
    sumline = sumline + answr.rjust(len(middle_part)) + "    "

     
  top = top.rstrip()
  middle = middle.rstrip()
  bottom = bottom.rstrip()
  arranged_problems = top + "\n" + middle + "\n" + bottom
  # True
  if svt == True:         
    sumline = sumline.rstrip()
    top = top.rstrip()
    middle = middle.rstrip()
    bottom = bottom.rstrip()
    arranged_problems = top + "\n" + middle + "\n" + bottom + "\n" + sumline

  return arranged_problems