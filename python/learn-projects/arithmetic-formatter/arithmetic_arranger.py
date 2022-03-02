# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# pylint: disable-all

import operator



def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
       return "Error: Too many problems."


    ops = {
        '+' : operator.add,
        '-' : operator.sub,
    }
  
    arranged_problems = []

# Add an index (enumerate) and loop to each problem. Ex.: "32 + 698"
    for index, value in enumerate(problems):
    
      # Returns a list splited by white spaces -> ["32", "+", "698"]
        opsValues = value.split(" ")      

        # Verify the operator:
        if opsValues[1] != "+" and opsValues[1] != "-":
            return "Error: Operator must be '+' or '-'."

        # Verify the lenght, must be 4 numbers max
        if len(opsValues[0]) > 4 or len(opsValues[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
        # Verify if the values are integers (try to convert)
        try:
            value1 = int(opsValues[0])
            value2 = int(opsValues[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        # Get the longest value width
        longestLine = max(len(opsValues[0]), len(opsValues[2]))
        
        # The +2 represents the whitespace and operator spaces
        widthLine = longestLine + 2
        
        # Uses :> to align to the right based on the widthLine lenght

        V1 = f"{opsValues[0]:>{widthLine}}"
        V2 = f"{opsValues[1]}" + f"{f'{opsValues[2]}':>{widthLine-1}}"
        D = '-' * widthLine
        ans = ops[opsValues[1]](value1, value2) 
        A = f"{str(ans):>{widthLine}}"
      
        try:
          arranged_problems[0] += (' ' * 4) + V1
        except IndexError:
          arranged_problems.append(V1)

        try:
          arranged_problems[1] += (' ' * 4) + V2
        except IndexError:
          arranged_problems.append(V2)

        try:
          arranged_problems[2] += (' ' * 4) + D
        except IndexError:
          arranged_problems.append(D)     
          
        if args:
          try:
            arranged_problems[3] += (' ' * 4) + A
          except IndexError:
            arranged_problems.append(A)     


    if args:
        return f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}\n{arranged_problems[3]}"
    else:
        return f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))