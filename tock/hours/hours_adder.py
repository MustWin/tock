from django.template.defaultfilters import pluralize
from decimal import Decimal, InvalidOperation
from .models import ReportingPeriod, Timecard, TimecardObject, Project, ReportingPeriod
import datetime

ERROR_MSG = """
    Oops.
    That command was not correct and no time was added to your timecard.
    Try again by entering a URL with this format:
    tock.gov/addHours?project=231&hours=1
"""

NEGATIVE_HOURS_ERROR_MSG = "The total hours after the operation cannot be negative"
SUBMIT_ERROR_MSG = "A submitted timecard for the current period already exists"
INVALID_PERIOD_MSG = "Could not find a current time period"

class HoursAdder(object):
    """Service object in charge of adding hours to a timecard object.
    self.current_date is an optional argument used for Dependency Injection during tests.
    """

    def __init__(self, **kwargs):
        self.project_id = kwargs.get('project_id', None)
        self.hours = kwargs.get('hours', None)
        self.reporting_period_id = kwargs.get('reporting_period_id', None)
        self.message = "Unknown error"
        self.user_id = kwargs.get('user_id', None)
        self.operation_was_successful = False
        self.undo_url = kwargs.get('undo_url', '')
        self.current_date = kwargs.get('current_date', None)

    def generate_successful_message(self, hours, project):
        if hours > 0:
            plural_hours = pluralize(hours, 'hour,hours')
            has = pluralize(hours, 'has,have')
            undo_query = "?hours=-%s&project=%s" % (hours, project.id)
            undo_tag = "<a href=\"%s\">Undo</a>" % (self.undo_url + undo_query)
            return "%s %s %s been added to %s. %s" % (hours, plural_hours, has,
                    project.name, undo_tag)

        plural_hours = pluralize(-hours, 'hour,hours')
        has = pluralize(-hours, 'has,have')
        return "%s %s %s been removed from %s." % (-hours, plural_hours, has,
                project.name)

    def inputs_are_invalid(self):
        if self.hours is None:
            return True

        if self.project_id is None:
            return True

        if self.reporting_period_id is None:
            return True

        if self.current_date is None:
            self.current_date = datetime.datetime.now().date()

        try:
            reporting_period = ReportingPeriod.objects.get(id=self.reporting_period_id)
        except ReportingPeriod.DoesNotExist:
            self.message = ERROR_MSG
            return True

        if reporting_period.start_date > self.current_date:
            self.message = INVALID_PERIOD_MSG
            return True

        if reporting_period.end_date < self.current_date:
            self.message = INVALID_PERIOD_MSG
            return True

        try:
            self.hours = Decimal(self.hours)
        except InvalidOperation:
            return True
        except TypeError:
            return True

        try:
            self.project_id = int(self.project_id)
        except TypeError:
            return True
        except ValueError:
            return True

        return False

    def perform_operation(self):
        if self.inputs_are_invalid():
            self.message = ERROR_MSG
            return

        try:
            project = Project.objects.get(id=self.project_id)
        except Project.DoesNotExist:
            self.message = ERROR_MSG
            return

        submited_timecards_current_period = Timecard.objects.filter(
            reporting_period_id=self.reporting_period_id,
            submitted=True,
            user_id=self.user_id
        )

        if len(submited_timecards_current_period) > 0:
            self.message = SUBMIT_ERROR_MSG
            return

        tc, created = Timecard.objects.get_or_create(
            reporting_period_id=self.reporting_period_id,
            user_id=self.user_id)

        tco, created = TimecardObject.objects.get_or_create(
            timecard_id=tc.id,
            project_id=project.id)


        if tco.hours_spent is None:
            tco.hours_spent = 0

        updated_hours = tco.hours_spent + self.hours
        if updated_hours < 0:
            self.message = NEGATIVE_HOURS_ERROR_MSG
            return

        tco.hours_spent = updated_hours
        tco.save()
        tc.save()

        self.message = self.generate_successful_message(self.hours, project)
        self.operation_was_successful = True

    def successful(self):
        return self.operation_was_successful

    def message(self):
        return self.message