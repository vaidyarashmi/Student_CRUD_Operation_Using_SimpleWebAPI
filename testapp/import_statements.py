# for views, mixins
import django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from testapp.models import Student
from django.core.serializers import serialize
import json
from testapp.mixins import HttpMixins,JSONDataMixins,IDMixins
from testapp.forms import StudentForm

