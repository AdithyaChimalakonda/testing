
depends={}
installed=[]

def find_dependencies(item):
    current=[]
    if not item in depends.keys():
        return current
    for token in depends[item]:
        current.append(token)
        current.extend(find_dependencies(token))

    with_out_dups=[]
    for token in current:
        if token not in with_out_dups:
            with_out_dups.append(token)

    return with_out_dups

def find_dependents(item):
    current=[]
    for key,value in depends.items():
        if item in value:
            current.append(key)

    return current

def remove_if_possible(item):
    if not item in installed:
        return

    deps=find_dependents(item)
    if len(deps)==0:
        if item in installed:
            installed.remove(item)
            print("Removing " + item)
        else:
            print(item + " Not installed")
    else:
        print(item + " Still needed")
        for token in deps:
            remove_if_possible(token)

if __name__ == '__main__':
    fp = open("depends-input.txt", "r")
    lines = fp.readlines()

    for line in lines:
        line=line.strip()
        tokens = line.split(" ")
        actuals=[]
        for token in tokens:
            if token=="":
                continue
            actuals.append(token)

        if actuals[0]=="DEPEND":
            print(line)
            if actuals[1] not in depends.keys():
                depends[actuals[1]]=[]
            for token in actuals[2:]:
                depends[actuals[1]].append(token)
        elif actuals[0]=="INSTALL":
            if actuals[1] in installed:
                print(actuals[1] + " already installed")
            print("Installing " + actuals[1])
            installed.append(actuals[1])
            if actuals[1] in depends.keys():
                for token in depends[actuals[1]]:
                    if token in installed:
                        continue
                    print("Installing " + token)
                    installed.append(token)

        elif actuals[0]=="LIST":
            for token in installed:
                print(token)
        elif actuals[0]=="REMOVE":
            if actuals[1] in depends.keys():
                for token in depends[actuals[1]]:
                    remove_if_possible(token)
            if actuals[1] in installed:
                print("Removing " + actuals[1])
