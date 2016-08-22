from django.core import serializers
from django.contrib.auth.models import *
from django.contrib.admin.models import *
from django.contrib.contenttypes.models import *
from django.contrib.sessions.models import *
from django.db import migrations, models
from projects.models import *
from hours.models import *
from employees.models import *

models = {
    Group: 'Group',
    Permission: 'Permission',
    User: 'User',
    LogEntry: 'LogEntry',
    ContentType: 'ContentType',
    Session: 'Session',
    UserData: 'UserData',
    ReportingPeriod: 'ReportingPeriod',
    Timecard: 'Timecard',
    TimecardObject: 'TimecardObject',
    AccountingCode: 'AccountingCode',
    Agency: 'Agency',
    Project: 'Project',
    ProjectAlert: 'ProjectAlert',
    }

for i, x in models.items():
    print(i, x)
    model_data = serializers.serialize('json', i.objects.all())
    file_name = x + '_data.json'
    data_out = open(str(file_name), 'w')
    data_out.write(model_data)
