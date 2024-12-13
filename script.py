#making the blocks
class Create_Block:
    #used to represent a single block of memory
    def __init__(self, size): #initialize a memory block with a specific size
        self.size = size
        self.p_id = None
        #none means the block is free

    def is_free(self): #returns true when the block has no process assigned to it
        return self.p_id is None

#manage created blocks with worst fit memory algo
class Worstfit_Algorithm:
    #used to manage memory allocation using worst fit algo
    def __init__(self, block_sizes): #take a list of block sizes as input

        self.blocks = [Create_Block(size) for size in block_sizes] 
        #creates a list of memory block instances one for each specific block size
        #list of initial block sizes can be changed on the code which first call to this class on the bottom

    #allocate memory to a process using worst fit algo
    def add_process(self, p_id, p_size):

        
        #go through the free blocks to find the largest free block to fit the process
        largest_block = None
        for block in self.blocks:
            if block.is_free() and block.size >= p_size: 
                if largest_block is None or block.size > largest_block.size:
                    largest_block = block

        if largest_block:
            largest_block.p_id = p_id
            remaining_size = largest_block.size - p_size
            if remaining_size > 0:
                #cut the block to assign exact size and leave remaining space as free in a new block
                largest_block.size = p_size
                self.blocks.append(Create_Block(remaining_size))
            print(f"Process {p_id} added with size {p_size}KB.")
        else:
            #combin free blocks if no suitable block is found previously
            self.combinfree()

            #retry finding the largest block after combining space
            largest_block = None
            for block in self.blocks:
                if block.is_free() and block.size >= p_size:
                    if largest_block is None or block.size > largest_block.size:
                        largest_block = block

            if largest_block:
                largest_block.p_id = p_id
                remaining_size = largest_block.size - p_size
                if remaining_size > 0:
                    
                    largest_block.size = p_size
                    self.blocks.append(Create_Block(remaining_size))
                print(f"Process {p_id} added with size {p_size}KB.")
            else:
                print(f"Adding error. not enough memory space to add process {p_id} with size {p_size}KB.")

#merge adjecent free blocks into larger single block. initiatd when not enough free space is found to add a process
    def combinfree(self):
        i = 0

        #iterate through the blocks
        while i < len(self.blocks) - 1:
            if self.blocks[i].is_free() and self.blocks[i + 1].is_free(): #check near by adjecent blocks. if both blocks are free
                self.blocks[i].size += self.blocks[i + 1].size #merge them
                del self.blocks[i + 1] #remove the second block
            else:
                i += 1
        print("Free blocks combind.")


    #used to free a process from a memory block
    def free_process(self, p_id):
        freed = False
        for block in self.blocks:
            if block.p_id == p_id: #try to find the block with a process id to match
                block.p_id = None #if found set p_id to non on the block
                freed = True
                print(f"Process {p_id} has been freed.")
        if not freed:
            print(f"Freeing error. process {p_id} not found.")

    

    #view the current state of the memory blocks. size and availability
    def view_memory_status(self):
        print("\nMemory Status:")
        for idx, block in enumerate(self.blocks): #iterate through all the blocks and print it
            status = "Free" if block.is_free() else f"Process {block.p_id}"
            print(f"Block {idx + 1}: Size {block.size} KB, Status: {status}")



#interactive console to manipulate memory blocks
if __name__ == "__main__":
    #create a WFMM instance and make 5 blocks with specified sizes
    memory_manager = Worstfit_Algorithm([100, 200, 300, 400, 500])

    while True:
        print("\nOptions:")
        print("1. Add process")
        print("2. Free process")
        print("3. View memory status")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            p_id = input("Enter process ID: ")
            p_size = int(input("Enter process size(KB): "))
            memory_manager.add_process(p_id, p_size)
        elif choice == "2":
            p_id = input("Enter process ID to free: ")
            memory_manager.free_process(p_id)
        elif choice == "3":
            memory_manager.view_memory_status()
        elif choice == "4":
            break #close the program
        else:
            print("Unknown command. Try again.")
