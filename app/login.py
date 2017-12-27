# -*- coding: utf8 -*-
from flask import Flask,session, redirect
from flask import Blueprint, render_template, abort, request, redirect
from flask import request, Response, session
from functools import wraps
# from app.login import requires_auth

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'id' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated
