from bottle import run, route, request, template, static_file, get, post
import os
import create_acapella as ac
import subprocess

@get('/')
def upload():
    return template('upload', msg='', col='red')

@post('/')
def do_upload():
    original = request.files.get('original')
    instrumental = request.files.get('instrumental')
    fn = request.forms.get('fn')
    orig_name, orig_ext = os.path.splitext(original.filename)
    instr_name, instr_ext = os.path.splitext(instrumental.filename)
    if orig_ext != '.mp3' or instr_ext != '.mp3':
        return(template('error', text='You can only extract acapellas from .mp3-files.'))

    save_path = '../temp/'
    original.save(save_path)
    instrumental.save(save_path)

    o_wav = save_path + orig_name + ".wav"
    i_wav = save_path + instr_name + ".wav"
    process1 = subprocess.Popen("mpg123 -w " + o_wav + " " + save_path + original.filename, shell=True, stdout=subprocess.PIPE)
    process2 = subprocess.Popen("mpg123 -w " + i_wav + " " + save_path + instrumental.filename, shell=True, stdout=subprocess.PIPE)
    process1.wait()
    process2.wait()
    print (process1.returncode)
    print (process2.returncode)
    os.remove(save_path + original.filename)
    os.remove(save_path + instrumental.filename)

    ac.create_acapella(o_wav, i_wav, save_path + fn)
    os.remove(o_wav)
    os.remove(i_wav)
    process = subprocess.Popen("lame -b 192 " + save_path + fn + ".wav " + save_path + fn + ".mp3", shell=True, stdout=subprocess.PIPE)
    process.wait()
    os.remove(save_path + fn + ".wav")
    return static_file(fn + ".mp3", root=save_path, mimetype='audio/mpeg')
    #return (template('upload', msg='Successfully extracted Acapella. Download...'))

if __name__ == "__main__":
    run(debug=True, reloader=True)
