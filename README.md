{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # SQLite Database Comparison Tool\
\
This application allows you to upload two SQLite database files, compare their tables, and view the differences in a web interface. The results will display tables and their rows that are present in one database but not the other.\
\
## Features\
\
- Upload two SQLite database files via a web interface.\
- Compare the tables between the two databases.\
- Identify rows unique to each database for tables that exist in both.\
- User-friendly web interface for file upload and result display.\
\
## Prerequisites\
\
Before running the application, ensure you have the following installed:\
\
1. **Python 3.7 or later**\
2. **pip** (Python package manager)\
\
Install the required dependencies by running:\
\
```bash\
pip install flask\
```\
\
## How to Use\
\
1. **Clone or Download the Project** Download the source code files and ensure all files are in the same directory.\
\
2. **Prepare the Environment** Make sure Python is installed and set up on your system. Install Flask if not already installed:\
\
   ```bash\
   pip install flask\
   ```\
\
3. **Run the Application** Execute the `app.py` script:\
\
   ```bash\
   python app.py\
   ```\
\
   The application will start a web server and will display the URL to access it (e.g., `http://127.0.0.1:5000/`).\
\
4. **Upload Databases**\
\
   - Open the application in your web browser using the provided URL.\
   - Use the file upload form to select and upload two SQLite database files.\
   - Click "Compare" to perform the comparison.\
\
5. **View Results**\
\
   - The results page will display:\
     - Tables unique to each database.\
     - Rows present in one database but missing in the other for common tables.\
\
## File Structure\
\
```\
project/\
\uc0\u9500 \u9472 \u9472  app.py               # Main application script\
\uc0\u9500 \u9472 \u9472  templates/\
\uc0\u9474    \u9500 \u9472 \u9472  upload.html      # File upload form template\
\uc0\u9474    \u9492 \u9472 \u9472  results.html     # Comparison results display template\
\uc0\u9492 \u9472 \u9472  uploads/             # Directory to store uploaded database files\
```\
\
## Templates\
\
1. \\`\\`\
\
   - Displays the upload form for two database files.\
\
2. \\`\\`\
\
   - Displays the comparison results in a tabular format.\
\
## Example Usage\
\
1. Launch the application:\
   ```bash\
   python app.py\
   ```\
2. Navigate to `http://127.0.0.1:5000/` in your browser.\
3. Upload two SQLite databases.\
4. View the results with table and row-level differences.\
\
## Notes\
\
- Ensure the uploaded files are valid SQLite databases.\
- The uploaded files are temporarily stored in the `uploads/` directory for processing.\
- This tool is for local use; do not deploy it to production without proper security measures.\
\
## Troubleshooting\
\
- **Issue:** Flask is not installed.\
\
  - **Solution:** Install Flask using `pip install flask`.\
\
- **Issue:** The server does not start or shows an error.\
\
  - **Solution:** Check if Python and pip are correctly installed. Ensure all dependencies are installed.\
\
## License\
\
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the license terms.\
\
}