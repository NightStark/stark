from flask import render_template, g, flash, session, redirect, url_for, request
from app import app, lm
from .forms import LoginForm, SignUpForm
from flask.ext.login import LoginManager, login_manager, login_user, current_user, logout_user
from .models import User
from .user_op import UserOp
import traceback


@lm.user_loader
def load_user(user_id):
    print("user_id:" + user_id.__str__())
    #traceback.print_stack()
    #return User.get(user_id)
    user = User()

    return user



@app.before_request
def before_request():
    print("before_request")
    g.user = current_user
    print(current_user)
    # traceback.print_stack()


@app.route('/')
@app.route('/index')
def index():
    print("index current_user")
    print(current_user)
    print("index g.user")
    print(g.user.is_authenticated)
    #if g.user.is_authenticated():
    #    print("is_authenticated")
    return render_template("index.html", title="Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("current_user")
    print(current_user)
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    user = User()
    form = LoginForm()
    flash(form.validate_on_submit())
    if form.validate_on_submit():
        flash('Login requested for username="' +
              form.username.data + '" remember_me=' +
              form.remember_me.data.__str__())
        session['remember_me'] = form.remember_me.data
        # return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
        form.login_check()
        flash("form.username_is_invalid:" + form.username_is_invalid().__str__())
        flash("form.password_is_invalid:" + form.password_is_invalid().__str__())
        if not form.username_is_invalid() or not form.password_is_invalid():
            return render_template('login.html',
                                   title="Sign In",
                                   form=form)

        login_user(user)
        flash('Logged in successfully.')
        # user_op = UserOp()

        next = request.args.get('next')
        # print(next)

        return redirect(next or url_for('index'))

        # return redirect(url_for('index'))
    else:
        flash("some thing is error.")

    return render_template('login.html',
                           title="Sign In",
                           form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    flash("sign up")
    sign_up_form = SignUpForm()
    flash(sign_up_form.validate_on_submit())
    if sign_up_form.validate_on_submit():
        flash('Login requested for username="' +
              sign_up_form.username.data + '" email=' +
              sign_up_form.email.data)
        flash("sign_up_form user_op_check")
        sign_up_form.user_op_check()
        if sign_up_form.user_op_get_error():
            flash("checker.get_error: username: "+sign_up_form.checker.username_is_exit.__str__()+
                  "   nickname:"+sign_up_form.checker.nickname_is_exit.__str__() +
            "  email: " + sign_up_form.checker.email_is_exit.__str__() +
            "  get_error: " + sign_up_form.checker.get_error.__str__())
            return render_template('sign_up.html',
                                   title="Sign Up",
                                   sign_up_form=sign_up_form)
        else:
            flash(" not checker.get_error, checker.user_op_create")
            sign_up_form.checker.user_op_create(sign_up_form)
            return render_template('sign_up_success.html',
                                   title="Sign Up",
                                   sign_up_form=sign_up_form)

        return render_template('sign_up.html',
                               title="Sign Up",
                               sign_up_form=sign_up_form)

    else:
        flash("some thing is error.")

    return render_template('sign_up.html',
                           title="Sign Up",
                           sign_up_form=sign_up_form)





