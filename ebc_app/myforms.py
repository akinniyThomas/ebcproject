from django import forms

class SearchTerm(forms.Form):
	search_term = forms.CharField(label = "Search", max_length = 100)

	"""docstring for SearchTerm"""
	# def __init__(self, arg):
	# 	super(SearchTerm, self).__init__()
	# 	self.arg = arg
