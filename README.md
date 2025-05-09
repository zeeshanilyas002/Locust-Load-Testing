# Locust Load Testing Setup

## Description

Locust is a modern, open-source load testing framework that allows you to define user behavior in Python code. It can simulate millions of concurrent users interacting with your system, making it an excellent choice for performance testing of web applications, APIs, or any system under load.

### When to Use Locust

Locust is ideal for:

* **Stress Testing:** To see how your system behaves under heavy load.
* **Performance Testing:** To identify bottlenecks and optimize your system.
* **API Load Testing:** For simulating a large number of API requests to evaluate performance.
* **Continuous Integration:** Automating load tests as part of your CI/CD pipeline.

Locust allows you to write test scenarios in Python, which gives you full control over the behavior of your virtual users.

---

## Steps to Configure Locust in Visual Studio Code

### 1. Install Python

First, ensure that you have **Python** installed. You can download the latest version of Python from the [official Python website](https://www.python.org/downloads/).

To verify the installation, run the following command in your terminal:

```bash
python --version
```

### 2. Install Locust

Once Python is installed, open a terminal in **Visual Studio Code** and install Locust using **pip**:

```bash
pip install locust
```

This command will install Locust and all the required dependencies.

To confirm Locust was installed correctly, run:

```bash
pip show locust
```

### 3. Create Your Locust Test Script

In your project directory, create a new Python file (e.g., `locustfile.py`). This file will contain your test scenarios.

Here’s a simple example to simulate users hitting an API endpoint:

```python
from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 5)  # Simulate a wait time of 1 to 5 seconds between tasks

    @task
    def get_homepage(self):
        self.client.get("/")  # Replace with your API's endpoint
```

### 4. Run Locust in Visual Studio Code

![image](https://github.com/user-attachments/assets/761ccebb-aa23-4dd1-8c3e-f8331d3230c1)

To run Locust, open the terminal in Visual Studio Code and execute the following command:

```bash
python -m locust -f locustfile.py --host https://your-api.com --web-port 8082
```

Make sure to replace `https://your-api.com` with the URL of the API you want to test.

### 5. Access the Web Interface

After running the above command, Locust will start a web interface at [http://localhost:8082](http://localhost:8082). You can open this URL in your browser to start the test and configure the number of users and spawn rate.

### 6. Start Load Testing

In the Locust web interface, you'll see options to set the number of **total users** and **spawn rate** (how fast users will be spawned). Once you set the values, click **Start Swarming** to begin the load test.
![RunningLoadTest](https://github.com/user-attachments/assets/10af3c20-3e30-48d7-9ef0-fdc7eaa70b14)

---

## Additional Configuration (Optional)

### Running Locust on a Different Port

If port `8082` is occupied or if you want to use a different port for the web interface, you can specify the port with the `--web-port` flag:

```bash
python -m locust -f locustfile.py --host https://your-api.com --web-port 8085
```

### Running Locust with Multiple User Types

You can create multiple user types (i.e., `HttpUser` classes) with different behavior patterns. Here’s how you can extend the previous example with a different user type:

```python
class AdminUser(HttpUser):
    @task
    def access_admin(self):
        self.client.get("/admin")

class RegularUser(HttpUser):
    @task
    def access_home(self):
        self.client.get("/")
```

---

## Troubleshooting

### Common Errors

1. **Port Conflict (Error 10013)**:
   If you encounter `PermissionError: [WinError 10013]`, it means port `8089` is blocked or already in use. You can change the port by specifying a different one with the `--web-port` flag (as shown above).

2. **Locust Command Not Found**:
   If you get a `command not found` error for Locust, ensure that your environment's `Scripts` directory (for Python) is added to the system’s PATH.

### Locust Documentation

For more advanced configurations, you can refer to the [Locust Documentation](https://docs.locust.io/en/stable/).

---

Feel free to modify the repository with more custom configurations or complex scenarios as needed for your testing.

