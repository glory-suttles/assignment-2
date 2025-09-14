# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
first_node = Node ("Julie")

'''
    A class representing a node in a linked list.
        Attributes:
            name (str): The name of the customer.
            next (Node): A reference to the next node in the list.
        '''
        
        


# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None 
        print("New Waitlist:")
    def add_front(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def print_list(self):
        current = self.head
        if not current:
            print("Waitlist is empty.")
        else:
            while current:
                print(current.name)
                current= current.next
    def remove(self, name):
        if self.head.name == name:
            removed_name = self.head.name
            self.head = self.head.next
            return removed_name

        current = self.head
        while current.next:
            if current.next.name == name:
                removed_name = current.next.name
                current.next = current.next.next
                return removed_name
            current = current.next
          
    def add_end(self, name):
        new_node = Node (name)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

new_list = LinkedList()
new_list.add_front("Trevor")
new_list.add_front("Julie")
new_list.remove("Trevor")
new_list.add_end("Trevor")
new_list.print_list()


''' 
   A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    


def waitlist_generator():
    user_input = LinkedList()
    # Create a new linked list instance

    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            user_input.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            user_input.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            user_input.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            user_input.print_list()
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work? 
This is how my list works; first a node class is created to serve as the user/customer at hand. 
Then through a class called “Linked List” the functions of customizing (adding, subtracting, and changing the order) these lists are established. 
Once the functionality of the code is set and stone, the user input component is required. By turning the class “Linked List” into an instance, 
the functions can be called whenever the user may need them. 
All of this is called through the function waitlist_generator() and the Waitlist is now being tracked and edited. 
- What role does the head play? 
The head plays a role in the overall order of the list. The head is required in order for the first node to 
be placed. By keeping track of the first node then the rest of the code is able to play out and function. 
- When might a real engineer need a custom list like this? 
An engineer might need a custom list like this if they need ways to organize the task at hand. If they need to add or subtract to their list this code 
would give them that ability easily. It also would be able to keep track of the process through whatever they are working on whether it be through 
tools, systems, or small details.  
'''
