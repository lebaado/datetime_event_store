<h1>📦 Datetime Event Store API</h1>
A simple Python package and REST API that allows you to store and retrieve events based on datetime ranges.

<h2>🚀 Features</h2>

Store events tied to a specific datetime

Retrieve events between two datetime values

Lightweight REST API built with Flask

Some test Files added for the api file (storageFlask.py) as well as the one that doesn't use api (storage.py)

<h2>🖼️ Preview</h2>

This happenss when we launch storageFlask.py


![image](https://github.com/user-attachments/assets/8e8f232b-98df-4c38-aa36-79a51a8d7fbb)


Now, we can add entries with python requests 


![image](https://github.com/user-attachments/assets/22e4ae27-0496-42a6-9777-2b9bf89927b2)

![image](https://github.com/user-attachments/assets/da65ca82-5c02-4bb8-aad2-73518e49f1c9)


And to access them, we can write in the url, the range of the research in the URL like this : http://127.0.0.1:5000/events?start=2025-07-05T00:00:00&end=2025-07-05T23:59:59


![image](https://github.com/user-attachments/assets/c05f899c-e71a-4a2f-a9f1-a838d435f8ee)


<h2>📦 Installation</h2>

To install it, you will first need requests and flask packages with this

<code>pip install flask
  pip install requests
</code>

<h2>📁 Project Structure</h2>


![image](https://github.com/user-attachments/assets/b990299c-29d6-4e9a-b291-d1ae23760235)


<h2>🧠 Notes</h2>

<ul>
  <li>
    The data is not persisted between runs (in-memory only).
  </li>
  <li>
    Designed only for demonstration.
  </li>
</ul>
