import sys

sys.path.insert(0, 'static/xml_files')

from flask import Flask, render_template, redirect, request, send_file, url_for
from flask_uploads import UploadSet, configure_uploads
from main import HANCOC

app = Flask(__name__)

app.config['UPLOADED_XMLS_DEST'] = 'static/xml_files'
xmls = UploadSet('xmls', 'xml')

configure_uploads(app, (xmls))


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and 'xml' in request.files:
        filename = xmls.save(request.files['xml'])
        xml_string = open(('static/xml_files/' + filename)).read()
        xml_name = filename.rsplit('.', 1)[0]
        HANCOC(xml_string, xml_name + '_HANCOC')
        return return_file(xml_name)
    return render_template('home.html')


@app.route("/return-file")
def return_file(xml_name):
    return send_file(xml_name + '_HANCOC.xml')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
