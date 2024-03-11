from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # FIXME: Validate that 'issue_date' is not a future date
        fields = ("issue_date", "description")
        labels = {
            "issue_date": "When did the issue started?",
            "description": "Add a detailed description of the problem"
        }

        widgets = {
            "issue_date": forms.DateInput({"class": "form-control", "type": "date"}),
            "description": forms.Textarea({"class": "form-control", "rows": "5"}),
        }
