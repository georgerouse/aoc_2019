if __name__ == '__main__':
    # Get the input data
    with open('input/day_02.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(',')]
    original_list = input_list.copy()   
    input_list[1] = 12
    input_list[2] = 2
    
    # Loop through the instruction list
    for i in range(0, len(input_list), 4):
        instruction = input_list[i:i + 4]
        if len(instruction) == 4:
            opcode, param_1, param_2, param_3 = instruction
        else:
            opcode = instruction[0]
            
        if opcode == 1:
            input_list[param_3] = input_list[param_1] + input_list[param_2]
            
        elif opcode == 2:
            input_list[param_3] = input_list[param_1] * input_list[param_2]
            
        elif opcode == 99:
            break
     
    print("Position 0:", input_list[0])

    # Loop through the combinations of noun and verb
    for noun in range(0, 100):
        for verb in range(0, 100):
            instruction_copy = original_list.copy()
            instruction_copy[1] = noun 
            instruction_copy[2] = verb
            
            # Loop through the instruction list
            for i in range(0, len(instruction_copy), 4):
                instruction = instruction_copy[i:i + 4]
                if len(instruction) == 4:
                    opcode, param_1, param_2, param_3 = instruction
                elif(instruction) == 1:
                    opcode = instruction[0]
                else: 
                    break
                
                try:
                    if opcode == 1:
                        instruction_copy[param_3] = instruction_copy[param_1] + instruction_copy[param_2]
                        
                    elif opcode == 2:
                        instruction_copy[param_3] = instruction_copy[param_1] * instruction_copy[param_2]
                        
                    elif opcode == 99:
                        break
                except:
                    pass
    
            if instruction_copy[0] == 19690720:
                print("Noun:", noun, " Verb:", verb)
                print("100 * noun + verb:",100 * noun + verb)
