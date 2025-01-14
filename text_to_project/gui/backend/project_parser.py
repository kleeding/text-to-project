def _script(line):
    ##
    pass

def _variables(line):
    pass

def _functions(line):
    result = []

    ## ADD CHECK FOR TYPE 2 - ADD TAB BEFORE FUNCTION START
    l1 = ["def ", line[0], "(", "):"]
    args = []
    for inputs in line[2:]:
        if inputs == "->" or inputs == "_":
            break
        args.append(inputs)

    args = ", ".join(args)
    if args:
        l1.insert(3, args)

    definition = "".join(l1)
    result.append(definition)

    l2 = ["\treturn"]
    pos = 4 + len(args)
    returns = []
    for outputs in line[pos:]:
        if outputs == "_":
            break
        returns.append(outputs)

    returns = ", ".join(returns)
    if returns:
        l2.append(" " + returns)

    output = "".join(l2)
    result.append(output)
    result.append("\n")
    
    return result

def _main(line):
    pass

parts = [_main, _script, _variables, _functions]
segments = ["Main", "Project", "Variables", "Functions"]

def project_parser(content):
    content = content.split('\n')
    imports = []
    project = []

    seg = 0
    _type = 0

    index = 0
    while index < len(content):
        line = content[index]
        if line in segments:
            seg = segments.index(line)
        
        index += 1
        tabbed_line = content[index]
        while tabbed_line[:1] == "\t" and index < len(content): # <- part of this segment (function/variable)
            tabbed_line = content[index]
            print("function/variable/main", tabbed_line)
            while tabbed_line[1:3] == "\t" and index < len(content): # <- part of a function (variable/function call)
                print("function Variable", tabbed_line)
                index += 1
            index += 1
            # print(seg)
        line = line.replace(","," ").split()
        print("project, variable, function, main", line)
        index += 1

    # for line in content:
    #     # print(line)
    #     if line[:1] == "\t":
    #         line_split = line.replace(","," ").split()
    #         output = parts[seg](line_split)
    #         if output:
    #             for out in output:
    #                 project.append(out + "\n")
    #     elif line == "Project":
    #         _type = 0
    #         seg = 1
    #     elif line == "Variables":
    #         seg = 2
    #     elif line == "Functions":
    #         seg = 3
    #     elif line == "Main":
    #         seg = 0

    return project

