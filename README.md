# Librebook-LBBK-File-Interpreter

A text file interpreter designed to execute `.LBBK` header instructions, display content, and convert standard `.txt` files into `.lbbk` format.

## 📄 What is a `.LBBK` File?

`.LBBK` is a custom text file format that blends structured instructions with regular text, giving users full control over how the content is displayed. These files include a **header section** at the top that contains commands executed before rendering the rest of the text.

## 🧠 How It Works

The interpreter scans the `.LBBK` file, processes the header commands, and then displays or modifies the content based on those instructions. If the header is incomplete or malformed, it will be treated as plain text.

## 🔧 Header Syntax and Commands

The **header** must end with the marker:

    /@]

Any lines after this marker are considered normal content and not interpreted as commands.

---

### 📌 Commands

#### `IGNORE`

Skips a specified line from the content after the header.

- **Syntax**:  
    IGNORE <line_number>&

- **Example**:  
    IGNORE 3&  
    → This tells the interpreter to skip line 3 in the content.

- **Important**: The `&` is required at the end of the command. It acts as a command terminator and must be present.

---

#### `REPEAT`

Duplicates a specified line from the content a given number of times.

- **Syntax**:  
    REPEAT <line_number>&X<repeat_count>#

- **Example**:  
    REPEAT 10&X2#  
    → This repeats line 10 **two times** in the output.

- **Notes**:
  - `&` ends the line number section.
  - `X` separates the repeat count.
  - `#` marks the end of the command.

---

## ✅ Features

- Parses and executes `.LBBK` header commands
- Converts `.txt` files into `.lbbk` format
- Fully customizable content display
- Simple and readable command syntax

## 🚧 Roadmap / To-Do

- Add support for nested or conditional commands
- Improve error handling for invalid syntax
- Expand the available instruction set

---

## 📁 Example `.lbbk` File

Example input:
IGNORE 2&
REPEAT 5&X3#
/@]
Hello, World!
This line will be ignored.
This is line 3.
This is line 4.
Repeat me!


**Expected output:**
Hello, World!
This is line 3.
This is line 4.
Repeat me!
Repeat me!
Repeat me!
