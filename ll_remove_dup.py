class Node:

    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:

    def __init__(self, head):
        self.head= head
    #The following method, removes the duplicates using the set () function
    def remove_dupes(self):
        values=[]
        current= self.head # start from the head node and call it current
        while current: # as long as current is not None
            values.append(current.data) # append the data of current to the values list
            current= current.next # update the current "current" to the next node
        values=list(set(values)) # the set function removes the duplicates from the values list
        
        # The following steps rebuild the linked list
        if values: # as long as values is not empty
            self.head = Node(values[0]) #create a Node object and assign the first element in values to the variable self.head
            current = self.head # call the start of the head node current
            for value in values[1:]: # loop for every element(value) in the values list starting form index 1 and onward
                new_node = Node(value) # create a new Node with that value and store it in new_node
                current.next = new_node #link the previous current node to the new one
                current = new_node # update the current "current" to the next node

    #The following method manually removes the duplicates
    def manual_remover(self):
        elements=[]
        current= self.head # start from the head node and call it current
        while current: # as long as current is not empty
            elements.append(current.data) #append the data of current to the elements list
            current= current.next # update the current "current" to the next one
        unique_elements=[] # create a new list to store the unique data
        for value in elements: #for every element (called value) in the elements list
            if value not in unique_elements: #ask if the value hasn't been added before
                unique_elements.append(value)# add value to the unique_elements list
        
        #the following steps rebuild the linked list
        if unique_elements: # as long as unique_elements is not empty
            self.head= Node(unique_elements[0]) #create a Node object and assign the first element in the unique_elements to the variable self.head
            current= self.head #call the start of the head node current
            for value in unique_elements[1:]: #loop for every element(value) in the unique_elements list starting form index 1 and onward
                new_node= Node(value)# create a new Node with that value and store it in new_node
                current.next= new_node #link the previous current node to the new one
                current= new_node # update the current "current" to the next node

    # This method prints out the results
    def print(self):
        current= self.head # start from the head node and call it current
        while current: # as long as current is not empty
            print(current.data, end=", ") # print out the data in current and add a comma after each current
            current= current.next # update the current"current" to the next node
        print("None") # indicate that after the end of the list, there's None


                


# Create nodes
n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(3)
n6 = Node(4)

# Link nodes together
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

# Create the LinkedList
linked_list = LinkedList(n1)

# Before removing duplicates
print("Before removing duplicates:")
linked_list.print()

# Remove duplicates manually
linked_list.manual_remover()

# After removing duplicates
print("After manual_remover:")
linked_list.print()
