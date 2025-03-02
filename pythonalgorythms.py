
class Stack:

    class StackNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self._top = None
        self._size = 0
    
    def push(self, item):
        if (item == ' '):
            pass
        else:
            init = self.StackNode(item)
            if (self._size == 0):
                self._top = init
            else:
                init.next = self._top 
                self._top = init 
            self._size +=1

    
    def pop(self):
        if (self._size <= 0):
            raise IndexError("pop- Stack is empty")
        else:
            self._size -=1
            popped = self._top
            self._top = self._top.next
            return popped.value
    
    def top(self):
        if (self._size <= 0):
            raise IndexError("top- Stack is empty")
        else:
            return self._top.value
    
    def size(self):
        return self._size
    
    def clear(self):
        self._top = None
        self._size = 0

    def __str__(self):
        str_bld = ""
        curr = self._top
        for char in range(self._size):
            str_bld += str(curr.value)
            str_bld += " "
            curr = curr.next
        return str_bld
        

# from stack import Stack

def eval_postfix(expr):
    postack = Stack()

    for char in expr:
        if char in "0123456789":
            postack.push(float(char))
        elif(char == ' '):
            pass
        else:
            oper1 = postack.pop()
            oper2 = postack.pop()
            match char:
                case '+':
                    postack.push(oper1 + oper2)
                case '-':
                    postack.push(oper2 - oper1)
                case '*':
                    postack.push(oper1 * oper2)
                case '/':
                    postack.push(oper2 / oper1)
                
    return postack.pop()

def in2post(expr):
    post = ""
    pstack = Stack()

    def check_prec(char):
        if ((char == '/') or (char == '*')):
            return False
        elif ((pstack.top() == '/') or (pstack.top() == '*')):
            return True
        else:
            return True 

    for char in expr:
        if (char == '('):
            pstack.push(char) 
        elif (char in "0123456789"):
            post += char
            post += ' '
        elif (char in "/*-+"):
            while (pstack.size() > 0):
                if ((pstack.top() != '(') & check_prec(char)):
                    post += pstack.pop() 
                    post += ' '
                else:
                    break
            pstack.push(char)
        elif (char == " "):
            pass 
        else: 
            if (char == ')'): 
                post += pstack.pop()
                post += ' '
                while (pstack.top() != '('):
                    post += pstack.pop()
                    post += ' '
                pstack.pop()

    while (pstack.size() > 0):
        post += pstack.pop()
        post += ' '

    return post 

def main():

    # with open("data.txt", "r") as read_file:
        # for expression in read_file.readlines():
        #     postfix = in2post(expression)
        #     answer = eval_postfix(postfix)
        #     print(f"infix: {expression}postfix: {postfix}")
        #     print(f"answer: {answer}")
        #     print()


    # TESTING
    # ma_stack = Stack()

    # ma_stack.push(9)
    # ma_stack.push(8)
    # ma_stack.push('a')

    # print(ma_stack)
    # print(ma_stack.pop())
    # print(ma_stack.pop())
    
    # print(ma_stack.top())
    # print(ma_stack.top())

    # print(ma_stack.size())

    # ma_stack.clear()
    # print(ma_stack.top())

    expr1 = "((8+3)*(2-7))"
    expr2 = "((8+3)*2)-7"
    expr3 = "(8*5)+((3-2)-7*3)"
    expr4 = "((8*5+3)-7)-(5*3)"
    expr5 = "7*9+7-5*6+3-4"
    expr6 = "8 * (5+3)"
    
    sol1= in2post(expr1)
    sol2= in2post(expr2)
    sol3= in2post(expr3)
    sol4= in2post(expr4)
    sol5= in2post(expr5)
    sol6= in2post(expr6)

    print(sol1)
    print(sol2)
    print(sol3)
    print(sol4)
    print(sol5)
    print(sol6)

    print(eval_postfix(sol1))
    print(eval_postfix(sol2))
    print(eval_postfix(sol3))
    print(eval_postfix(sol4))
    print(eval_postfix(sol5))
    print(eval_postfix(sol6))


    return 0
    
if __name__=="__main__":
    main()