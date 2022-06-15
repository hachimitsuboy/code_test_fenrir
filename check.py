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
        # print("閉じかっこ: " + input)
        # print("popValue: " + popValue)
        result = check(popValue, input)
        # print(result)
        if(not result):
            # print("false")
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
            # print("stack: " + i)
            value = convert(i)
            stack.append(value)
            # print("convert stack: " + str(stack))
            count += 1
            # print(count)
            continue

        else:
            result = isValidEntry(i, stack)
            if(result):
                count += 1
                # print(count)
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
