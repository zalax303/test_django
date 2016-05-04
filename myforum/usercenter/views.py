#coding:utf-8
import datetime
import uuid

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from models import ActivateCode

