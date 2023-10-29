# Overview

I created a simple Password Manager in Rust that lets you store a website, username, and password. It also lets you retrieve the password for a given website. The program allows you to either create your own password or have the program generate the password for you. If you create your own password you are required to have at least 8 characters. Once you have a password entry, you can then go back to the menu and choose to retrieve the password and username. The program will then ask you for the website you want to retrieve the password for. If the website is found, the program will print out the username and password. Before it prints out the password, you will be prompted to choose between seeing the full password or the obscured password. If you choose the obscured password, the program will print out the password with the first 3 and last 3 characters visible and the rest of the characters will be replaced with asterisks. If you choose the full password, the program will print out the full password so the user can copy it if needed.



The purpose behind writing this Password Manager was to practice Rust and learn more about the language. I wanted to learn more about Rust because I have heard a lot of good things about it and I wanted to see what it was like. I also wanted to learn more about Rust because I have heard that it is a good language for writing low level code. Creating a Password Manager was a good way to practice Rust because it allowed me to use a lot of the language's features. I was able to use structs, vectors, match statements, and so much more. I was also able to use random number and letter generation which was a lot of fun to implement. Overall, I learned a lot about Rust and I am excited to learn more about the language moving forward.


# YouTube Demo

[Password Manager Demo](https://youtu.be/1zA9AWgRcuQ)

# Development Environment

* JetBrains Rust Rover

* Programming Language: Rust

* Libraries: `rand::Rng`, `rand::distributions::Alphanumeric`, `std::collections::HashMap`

# Useful Websites



- [Learn Rust](https://www.rust-lang.org/learn)
- [Rust Playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021)
- [Rust Documentation](https://doc.rust-lang.org/book/)

# Future Work


- Add a feature that allows the user to delete a password entry
- Add encryption to the password entries
- Improve the password generation algorithm
