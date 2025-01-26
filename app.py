{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, render_template, request\
import sqlite3\
import os\
\
app = Flask(__name__)\
UPLOAD_FOLDER = './uploads'\
os.makedirs(UPLOAD_FOLDER, exist_ok=True)\
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER\
\
\
def get_tables(db_path):\
    """Retrieve the list of tables from a database."""\
    conn = sqlite3.connect(db_path)\
    cursor = conn.cursor()\
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")\
    tables = [table[0] for table in cursor.fetchall()]\
    conn.close()\
    return tables\
\
\
def compare_tables(db1_path, db2_path):\
    """Compare the tables of two databases."""\
    conn1 = sqlite3.connect(db1_path)\
    conn2 = sqlite3.connect(db2_path)\
    cursor1 = conn1.cursor()\
    cursor2 = conn2.cursor()\
\
    tables1 = get_tables(db1_path)\
    tables2 = get_tables(db2_path)\
\
    results = []\
\
    for table in set(tables1) | set(tables2):\
        if table in tables1 and table in tables2:\
            cursor1.execute(f"SELECT * FROM \{table\}")\
            data1 = cursor1.fetchall()\
\
            cursor2.execute(f"SELECT * FROM \{table\}")\
            data2 = cursor2.fetchall()\
\
            differences = \{'table': table, 'only_in_db1': [], 'only_in_db2': []\}\
\
            # Find rows in db1 not in db2\
            for row in data1:\
                if row not in data2:\
                    differences['only_in_db1'].append(row)\
\
            # Find rows in db2 not in db1\
            for row in data2:\
                if row not in data1:\
                    differences['only_in_db2'].append(row)\
\
            results.append(differences)\
        else:\
            results.append(\{'table': table, 'only_in_db1': 'Table Missing', 'only_in_db2': 'Table Missing'\})\
\
    conn1.close()\
    conn2.close()\
    return results\
\
\
@app.route('/', methods=['GET', 'POST'])\
def upload_files():\
    if request.method == 'POST':\
        db1 = request.files['db1']\
        db2 = request.files['db2']\
\
        db1_path = os.path.join(app.config['UPLOAD_FOLDER'], db1.filename)\
        db2_path = os.path.join(app.config['UPLOAD_FOLDER'], db2.filename)\
\
        db1.save(db1_path)\
        db2.save(db2_path)\
\
        results = compare_tables(db1_path, db2_path)\
\
        return render_template('results.html', results=results)\
\
    return render_template('upload.html')\
\
\
if __name__ == '__main__':\
    app.run(debug=True)\
\
# upload.html\
UPLOAD_HTML = """\
<!DOCTYPE html>\
<html>\
<head>\
    <title>Upload Databases</title>\
</head>\
<body>\
    <h1>Upload SQLite Databases</h1>\
    <form action="/" method="post" enctype="multipart/form-data">\
        <label for="db1">Database 1:</label>\
        <input type="file" id="db1" name="db1" required><br><br>\
        <label for="db2">Database 2:</label>\
        <input type="file" id="db2" name="db2" required><br><br>\
        <button type="submit">Compare</button>\
    </form>\
</body>\
</html>\
"""\
\
# results.html\
RESULTS_HTML = """\
<!DOCTYPE html>\
<html>\
<head>\
    <title>Comparison Results</title>\
</head>\
<body>\
    <h1>Database Comparison Results</h1>\
    <table border="1">\
        <tr>\
            <th>Table Name</th>\
            <th>Only in Database 1</th>\
            <th>Only in Database 2</th>\
        </tr>\
        \{% for result in results %\}\
        <tr>\
            <td>\{\{ result.table \}\}</td>\
            <td>\
                \{% if result.only_in_db1 == 'Table Missing' %\}\
                    \{\{ result.only_in_db1 \}\}\
                \{% else %\}\
                    <ul>\
                    \{% for row in result.only_in_db1 %\}\
                        <li>\{\{ row \}\}</li>\
                    \{% endfor %\}\
                    </ul>\
                \{% endif %\}\
            </td>\
            <td>\
                \{% if result.only_in_db2 == 'Table Missing' %\}\
                    \{\{ result.only_in_db2 \}\}\
                \{% else %\}\
                    <ul>\
                    \{% for row in result.only_in_db2 %\}\
                        <li>\{\{ row \}\}</li>\
                    \{% endfor %\}\
                    </ul>\
                \{% endif %\}\
            </td>\
        </tr>\
        \{% endfor %\}\
    </table>\
</body>\
</html>\
"""\
\
# Save templates to files\
with open('templates/upload.html', 'w') as f:\
    f.write(UPLOAD_HTML)\
\
with open('templates/results.html', 'w') as f:\
    f.write(RESULTS_HTML)\
}