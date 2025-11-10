from django import forms

from cinemaapp.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'announcement_date': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'title': 'Title of the movie',
            'synopsis': 'Short plot summary',
            'genre': 'Movie genre',
            'director': "Director's full name",
            'release_year': 'Year of release',
            'duration': 'Duration (in minutes)',
            'release_date': 'Release date',
            'announcement_date': 'Announcement date',
            'has_subtitles': 'Has subtitles',
            'subtitles_language': 'Subtitles language',
            'imdb': 'IMDB URL',
            'rating': 'Average rating (0-10)',
        }
        error_messages = {
            'title': {
                'max_length': 'The title of the movie must not be more than 100 characters long',
                'required': 'The title of the movie is required'
            },
            'genre': {
                'required': 'The genre of the movie is required',
            },
            'release_year': {
                'min_value': 'The year of release must not be earlier than 1900'
            },
            'duration': {
                'min_value': 'The duration must be between 1 and 500 minutes',
                'max_value': 'The duration must be between 1 and 500 minutes',
            },
            'release_date': {
                'required': 'The release date is required',
            },
            'rating': {
                'min_value': 'The average rating must be between 0,0 and 10,0',
                'max_value': 'The average rating must be between 0,0 and 10,0',
            }
        }