from bottle import run, route, request, template, static_file, get, post
import os

@get('/')
def upload():
    return template('upload')

@post('/')
def do_upload():
    original = request.files.get('original')
    instrumental = request.files.get('instrumental')
    orig_name, orig_ext = os.path.splitext(original.filename)
    instr_name, instr_ext = os.path.splitext(instrumental.filename)
    save_path = '/home/marlon/code/'
    original.save(save_path)
    instrumental.save(save_path)
    return (template('print', text='OK'))

if __name__ == "__main__":
    run(debug=True, reloader=True)
