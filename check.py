import sys
args = sys.argv


def convert(input):
    if (input == "("):
        return ")"
    elif(input == "{"):
        return "}"
    elif(input == "["):
        return "]"


def check(stackValu, input):
    if(stackValu != input):
        return False
    else:
        return True


def isValidEntry(input, stack):
    if(input == ")" or input == "}" or input == "]"):
        popValue = stack.pop()
        result = check(popValue, input)
        if(not result):
            return False
        else:
            return True

    else:
        print("入力エラー: " + input)
        print("false")
        return False


def stack(input):
    stack = []
    goal = len(input)
    count = 0
    for i in input:
        if(i == "(" or i == "[" or i == "{"):
            value = convert(i)
            stack.append(value)
            count += 1
            continue

        else:
            result = isValidEntry(i, stack)
            if(result):
                count += 1
            else:
                print("false")
                break

        if(count == goal):
            print("true")


def input():

    inputword = args[1]
    print("input: " + inputword)
    stack(inputword)


input()
