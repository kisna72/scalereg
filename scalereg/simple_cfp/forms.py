from django.forms import ModelForm
from scalereg.simple_cfp.models import Presentation
from scalereg.simple_cfp.models import Speaker


class PresentationForm(ModelForm):
  class Meta:
    model = Presentation
    fields = (
      'speaker_code',
      'categories',
      'audiences',
      'title',
      'description',
      'short_abstract',
      'long_abstract',
    )


class SpeakerForm(ModelForm):
  class Meta:
    model = Speaker
    fields = (
      'salutation',
      'first_name',
      'last_name',
      'title',
      'org',
      'zip',
      'email',
      'phone',
      'url',
      'bio',
    )
