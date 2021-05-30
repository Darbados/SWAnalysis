from django import forms


class ValueCountsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.value_fields = kwargs.pop('header_fields')
        super().__init__(*args, **kwargs)

        for field in self.value_fields:
            self.fields[field] = forms.BooleanField(required=False)

    def get_changed_fields(self):
        if self.is_valid():
            return self.changed_data
        return []
