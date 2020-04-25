from functools import wraps
from flask import session, render_template, url_for, redirect

def roles_admin():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'role' in session.keys():
                if 'admin' in session["role"]:
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for('loginModule.error'))
            else:
                return redirect(url_for('loginModule.error'))
        return wrapped
    return wrapper

def roles_user():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'role' in session.keys():
                if session["role"] == 'user':
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for('loginModule.error'))
            else:
                return redirect(url_for('loginModule.error'))
        return wrapped
    return wrapper


def roles_admin_user():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'role' in session.keys():
                if session["role"] == 'user' or session["role"] == 'admin':
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for('loginModule.error'))
            else:
                return redirect(url_for('loginModule.error'))
        return wrapped
    return wrapper
