import json
import time

from flask import Flask, render_template, abort, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/elements/')
def elements():
    return render_template('elements.html')


@app.route('/disabled-elements/')
def disabled_elements():
    return render_template('disabled_elements.html')


@app.route('/dynamic-elements/')
def dynamic_elements():
    delay = request.args.get('delay', 0)
    delay = int(delay) if delay.isdigit() else 0
    return render_template('dynamic_elements.html', delay=delay)


@app.route('/special-elements/')
def special_elements():
    return render_template('special_elements.html')


@app.route('/drag-and-drop/')
def drag_and_drop():
    return render_template('drag_and_drop.html')


@app.route('/form-basic/')
def form_basic():
    return render_template('form_basic.html')


@app.route('/form-basic-result/', methods=['POST'])
def form_basic_result():
    print(request.form.getlist('lightsaber'))
    data = {
        'name': request.form['name'],
        'planet': request.form['planet'],
        'lightsaber': 'lightsaber' in request.form,
        'alignment': request.form['alignment']
    }
    return render_template('form_basic_result.html', data=data)


@app.route('/ajax-request/')
def ajax_request():
    return render_template('ajax_request.html')


@app.route('/ajax-request-process/', methods=['POST'])
def ajax_request_process():
    result = None
    number_one = request.form['numberOne'].strip()
    number_two = request.form['numberTwo'].strip()
    delay = request.form.get('delay', 0).strip()
    if delay.isdigit():
        time.sleep(int(delay))
    if number_one.isdigit() and number_two.isdigit():
        result = int(number_one) + int(number_two)
    return json.dumps(result)


@app.route('/tabs/')
def tabs():
    return render_template('tabs.html')


@app.route('/tab/')
def tab():
    delay = request.args.get('delay', 0)
    title = request.args.get('title', 'Tab')
    time.sleep(int(delay))
    return render_template('tab.html', title=title)


# Frames

@app.route('/frames/')
def frames():
    return render_template('frames/frames.html')


@app.route('/frame-top/')
def frame_top():
    return render_template('frames/frame_top.html')


@app.route('/frame-bottom/')
def frame_bottom():
    return render_template('frames/frame_bottom.html')


@app.route('/frame-bottom-left/')
def frame_bottom_left():
    return render_template('frames/frame_bottom_left.html')


@app.route('/frame-bottom-right/')
def frame_bottom_right():
    return render_template('frames/frame_bottom_right.html')


# IFrames

@app.route('/iframes/')
def iframes():
    return render_template('frames/iframes.html')


@app.route('/iframe-top/')
def iframe_top():
    return render_template('frames/iframe_top.html')


@app.route('/iframe-bottom/')
def iframe_bottom():
    return render_template('frames/iframe_bottom.html')


@app.route('/iframe-bottom-left/')
def iframe_bottom_left():
    return render_template('frames/iframe_bottom_left.html')


@app.route('/iframe-bottom-right/')
def iframe_bottom_right():
    return render_template('frames/iframe_bottom_right.html')


@app.route('/alert/')
def alert():
    return render_template('alerts/alert.html')


@app.route('/prompt/')
def prompt():
    return render_template('alerts/prompt.html')


@app.route('/confirm/')
def confirm():
    return render_template('alerts/confirm.html')


@app.route('/confirm-exit/')
def confirm_exit():
    return render_template('alerts/confirm_exit.html')


@app.route('/http-error/<int:error_code>/')
def http_error(error_code):
    try:
        return abort(error_code)
    except LookupError:
        msg = ('<h1>status code {} not found</h1>\n'
               '<a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes">'
               'List of HTTP status codes</a>'
               .format(error_code))
        return msg
