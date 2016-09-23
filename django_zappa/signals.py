# coding=utf-8
from django.dispatch.dispatcher import Signal


AWSEvent = Signal(['name', 'source', 'message'])
