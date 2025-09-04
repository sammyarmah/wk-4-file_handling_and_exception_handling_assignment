#### 📂 File Read & Write Program

This project demonstrates **basic file handling in Python**. It shows how to:

* ✅ Create a new file and write text into it
* ✅ Read the contents of an existing file
* ✅ Ask the user to enter a filename and handle errors gracefully if the file does not exist

---

#### 🚀 How It Works

1. **File Creation**
   The program first creates a new file called `randomFile.txt` and writes some text into it.

2. **File Reading**
   It then opens the file in read mode and prints out its contents.

3. **User Input**
   Finally, the program asks the user to enter the name of a file.

   * If the file exists → it opens and displays the content.
   * If the file does not exist → it prints an error message.

---

#### 📝 Example Usage

```bash
Enter the name of the file here.
randomFile.txt
```

Output:

```
File randomFile.txt opened successfully.
This is a new file I am creating
The file is in a pdf format
I have some contents in the file
```

If the file does not exist:

```
Enter the name of the file here.
missing.txt
File not found. Please check the filename.
```

---

#### ⚙️ Requirements

* Python 3.x
* No external libraries required

---

#### 💡 Key Concepts Learned

* Using `open()` with different modes:

  * `'w'` → write mode
  * `'r'` → read mode
* Reading file content with `.read()`
* Exception handling with `try ... except` for missing files
