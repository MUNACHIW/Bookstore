from django import forms
from .model import Review


class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ['']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your FeedBack",
            "Rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name",
            }
        }
