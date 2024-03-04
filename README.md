Welcome to our repository! In this guide, we'll walk you through setting up a virtual environment and installing the necessary requirements for our project.

## Setting Up Your Virtual Environment

A virtual environment is a great way to isolate project dependencies and ensure that the correct versions of packages are installed without affecting your system's global configuration. Follow these steps to create and activate a virtual environment:

1. **Install `virtualenv` (if you don't have it already):**

   ```bash
   pip install virtualenv
   ```

2. **Create a new virtual environment:**

   ```bash
   virtualenv venv
   ```

   Replace `venv` with your desired virtual environment name.

      or **Use Python3:**

   ```bash
   python3 -m venv .venv
   ```

4. **Activate the virtual environment:**

   - On Windows, run:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux, run:
     ```bash
     source venv/bin/activate
     ```

   Once activated, your terminal prompt will change, indicating that you're now working within the virtual environment.

5. **Install Project Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the required packages specified in `requirements.txt` into your virtual environment.

6. **When Finished, Deactivate the Virtual Environment:**

   To exit the virtual environment, simply run:
   ```bash
   deactivate
   ```

## Running the Project

After setting up your virtual environment and installing the requirements, you can run the project using the following command after going into the folder:

```bash
scrapy crawl your_spider
```

Replace `your_spider` with the name of the spider you want to run.

## Updating Requirements

If you need to update the project's dependencies, you can do so by modifying `requirements.txt`. After making changes, run the following command to update the virtual environment:

```bash
pip install -r requirements.txt
```

That's it! You should now have a virtual environment set up for our project, with all the necessary requirements installed. If you encounter any issues, feel free to reach out to us. Happy coding!
