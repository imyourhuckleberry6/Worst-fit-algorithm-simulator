# Worst-Fit Algorithm simulator

This script simulates a program which uses Worst fit memory management strategies to manage adding and removing processes from its partitions. User is able to add new processes to the partitions, remove existing processes from the partitions as well as view the status of all partitions in this program.

In Worst fit memory allocation algorithm, the process to be assigned go through all the available memory partitions and looks for the largest partition/block. Then the process is placed in that partition. Depending on the number of available partitions, this can be quicker or slower. But due to having to traverse the entire memory partition list eitherway, generally it is a slow process.

In this program for practicality in using Worst fit allocation, when assigning a process to a large partition, the partition is cut into two, one for the process and the rest as free space. Doing this can help lessen the likelihood of fragmentation of the memory. Space for more processes will be available as a new partition while the assigned process takes the necessary space for itself.

# Installation

To run this script, a Computer which has Python language support is required.

You can download and install the latest Python version from: www.python.org before proceeding further.

After installing python, the Module which contains the demonstration of the Worst fit algorithm, can be run through a console program, such as Window’s Command prompt or VS Code terminal.

Apart from these methods to run the script, it can also be accessible through a online code editor/terminal program. Although the guarantee of successful simulation on a browser cannot be fully assured due to the varying factors of each browser. If such methods fail, please run the program locally as intented.

# Features

- Add Processes: User can add a new process to the memory.

- Free Memory: Remove processes from the memory to free up space.

- View Memory Status: View all the available partitions of the modules as well as their sizes and status.

#

Made by M. M. Hettige using Python Language.
