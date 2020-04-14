from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

astronauts = {}
last_name = None


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def prof(prof):
    title = 'http://127.0.0.1:8089//training/' + prof
    prof = prof.lower()
    return render_template('prof.html', title=title, prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    title = 'http://127.0.0.1:8089//list_prof/' + list
    prof_list = ['инженер-исследователь', 'врач', 'пилот', 'строитель', 'экзобиолог', 'климатолог',
                 'штурман', 'пилот дронов', 'астрогеолог', 'инженер жизнеобеспечения', 'киберинженер',
                 'оператор марсохода']
    return render_template('list_prof.html', title=title, list=list, prof_list=prof_list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    if last_name is not None:
        surname = astronauts[last_name]["surname"]
        name = astronauts[last_name]['name']
        education = astronauts[last_name]['education']
        proff = astronauts[last_name]['prof']
        sex = astronauts[last_name]['sex']
        reason = astronauts[last_name]['reason']
        accept = astronauts[last_name]['accept']
    else:
        surname = ''
        name = ''
        education = ''
        proff = ''
        sex = ''
        reason = ''
        accept = ''
    return render_template('answer.html', surname=surname, name=name, education=education,
                           proff=proff, sex=sex, rea=reason, accept=accept)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" 
                        href="{url_for('static', filename='css/astronaut_selection.css')}" />
                        <title>Отбор астронавтов</title>
                      </head>
                      <body>
                        <h1>Анкета претендента</h1>
                        <h2>на участие в миссии</h2>
                        <div>
                            <form class="login_form" method="post">
                                <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                <input type="text" class="form-control" id="surname" placeholder="Введите имя" name="name">
                                <label></label>
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">

                                <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                          <option>Высшее профессиональное</option>
                                        </select>
                                </div>

                                <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <label for="form-check">Какие у Вас есть профессии?</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="prof" id="doctor" value="doctor">
                                      <label class="form-check-label" for="doctor">
                                        Врач
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="prof" id="ingener" value="ingener">
                                      <label class="form-check-label" for="ingener">
                                        Инженер
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="prof" id="pilot" value="pilot">
                                      <label class="form-check-label" for="pilot">
                                        Пилот
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="prof" id="biolog" value="biolog">
                                      <label class="form-check-label" for="biolog">
                                        Биолог
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="prof" id="dron" value="dron">
                                      <label class="form-check-label" for="dron">
                                        Пилот дронов
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="prof" id="radiacia" value="radiacia">
                                      <label class="form-check-label" for="radiacia">
                                        Специалист по радиационной защите
                                      </label>
                                    </div>

                                </div>

                                <div class="form-group">
                                    <label for="reason">Почему Вы хотите принять участие в миссии?</label>
                                    <textarea class="form-control" id="reason" rows="3" name="reason"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>

                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                </div>
                                <button type="submit" class="btn btn-primary">Записаться</button>
                            </form>
                        </div>
                      </body>
                    </html>'''

    elif request.method == 'POST':
        global astronauts, last_name
        surname = request.form['surname']
        name = request.form['name']
        email = request.form['email']
        education = request.form['education']
        proff = request.form['prof']
        sex = request.form['sex']
        reason = request.form['reason']
        file = request.form['file']
        try:
            accept = request.form['accept']
        except Exception:
            accept = 'off'
        last_name = surname + ' ' + name

        astronauts[last_name] = {'surname': surname, 'name': name, 'email': email, 'education': education,
                                 'prof': proff, 'sex': sex, 'reason': reason,
                                 'file': file, 'accept': accept}
        return redirect('/answer')


@app.route('/distribution')
def distribution():
    title = 'Каюты'
    user_list = list(astronauts.keys())
    print(user_list)
    return render_template('distribution.html', title=title, user_list=user_list)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    print(sex, age)
    return render_template('table.html', title='Ваша каюта', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8088, host='127.0.0.1')
