
// These are the libraries that are included in the program. 
//The iostream lib is used for user input/output, the vector lib is used for vectors, the string lib is used for strings, and the fstream lib is used for file input/output
#include <iostream> 
#include <vector>
#include <string>
#include <fstream> 


class Task { // This is a class that represents a task
public:

    // This is the constructor for the class, it takes a string as a parameter and sets the description to that string and sets isDone to false
    explicit Task(std::string desc) : description(std::move(desc)), isDone(false) { // Uses member initializer list to initialize the variables

    } 

    std::string description;  // A string to store the description of the task
    bool isDone;  // A boolean to store whether the task is done or not

    // This function marks the task as done, it does not return anything as it is a void function
    void markAsDone() {
        isDone = true;
    }
};


class TodoList { // This is a class that represents a list of tasks


private:
    std::vector<Task> tasks;  // Vector to store tasks (vector is used for efficiency, it is a dynamic array)


public:
    // Adds a task to the list
    void addTask(std::string desc) {
        tasks.emplace_back(std::move(desc));  

        // emplace_back is a function that is used to add an element to the end of a vector. It is more efficient than push_back as it avoids copying the element.
    }

    // Removes a task by index
    void removeTask(int index) {
        if(index >= 0 && index < tasks.size()) {  // Make sure the index given is correct
            tasks.erase(tasks.begin() + index);  // Remove the task
        }
    }

    // Marks a task as done by index
    void markTaskAsDone(int index) {
        if(index >= 0 && index < tasks.size()) {  // Make sure the index given is correct
            tasks[index].markAsDone();  // Mark the task as done
            std::cout << "\nMarked task " << index + 1 << " as done.\n\n";
        } 
        
        else {
            std::cout << "\nInvalid task number.\n\n";
        }
    }

    // Displays all the tasks
    void displayTasks() {
        std::cout << "\nTasks:\n";
        if (tasks.empty()) {  // Check if there are no tasks
            std::cout << "No tasks available.\n\n";
        } 
        
        else {
            for(int i = 0; i < tasks.size(); ++i) {  // Loop through tasks
                // Display each task with its number, status, and description
                std::cout << i + 1 << ". " << (tasks[i].isDone ? "[Done] " : "") << tasks[i].description << "\n";
            }
            std::cout << "\n";
        }
    }

    // This function exports the tasks to a file. This satisfies the requirement of the stretch challenge for this module.
    void exportToFile() {
        std::ofstream file("todo_list.txt");  // Here, we create an "ofstream" object that writes the tasks to a file named "todo_list.txt"

        if (file.is_open()) {  

            file << "To-do List:\n\n";

            for(int i = 0; i < tasks.size(); ++i) {  // Loop through tasks

                // Add the number, status, and description to the file for each task
                file << i + 1 << ". " << (tasks[i].isDone ? "[Done] " : "[Not Done] ") << tasks[i].description << "\n";
            }


            file.close();  
            std::cout << "\nTasks exported to todo_list.txt\n\n";
        } 
        
        
        else {
            std::cout << "\nUnable to create file.\n\n";
        }
    }


};

// Function to display the menu options (Cleaner than having it in the main function imo)
void displayMenu() {
    std::cout << "1. Add Task\n";
    std::cout << "2. Remove Task\n";
    std::cout << "3. View Tasks\n";
    std::cout << "4. Mark Task as Done\n";
    std::cout << "5. Export To-do List to file\n";
    std::cout << "6. Exit\n";
    std::cout << "Choose an option: ";
}

// Main function, where the program starts
int main() {
    TodoList myTasks;  // Create a TodoList object

    // Continuous while loop to display menu and get user input
    while(true) {
        displayMenu();
        int choice;
        std::cin >> choice; // Get user input for choice

        switch(choice) { // This switch statement is used to determine which function to call based on the user's choice
            case 1: {
                std::cout << "\nEnter task description: ";
                std::string desc;
                std::cin.ignore(); // Need to add so that the string doesn't have a newline character in it
                std::getline(std::cin, desc);
                myTasks.addTask(desc);
                std::cout << "\n";
                break;
            }

            case 2: {
                myTasks.displayTasks();  // Display all tasks
                std::cout << "Enter task number to remove: ";
                int index;
                std::cin >> index;
                myTasks.removeTask(index - 1);
                std::cout << "\n";
                break;
            }

            case 3: {
                myTasks.displayTasks();
                break;
            }

            case 4: {
                myTasks.displayTasks();  // Display all tasks
                std::cout << "Enter task number to mark as done: ";
                int index;
                std::cin >> index;
                myTasks.markTaskAsDone(index - 1);
                break;
            }

            case 5: {

                myTasks.exportToFile();  // Call the exportToFile function to export the tasks to a file
                break;
            }

            case 6:
                return 0; // 0 is returned to exit the program

            default: // If the user enters an invalid choice (anything not 1-6), display an error message
                std::cout << "\nInvalid choice. Try again.\n\n";
        }
    }
}
