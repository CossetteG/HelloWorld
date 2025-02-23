
class SList:

    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None
            # self.index = 0

    def __init__ (self):
        self._head = None
        self._tail = None
        self._size = 0
        self._iterator = None

    # def assign_index(self):
    #     curr = self._head
    #     for i in range(self._size):
    #         curr.index  = i
    #         curr = curr.next

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        curr = self._head
        prev = self._head
        inserting = self.SListNode(value)

        if (self._head == None):
            self._head = inserting
            self._tail = inserting
            self._size += 1
            # self.assign_index()
            return
        elif(value < self._head.value): 
            inserting.next = self._head
            self._head = inserting
            self._size += 1
            return
            

        while(value >= curr.value):
            if (curr == self._tail):
                break
            prev = curr
            curr = curr.next

        if ((curr == self._tail) and (value >= curr.value)):
            self._tail.next = inserting
            self._tail = inserting
        else:
            prev.next = inserting
            inserting.next = curr

        self._size += 1
        # self.assign_index()
            
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        curr = self._head
        for i in range(self._size):
            if (curr.value == value):
                return curr
            curr = curr.next
        return None

    '''Remove the first occurance of value.'''
    def remove(self, value):
        curr = self._head
        prev = self._head

        while(value != curr.value):
            if (curr == self._tail):
                print("remove: item not found")
                return None
            prev = curr
            curr = curr.next

        if (curr == self._head):
            self._head = self._head.next
        elif (curr == self._tail):
            self._tail = prev
        else:
            prev.next = curr.next
            
        self._size -= 1
        return curr.value
        

    '''Remove all instances of value'''
    def remove_all(self, value):
        curr = self._head
        prev = self._head
        size = int(self._size)

        for i in range(size):
            if (curr.value == value):
                if (curr == self._head):
                    self._head = self._head.next
                elif (curr == self._tail):
                    self._tail = prev
                else:
                    prev.next = curr.next
                self._size -= 1
            else: 
                prev = curr 
            curr = curr.next

        return None

    '''Convert the list to a string and return it'''
    def __str__(self):
        strbuild = "["
        curr = self._head

        if (self._size == 0):
            return "(empty list)"
        else:
            for i in range(self._size):
                if (curr == self._tail):
                    strbuild += str(curr.value)
                    strbuild += "]"
                else:
                    strbuild += str(curr.value)
                    strbuild += ", "
                curr = curr.next

        return strbuild

    '''Return an iterator for the list'''
    def __iter__(self):
        self._iterator = self._head
        return self
    
    def __next__(self):
        if (self._iterator == self._tail):
            raise StopIteration
        elif (self._iterator == self._head): 
            temp = self.SListNode("fakenode")
            temp.next = self._head.next 
            self._iterator = temp
            return self._head.value
        else:
            self._iterator = self._iterator.next
            return self._iterator.value

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        try:
            curr = self._head
            for i in range(index):
                curr = curr.next
            return curr.value
        except: 
            print("Index Error: index out of range or not int type")

    def size(self):
        return self._size
    

''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0):
        self._number = self.validate(number, "int")
        self._name = self.validate(name, "str")
        self._credit_hour = self.validate(credit_hour, "float")
        self._grade = self.validate(grade, "grade")
        


    def validate(self, value, typ):
        if (typ == "int"):
            if (type(value) != int):
                raise ValueError("must be int type")
            elif (value < 0):
                raise ValueError("must be greater than 0")
            else:
               return value
        elif (typ == "float"):
            if (type(value) != float):
                raise ValueError("must be float type")
            elif (value < 0.0):
                raise ValueError("must be greater than 0")
            else:
                return value
                
        elif (typ == "grade"):
            if (type(value) != float):
                    raise ValueError("must be float type")
            elif (value < 0.0 or value > 4.0):
                raise ValueError("must be greater than 0 and less than 4")
            else:
                return value
        elif (typ == "str"):
            if (type(value) != str):
                raise ValueError("must be string type")
            else:
                return value

    def number(self):
        return self._number
    
    # def number(self, value):
    #     self._number = self.validate(value, "int")
    #     return None
    
    def name(self):
        return self._name 
    
    # def name(self, value):
    #     self._name = self.validate(value, "str")
    #     return None
    
    def credit_hr(self):
        return self._credit_hour
    
    # def credit_hr(self, value):
    #     self._credit_hour = self.validate(value, "float")
    #     return None
    
    def grade(self):
        return self._grade 
    
    # def grade(self, value):
    #     self._grade = self.validate(value, "grade")
    #     return None
  
    def __eq__(self, other):
        if (self._number == other.number()):
            return True 
        else:
            return False
      
    def __ne__(self, other):
        if (self._number != other.number()):
            return True 
        else:
            return False
      
    def __lt__(self, other):
        if (self._number < other.number()):
            return True 
        else:
            return False
      
    def __gt__(self, other):
        if (self._number > other.number()):
            return True 
        else:
            return False
      
    def __le__(self, other):
        if (self._number <= other.number()):
            return True 
        else:
            return False
      
    def __ge__(self, other):
        if (self._number >= other.number()):
            return True 
        else:
            return False
      
    def __str__(self):
        strbuild = "cs"
        strbuild += str(self._number)
        strbuild += " "
        strbuild += self._name
        strbuild += " Grade: "
        strbuild += str(self._grade)
        strbuild += " Credit Hours: "
        strbuild += str(self._credit_hour)
        return strbuild

# from slist import SList
# from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, lyst.size()  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True

def main():
    mylist = SList()
    mylist.insert(1)
    mylist.insert(6)
    mylist.insert(3)
    mylist.insert(6)
    mylist.insert(4)
    mylist.insert(0)

    print(mylist)

    mylist.remove_all(8)
    print(is_sorted(mylist))

    print(mylist)

    course1 = Course(1234, "taking care of birds", 3.0, 3.5)
    print(course1)
    print(str(course1))

    # print(course1.name())
    # print(course1.number())
    # print(course1.grade())
    # print(course1.credit_hr())

    course2 = Course(2345, "taking care of cats", 3.0, 3.0)
    course3 = Course(567, "taking care of dogs", 3.0, 4.0)

    courselist = SList()
    courselist.insert(course1)
    print(courselist)

    courselist.remove(course1)
    print(courselist)

    print(course3 == course2)
    print(course3 != course2)

  
if __name__ == "__main__":
    main()