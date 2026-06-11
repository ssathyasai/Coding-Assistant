import json

samples = [
    # ── Python ──────────────────────────────────────────────────────────────
    {
        "topic": "factorial",
        "questions": [
            "Write Python program for factorial",
            "Create factorial program in Python",
            "Find factorial using loop in Python",
            "Factorial using recursion in Python",
            "How to calculate factorial in Python?",
        ],
        "answer": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))  # 120",
    },
    {
        "topic": "palindrome",
        "questions": [
            "Write Python palindrome program",
            "Check palindrome in Python",
            "Python string palindrome example",
            "How to check if a string is palindrome in Python?",
            "Palindrome check using loop in Python",
        ],
        "answer": 'text = "madam"\nif text == text[::-1]:\n    print("Palindrome")\nelse:\n    print("Not Palindrome")',
    },
    {
        "topic": "bubble sort",
        "questions": [
            "Write Python program for bubble sort",
            "Implement bubble sort in Python",
            "Bubble sort algorithm Python",
            "Sort list using bubble sort Python",
            "How does bubble sort work in Python?",
        ],
        "answer": "def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n    return arr\n\nprint(bubble_sort([64, 34, 25, 12, 22]))",
    },
    {
        "topic": "fibonacci",
        "questions": [
            "Write Python program for Fibonacci series",
            "Print Fibonacci sequence in Python",
            "Fibonacci using loop in Python",
            "Fibonacci series using recursion Python",
            "How to generate Fibonacci numbers in Python?",
        ],
        "answer": "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        print(a, end=' ')\n        a, b = b, a + b\n\nfibonacci(10)",
    },
    {
        "topic": "list operations",
        "questions": [
            "What is Python list?",
            "How to add elements to a list in Python?",
            "How to remove elements from a list in Python?",
            "Python list append and remove example",
            "How to sort a list in Python?",
        ],
        "answer": "my_list = [3, 1, 4, 1, 5]\nmy_list.append(9)      # add\nmy_list.remove(1)      # remove first 1\nmy_list.sort()         # sort in place\nprint(my_list)",
    },
    {
        "topic": "dictionary",
        "questions": [
            "What is a Python dictionary?",
            "How to create a dictionary in Python?",
            "How to access dictionary values in Python?",
            "How to iterate over a dictionary in Python?",
            "Add and delete keys in Python dictionary",
        ],
        "answer": "student = {'name': 'Alice', 'age': 20, 'grade': 'A'}\nprint(student['name'])          # access\nstudent['city'] = 'Delhi'       # add key\ndel student['grade']            # delete key\nfor k, v in student.items():\n    print(k, ':', v)",
    },
    {
        "topic": "file handling",
        "questions": [
            "How to read a file in Python?",
            "How to write to a file in Python?",
            "Python file open and close example",
            "Read lines from file in Python",
            "Write list to file in Python",
        ],
        "answer": "# Write\nwith open('data.txt', 'w') as f:\n    f.write('Hello World\\n')\n\n# Read\nwith open('data.txt', 'r') as f:\n    for line in f:\n        print(line.strip())",
    },
    {
        "topic": "exception handling",
        "questions": [
            "How to handle exceptions in Python?",
            "Python try except example",
            "Explain try except finally in Python",
            "How to raise an exception in Python?",
            "Python exception handling best practices",
        ],
        "answer": "try:\n    result = 10 / 0\nexcept ZeroDivisionError as e:\n    print('Error:', e)\nexcept Exception as e:\n    print('Unexpected error:', e)\nelse:\n    print('Success:', result)\nfinally:\n    print('Always runs')",
    },
    {
        "topic": "list comprehension",
        "questions": [
            "What is list comprehension in Python?",
            "Python list comprehension example",
            "Create list using comprehension in Python",
            "Filter list with comprehension in Python",
            "List comprehension vs for loop Python",
        ],
        "answer": "# Squares of even numbers 1-10\nresult = [x**2 for x in range(1, 11) if x % 2 == 0]\nprint(result)  # [4, 16, 36, 64, 100]",
    },
    {
        "topic": "classes and objects",
        "questions": [
            "How to create a class in Python?",
            "Python class and object example",
            "Explain __init__ method in Python",
            "How to use self in Python class?",
            "Create Student class in Python",
        ],
        "answer": "class Student:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def greet(self):\n        print(f'Hi, I am {self.name}, age {self.age}')\n\ns = Student('Alice', 20)\ns.greet()",
    },
    {
        "topic": "inheritance",
        "questions": [
            "What is inheritance in Python?",
            "Python inheritance example",
            "How to use super() in Python?",
            "Create parent and child class in Python",
            "Explain method overriding in Python",
        ],
        "answer": "class Animal:\n    def speak(self):\n        print('Animal speaks')\n\nclass Dog(Animal):\n    def speak(self):\n        print('Dog barks')\n\nd = Dog()\nd.speak()       # Dog barks\nsuper(Dog, d).speak()  # Animal speaks",
    },
    {
        "topic": "lambda functions",
        "questions": [
            "What is lambda in Python?",
            "Python lambda function example",
            "How to use lambda with map in Python?",
            "Lambda with filter in Python",
            "Difference between lambda and def in Python",
        ],
        "answer": "square = lambda x: x ** 2\nprint(square(5))  # 25\n\nnumbers = [1, 2, 3, 4, 5]\nsquares = list(map(lambda x: x**2, numbers))\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(squares)\nprint(evens)",
    },
    {
        "topic": "decorators",
        "questions": [
            "What is a decorator in Python?",
            "Python decorator example",
            "How to create a decorator in Python?",
            "Explain @property decorator in Python",
            "Use decorator to log function calls",
        ],
        "answer": "def logger(func):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.__name__}')\n        result = func(*args, **kwargs)\n        print(f'Done {func.__name__}')\n        return result\n    return wrapper\n\n@logger\ndef add(a, b):\n    return a + b\n\nprint(add(3, 4))",
    },
    {
        "topic": "generators",
        "questions": [
            "What is a generator in Python?",
            "Python generator example",
            "Difference between generator and list in Python",
            "How to use yield in Python?",
            "Create infinite sequence generator in Python",
        ],
        "answer": "def count_up(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\n\nfor num in count_up(5):\n    print(num)",
    },
    {
        "topic": "string methods",
        "questions": [
            "Common Python string methods",
            "How to split a string in Python?",
            "How to join strings in Python?",
            "Python string replace example",
            "How to convert string to uppercase in Python?",
        ],
        "answer": "s = '  Hello World  '\nprint(s.strip())            # 'Hello World'\nprint(s.lower())            # '  hello world  '\nprint(s.upper())            # '  HELLO WORLD  '\nprint(s.replace('World', 'Python'))\nwords = s.strip().split(' ')\nprint('-'.join(words))",
    },
    {
        "topic": "sets",
        "questions": [
            "What is a set in Python?",
            "Python set operations example",
            "Union and intersection of sets in Python",
            "How to remove duplicates using set in Python?",
            "Difference between set and list in Python",
        ],
        "answer": "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(a | b)   # union\nprint(a & b)   # intersection\nprint(a - b)   # difference\n\n# Remove duplicates\nmy_list = [1, 2, 2, 3, 3, 4]\nunique = list(set(my_list))\nprint(unique)",
    },
    {
        "topic": "tuple",
        "questions": [
            "What is a tuple in Python?",
            "Difference between list and tuple in Python",
            "How to create a tuple in Python?",
            "Tuple unpacking in Python example",
            "When to use tuple instead of list?",
        ],
        "answer": "# Tuples are immutable\ncoords = (10, 20)\nx, y = coords          # unpacking\nprint(x, y)\n\n# Single element tuple\nsingleton = (42,)\nprint(type(singleton))  # <class 'tuple'>",
    },
    {
        "topic": "modules and imports",
        "questions": [
            "How to import a module in Python?",
            "Python import example",
            "Difference between import and from import in Python",
            "How to create your own module in Python?",
            "What is __name__ == '__main__' in Python?",
        ],
        "answer": "import math\nfrom datetime import datetime\n\nprint(math.sqrt(16))       # 4.0\nprint(datetime.now())      # current datetime\n\n# Custom module: save as mymodule.py\ndef greet(name):\n    return f'Hello, {name}'\n\n# In another file:\n# import mymodule\n# print(mymodule.greet('Alice'))",
    },
    {
        "topic": "error types",
        "questions": [
            "What is IndexError in Python?",
            "How to fix NameError in Python?",
            "Explain TypeError in Python",
            "What causes ValueError in Python?",
            "Common Python errors and how to fix them",
        ],
        "answer": "# IndexError - index out of range\ntry:\n    lst = [1, 2, 3]\n    print(lst[10])\nexcept IndexError:\n    print('List index out of range')\n\n# TypeError - wrong type operation\ntry:\n    result = '5' + 5\nexcept TypeError:\n    print('Cannot add str and int')\n\n# ValueError\ntry:\n    num = int('abc')\nexcept ValueError:\n    print('Invalid literal for int')",
    },
    {
        "topic": "recursion",
        "questions": [
            "What is recursion in Python?",
            "Python recursion example",
            "Write recursive function in Python",
            "Difference between recursion and iteration",
            "Tower of Hanoi in Python",
        ],
        "answer": "def sum_list(lst):\n    if not lst:\n        return 0\n    return lst[0] + sum_list(lst[1:])\n\nprint(sum_list([1, 2, 3, 4, 5]))  # 15",
    },
    # ── Java ────────────────────────────────────────────────────────────────
    {
        "topic": "java hello world",
        "questions": [
            "Write Hello World in Java",
            "Java first program example",
            "How to print in Java?",
            "Basic Java program structure",
            "Java main method example",
        ],
        "answer": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
    },
    {
        "topic": "java factorial",
        "questions": [
            "Write Java factorial program",
            "Java factorial using loop",
            "Factorial using recursion in Java",
            "Java program to find factorial of a number",
            "Calculate factorial in Java",
        ],
        "answer": "public class Factorial {\n    static int factorial(int n) {\n        if (n == 0) return 1;\n        return n * factorial(n - 1);\n    }\n    public static void main(String[] args) {\n        System.out.println(factorial(5)); // 120\n    }\n}",
    },
    {
        "topic": "java arrays",
        "questions": [
            "How to declare an array in Java?",
            "Java array example",
            "How to iterate over array in Java?",
            "Java array sorting example",
            "Find max element in Java array",
        ],
        "answer": "import java.util.Arrays;\npublic class ArrayExample {\n    public static void main(String[] args) {\n        int[] arr = {5, 3, 8, 1, 9};\n        Arrays.sort(arr);\n        System.out.println(Arrays.toString(arr));\n        System.out.println('Max: ' + arr[arr.length - 1]);\n    }\n}",
    },
    {
        "topic": "java OOP",
        "questions": [
            "Explain OOP concepts in Java",
            "Java class and object example",
            "What is encapsulation in Java?",
            "Java inheritance example",
            "What is polymorphism in Java?",
        ],
        "answer": "// Encapsulation example\npublic class Student {\n    private String name;\n    private int age;\n\n    public Student(String name, int age) {\n        this.name = name;\n        this.age = age;\n    }\n\n    public String getName() { return name; }\n    public int getAge() { return age; }\n\n    public static void main(String[] args) {\n        Student s = new Student('Alice', 20);\n        System.out.println(s.getName() + ' is ' + s.getAge());\n    }\n}",
    },
    {
        "topic": "java interface",
        "questions": [
            "What is interface in Java?",
            "Java interface example",
            "Difference between abstract class and interface in Java",
            "How to implement interface in Java?",
            "Java multiple interface implementation",
        ],
        "answer": "interface Shape {\n    double area();\n}\n\nclass Circle implements Shape {\n    double radius;\n    Circle(double r) { this.radius = r; }\n\n    public double area() {\n        return Math.PI * radius * radius;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Shape c = new Circle(5);\n        System.out.println(c.area());\n    }\n}",
    },
    {
        "topic": "java collections",
        "questions": [
            "What is ArrayList in Java?",
            "Java ArrayList example",
            "Difference between ArrayList and LinkedList in Java",
            "How to use HashMap in Java?",
            "Java HashMap example",
        ],
        "answer": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        // ArrayList\n        ArrayList<String> list = new ArrayList<>();\n        list.add('Alice');\n        list.add('Bob');\n        System.out.println(list);\n\n        // HashMap\n        HashMap<String, Integer> map = new HashMap<>();\n        map.put('age', 20);\n        System.out.println(map.get('age'));\n    }\n}",
    },
    # ── SQL ─────────────────────────────────────────────────────────────────
    {
        "topic": "sql select",
        "questions": [
            "What is SQL SELECT statement?",
            "How to select all records in SQL?",
            "SQL SELECT with WHERE clause",
            "SQL query to get specific columns",
            "Select distinct values in SQL",
        ],
        "answer": "-- Select all\nSELECT * FROM students;\n\n-- Select specific columns\nSELECT name, age FROM students;\n\n-- With condition\nSELECT * FROM students WHERE age > 18;\n\n-- Distinct\nSELECT DISTINCT city FROM students;",
    },
    {
        "topic": "sql joins",
        "questions": [
            "What is SQL JOIN?",
            "Explain INNER JOIN in SQL",
            "Difference between INNER JOIN and LEFT JOIN",
            "SQL JOIN example with two tables",
            "What is RIGHT JOIN in SQL?",
        ],
        "answer": "-- INNER JOIN: only matching rows\nSELECT s.name, c.course_name\nFROM students s\nINNER JOIN courses c ON s.id = c.student_id;\n\n-- LEFT JOIN: all from left + matching from right\nSELECT s.name, c.course_name\nFROM students s\nLEFT JOIN courses c ON s.id = c.student_id;",
    },
    {
        "topic": "sql aggregates",
        "questions": [
            "What are aggregate functions in SQL?",
            "How to use COUNT in SQL?",
            "SQL SUM and AVG example",
            "GROUP BY in SQL example",
            "SQL HAVING clause example",
        ],
        "answer": "SELECT department, COUNT(*) AS total, AVG(salary) AS avg_salary\nFROM employees\nGROUP BY department\nHAVING COUNT(*) > 5\nORDER BY avg_salary DESC;",
    },
    {
        "topic": "sql crud",
        "questions": [
            "How to insert data in SQL?",
            "SQL INSERT example",
            "How to update record in SQL?",
            "SQL DELETE example",
            "SQL CRUD operations example",
        ],
        "answer": "-- INSERT\nINSERT INTO students (name, age) VALUES ('Alice', 20);\n\n-- UPDATE\nUPDATE students SET age = 21 WHERE name = 'Alice';\n\n-- DELETE\nDELETE FROM students WHERE age < 18;\n\n-- SELECT (Read)\nSELECT * FROM students;",
    },
    {
        "topic": "sql subquery",
        "questions": [
            "What is a subquery in SQL?",
            "SQL subquery example",
            "How to use subquery in WHERE clause?",
            "Correlated subquery in SQL",
            "Subquery vs JOIN in SQL",
        ],
        "answer": "-- Find students who scored above average\nSELECT name, score\nFROM students\nWHERE score > (SELECT AVG(score) FROM students);\n\n-- Subquery in FROM\nSELECT dept, avg_sal\nFROM (SELECT department AS dept, AVG(salary) AS avg_sal FROM employees GROUP BY department) AS dept_avg\nWHERE avg_sal > 50000;",
    },
    # ── React ────────────────────────────────────────────────────────────────
    {
        "topic": "react useState",
        "questions": [
            "Explain React useState",
            "How to use useState hook in React?",
            "React state management with useState",
            "useState example in React functional component",
            "How to update state in React?",
        ],
        "answer": "import { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n\n  return (\n    <div>\n      <p>Count: {count}</p>\n      <button onClick={() => setCount(count + 1)}>Increment</button>\n      <button onClick={() => setCount(count - 1)}>Decrement</button>\n    </div>\n  );\n}\nexport default Counter;",
    },
    {
        "topic": "react useEffect",
        "questions": [
            "What is useEffect in React?",
            "React useEffect example",
            "How to fetch data with useEffect?",
            "useEffect with cleanup in React",
            "useEffect dependency array explained",
        ],
        "answer": "import { useState, useEffect } from 'react';\n\nfunction DataFetcher() {\n  const [data, setData] = useState(null);\n\n  useEffect(() => {\n    fetch('https://jsonplaceholder.typicode.com/posts/1')\n      .then(res => res.json())\n      .then(json => setData(json));\n\n    return () => { /* cleanup */ };\n  }, []);  // runs once on mount\n\n  return <div>{data ? data.title : 'Loading...'}</div>;\n}\nexport default DataFetcher;",
    },
    {
        "topic": "react props",
        "questions": [
            "What are props in React?",
            "How to pass props in React?",
            "React props example",
            "Difference between props and state in React",
            "How to pass function as prop in React?",
        ],
        "answer": "function Greeting({ name, age }) {\n  return <p>Hello {name}, you are {age} years old.</p>;\n}\n\nfunction App() {\n  return <Greeting name='Alice' age={20} />;\n}\nexport default App;",
    },
    {
        "topic": "react forms",
        "questions": [
            "How to handle forms in React?",
            "React controlled input example",
            "Form submit in React",
            "How to get input value in React?",
            "React form validation example",
        ],
        "answer": "import { useState } from 'react';\n\nfunction LoginForm() {\n  const [email, setEmail] = useState('');\n  const [pass, setPass] = useState('');\n\n  const handleSubmit = (e) => {\n    e.preventDefault();\n    console.log(email, pass);\n  };\n\n  return (\n    <form onSubmit={handleSubmit}>\n      <input value={email} onChange={e => setEmail(e.target.value)} placeholder='Email' />\n      <input type='password' value={pass} onChange={e => setPass(e.target.value)} placeholder='Password' />\n      <button type='submit'>Login</button>\n    </form>\n  );\n}\nexport default LoginForm;",
    },
    {
        "topic": "react list rendering",
        "questions": [
            "How to render a list in React?",
            "React map example",
            "Render array of objects in React",
            "What is key prop in React list?",
            "React list with delete button",
        ],
        "answer": "function ItemList({ items }) {\n  return (\n    <ul>\n      {items.map((item) => (\n        <li key={item.id}>{item.name}</li>\n      ))}\n    </ul>\n  );\n}\n\nfunction App() {\n  const items = [{id:1, name:'Apple'}, {id:2, name:'Banana'}];\n  return <ItemList items={items} />;\n}\nexport default App;",
    },
    # ── Interview ────────────────────────────────────────────────────────────
    {
        "topic": "interview OOP",
        "questions": [
            "What are the 4 pillars of OOP?",
            "Explain encapsulation with example",
            "What is abstraction in programming?",
            "Difference between abstraction and encapsulation",
            "OOP concepts interview questions",
        ],
        "answer": "The 4 pillars of OOP are:\n1. Encapsulation - bundling data and methods, hiding internal state\n2. Inheritance - child class inherits from parent class\n3. Polymorphism - same method behaves differently based on object\n4. Abstraction - hiding implementation details, showing only interface\n\nExample: A Car class encapsulates engine details. You call car.start() without knowing the internals.",
    },
    {
        "topic": "interview data structures",
        "questions": [
            "Difference between stack and queue",
            "What is a linked list?",
            "When to use array vs linked list?",
            "What is a binary tree?",
            "Explain Big O notation",
        ],
        "answer": "Stack: LIFO (Last In First Out) - e.g. undo operations\nQueue: FIFO (First In First Out) - e.g. print queue\n\nLinked List: nodes connected by pointers, O(1) insert, O(n) search\nArray: contiguous memory, O(1) access by index, O(n) insert\n\nBig O: describes algorithm efficiency\n  O(1) - constant, O(n) - linear, O(n^2) - quadratic, O(log n) - logarithmic",
    },
    {
        "topic": "interview python specific",
        "questions": [
            "Difference between list and tuple in Python interview",
            "What is GIL in Python?",
            "Explain Python memory management",
            "What is duck typing in Python?",
            "Mutable vs immutable in Python",
        ],
        "answer": "List vs Tuple:\n- List is mutable (can change), Tuple is immutable\n- List: [1,2,3], Tuple: (1,2,3)\n\nGIL (Global Interpreter Lock):\n- Prevents multiple threads from executing Python bytecode simultaneously\n- Affects CPU-bound multithreading\n\nMutable: list, dict, set (can be changed)\nImmutable: int, float, str, tuple (cannot be changed after creation)\n\nDuck Typing: if it walks like a duck and quacks like a duck, it is a duck - Python checks behavior not type",
    },
    {
        "topic": "interview web concepts",
        "questions": [
            "Difference between GET and POST request",
            "What is REST API?",
            "Explain HTTP status codes",
            "What is JSON?",
            "Difference between frontend and backend",
        ],
        "answer": "GET: retrieves data, params in URL, cacheable\nPOST: sends data in body, not cached, used for forms/login\n\nREST API: architectural style using HTTP methods (GET, POST, PUT, DELETE) for CRUD operations\n\nHTTP Status Codes:\n200 - OK, 201 - Created, 400 - Bad Request, 401 - Unauthorized, 404 - Not Found, 500 - Server Error\n\nJSON: JavaScript Object Notation - lightweight data format\n{\"name\": \"Alice\", \"age\": 20}\n\nFrontend: what user sees (HTML/CSS/React)\nBackend: server logic (Python/Java/Node.js)",
    },
    {
        "topic": "debugging tips",
        "questions": [
            "How to debug Python code?",
            "Python debugging techniques",
            "How to use print for debugging in Python?",
            "Common Python bugs and fixes",
            "How to fix IndentationError in Python?",
        ],
        "answer": "# 1. Print debugging\nx = 10\nprint(f'DEBUG: x = {x}')\n\n# 2. Use pdb\nimport pdb\npdb.set_trace()  # breakpoint\n\n# 3. Common fixes:\n# IndentationError: ensure consistent spaces (4 spaces recommended)\n# NameError: check variable is defined before use\n# TypeError: check variable types before operations\n\n# 4. Use try/except to catch and print errors\ntry:\n    risky_code()\nexcept Exception as e:\n    print(f'Error: {e}')",
    },
    # ── More Python (advanced/intermediate) ─────────────────────────────────
    {
        "topic": "python multiprocessing",
        "questions": [
            "What is multiprocessing in Python?",
            "Difference between threading and multiprocessing in Python",
            "Python multiprocessing example",
            "How to run parallel tasks in Python?",
            "Python Pool.map example",
        ],
        "answer": "from multiprocessing import Pool\n\ndef square(n):\n    return n * n\n\nif __name__ == '__main__':\n    with Pool(4) as p:\n        results = p.map(square, [1, 2, 3, 4, 5])\n    print(results)  # [1, 4, 9, 16, 25]",
    },
    {
        "topic": "python regex",
        "questions": [
            "How to use regex in Python?",
            "Python re module example",
            "Find pattern in string using Python",
            "Python regex match vs search",
            "Extract emails from text using Python regex",
        ],
        "answer": "import re\n\ntext = 'Contact us at support@example.com or info@site.org'\n\n# Find all emails\nemails = re.findall(r'[\\w.]+@[\\w.]+', text)\nprint(emails)  # ['support@example.com', 'info@site.org']\n\n# match vs search\nprint(re.match(r'Contact', text))   # matches at start\nprint(re.search(r'support', text))  # searches anywhere",
    },
    {
        "topic": "python json",
        "questions": [
            "How to read JSON in Python?",
            "Python json.loads and json.dumps example",
            "Parse JSON file in Python",
            "Convert Python dict to JSON",
            "Write JSON to file in Python",
        ],
        "answer": "import json\n\n# Dict to JSON string\ndata = {'name': 'Alice', 'age': 20}\njson_str = json.dumps(data, indent=2)\nprint(json_str)\n\n# JSON string to dict\nparsed = json.loads(json_str)\nprint(parsed['name'])\n\n# Write to file\nwith open('data.json', 'w') as f:\n    json.dump(data, f, indent=2)\n\n# Read from file\nwith open('data.json') as f:\n    loaded = json.load(f)\nprint(loaded)",
    },
    {
        "topic": "python virtual environment",
        "questions": [
            "What is virtual environment in Python?",
            "How to create virtual environment in Python?",
            "Why use venv in Python?",
            "Activate virtual environment Windows",
            "How to install packages in venv?",
        ],
        "answer": "# Create venv\npython -m venv venv\n\n# Activate (Windows)\nvenv\\Scripts\\activate\n\n# Activate (Mac/Linux)\nsource venv/bin/activate\n\n# Install package\npip install requests\n\n# Save dependencies\npip freeze > requirements.txt\n\n# Install from requirements\npip install -r requirements.txt\n\n# Deactivate\ndeactivate",
    },
]

output_file = "expanded_dataset.jsonl"
count = 0

with open(output_file, "w", encoding="utf-8") as f:
    for item in samples:
        for q in item["questions"]:
            row = {"instruction": q, "input": "", "output": item["answer"]}
            f.write(json.dumps(row) + "\n")
            count += 1

print(f"Dataset Generated Successfully — {count} records written to {output_file}")
