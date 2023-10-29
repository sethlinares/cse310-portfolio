extern crate rand;
use rand::Rng;
use rand::distributions::Alphanumeric;
use std::collections::HashMap;


// Declare the PasswordEntry struct
struct PasswordEntry {

    username: String,
    password: String,

}

// Implement methods for PasswordEntry
impl PasswordEntry {

    fn display_partial(&self) -> String {
        let visible_chars = 3; //
        let hidden_part = "*".repeat(self.password.len() - (2 * visible_chars)); // String literal -> String via repeat()

        // Return a String by formatting the string slices together with the String
        format!("{}{}{}", &self.password[..visible_chars], hidden_part, &self.password[self.password.len() - visible_chars..])

    }

}

// Function to add a new password entry
fn add_password_entry(password_db: &mut HashMap<String, PasswordEntry>) {

    let mut website = String::new();
    let mut username = String::new();
    let mut password = String::new();

    println!("\nEnter website:");
    match std::io::stdin().read_line(&mut website) { // Result<T, E> is returned, we need to check if we get OK (T) or an error(E)
        Ok(_) => { // Do nothing if it's okay, we'll just collect the input to password

        }

        Err(e) => { // If there's an error then it'll get printed
            println!("Error reading your input: {}", e);
        }
    }
    println!("\nEnter username:");
    match std::io::stdin().read_line(&mut username) {
        Ok(_) => {
        }

        Err(e) => {
            println!("Error reading your input: {}", e);
        }
    }

    println!("\nWould you like to:");
    println!("1. Enter your own password");
    println!("2. Generate a random password");

    let mut choice = String::new();

    match std::io::stdin().read_line(&mut choice) {
        Ok(_) => {
        }

        Err(e) => {
            println!("Error reading your input: {}", e);
        }
    }

    match choice.trim() {
        "1" => {
            println!("\nEnter password (minimum 8 characters):");
            match std::io::stdin().read_line(&mut password) {
                Ok(_) => {
                }

                Err(e) => {
                    println!("Error reading your input: {}", e);

                }
            }

            if password.trim().len() < 8 {
                println!("\nPassword too short. Please enter at least 8 characters.\n");
                return;  // Exit function if pass is too short
            }
        },

        "2" => {
            password = generate_password(12);  // Generate pass of x length, 12 here
            println!("\nGenerated password: {}", password); // Display the password we just stored
        },

        _ => {
            println!("\nInvalid choice.\n"); // Just catching errors here
            return;
        }
    }

    password_db.insert(website.trim().to_string(), PasswordEntry {
        username: username.trim().to_string(),
        password: password.trim().to_string(),
    });

    println!("\nPassword entry added successfully!\n");
}



fn generate_password(length: usize) -> String {
    rand::thread_rng() //random number generator
        .sample_iter(&Alphanumeric) // Will produce random values of A-Z, a-z, and 0-9
        .take(length)// Enforces the length we want
        .map(char::from) // Need to convert from u8 to unicode characters to allow us to make a String
        .collect() // Collects the chars into a String and we are returning since we have no ;
}

// Function to retrieve a password entry
fn retrieve_password_entry(password_db: &HashMap<String, PasswordEntry>) {
    // Check if the database is empty
    if password_db.is_empty() {
        println!("\nNo entries found.\n");
        return;
    }

    println!("\nStored websites:");
    let mut counter = 1;
    let mut websites: Vec<&String> = Vec::new();

    for website in password_db.keys() {
        println!("{}. {}", counter, website);
        websites.push(website);
        counter += 1;
    }

    println!("\nEnter the number of the website to retrieve:");
    let mut choice = String::new();

    match std::io::stdin().read_line(&mut choice) {
        Ok(_) => {
        }

        Err(e) => {
            println!("Error reading your input: {}", e);
        }
    }


    let choice: usize = match choice.trim().parse() { // Take choice string and parse it to make it a number
        Ok(num) =>  {
            num
        },

        Err(_) => { // unimportant to return an error
            println!("\nInvalid choice.\n");
            return;
        }
    };

    if choice > 0 && choice <= websites.len() { // Look for the entry corresponding to our choice in password_db
        let entry = match password_db.get(websites[choice - 1]) {
            Some(pass_entry) => {
                pass_entry
            }

            None => {
                println!("No entry found for the selected website.");
                return;
            }
        };


        println!("\nWebsite: {}", websites[choice - 1]);
        println!("Username: {}", entry.username);

        // New code: ask the user if they want to see the full password or obscured
        println!("\nWould you like to:");
        println!("1. See the obscured password");
        println!("2. See the full password");

        let mut display_choice = String::new();
        match std::io::stdin().read_line(&mut display_choice) {
            Ok(_) => {

            }

            Err(e) => {
                println!("Error reading your input: {}", e);
            }
        }

        match display_choice.trim() {
            "1" => {
                println!("\nPassword: {}\n", entry.display_partial()) // if 1, then give obscured pass
            }

            "2" => {
                println!("\nPassword: {}\n", entry.password) // if 2 then give full pass so they can copy it
            }

            _ => { // default case, invalid
                println!("\nInvalid display choice.\n")
            }
        }
    }

    else {
        println!("\nInvalid choice.\n");
    }
}



// Main function
fn main() {
    let mut password_db: HashMap<String, PasswordEntry> = HashMap::new(); // Create hashmap (Dictionary)

    loop { // Loop until 3 is called. This loop is basically a `while true` loop but shorter
        println!("Select an option:");
        println!("1. Add a password entry");
        println!("2. Retrieve a password entry");
        println!("3. Exit");

        let mut choice = String::new();
        match std::io::stdin().read_line(&mut choice) {
            Ok(_) => {

            }

            Err(e) => {
                println!("Error reading your input: {}", e);
            }
        }

        match choice.trim() {
            "1" => add_password_entry(&mut password_db), // create password entry
            "2" => retrieve_password_entry(&password_db), // get passwords
            "3" => break, // exit program
            _ => println!("Invalid choice. Try again.\n"), // default
        }

    }
}
