from django import forms
from .models import Review


class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ["book"]
        labels = {
            "user_name": "Your Name",
            "review_text": "Your FeedBack",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name",
            }
        }
