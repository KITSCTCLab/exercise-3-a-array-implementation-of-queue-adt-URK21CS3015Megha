class Solution:


    def _init_(self, size):


        self.stack = [None]*size
        self.queue = [None]*size
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1


    def is_stack_empty(self):

        return self.top==-1


    def is_queue_empty(self):

        return self.rear<self.front


    def is_stack_full(self):

        return self.top==(self.size-1)


    def is_queue_full(self):

        return self.rear==(self.size-1)


    def push_character(self, character):

        if self.is_stack_full()==False:

            self.top+=1

            self.stack[self.top]=character



    def enqueue_character(self, character):

        if self.is_queue_full()==False:

            if self.front==-1:

                self.front=0

            self.rear+=1

            self.queue[self.rear]=character



    def pop_character(self):

        if self.is_stack_empty()==False:

            x=self.stack[self.top]

            self.top-=1

            return x



    def dequeue_character(self):

        if self.is_queue_empty()==False:

            x=self.queue[self.front]

            if self.front==self.rear:

                self.front=-1

                self.rear=-1

            else:

                self.front+=1

            return x



# read the string text

text = input()


# find the length of text

length_of_text = len(text)


# Create the Solution class object

solution = Solution(length_of_text)


# push/enqueue all the characters of string text to stack

for index in range(length_of_text):

    solution.push_character(text[index])

    solution.enqueue_character(text[index])


is_palindrome = True

for i in range(int(length_of_text/2)):

    if(solution.pop_character()!=solution.dequeue_character()):

        is_palindrome=False



# finally print whether string text is palindrome or not.

if is_palindrome:

    print("The word, " + text + ", is a palindrome.")

else:

    print("The word, " + text + ", is not a palindrome.")
