from django.shortcuts import render
from django.http import HttpResponse
from .models import my_upload, Serie, Speaker
# from .myforms import SearchTerm

number_per_page = 20
# Create your views here.
def home(request):
	allFiles = my_upload.objects.order_by("-pk")
	totalUploads = allFiles.count()
	totalPages = totalUploads / number_per_page
	if totalUploads % number_per_page == 0:
		totalPages = int(totalPages)
	else:
		totalPages += 1
		totalPages = int(totalPages)
	if totalPages > 1:
		nextPage = 2
	else:
		nextPage = 1
	context = {
		"previous_page" : 1,
		"next_page" : nextPage,
		"current_page" : 1,
		"total_pages" : totalPages,
		"files" : allFiles[:number_per_page],
	}
	return render(request, "ebc_app/home.html", context)


def homepage(request, page_no):
	allFiles = my_upload.objects.order_by("-pk")
	totalUploads = allFiles.count()
	totalPages = totalUploads / number_per_page
	if totalUploads % number_per_page == 0:
		totalPages = int(totalPages)
	else:
		totalPages += 1
		totalPages = int(totalPages)
	# requestedPage = int(page_no)
	# currentFile = requestedPage * number_per_page
	# endFile = currentFile + number_per_page
	# printFiles = allFiles[currentFile : endFile]
	# if requestedPage > 1:
	# 	 previousPage = requestedPage - 1
	# else:
	# 	totalPages += 1
	# 	totalPages = int(totalPages)
	requestedPage = int(page_no)
	currentFile = requestedPage * number_per_page - number_per_page
	endFile = currentFile + number_per_page
	printFiles = allFiles[currentFile : endFile]
	if requestedPage > 1:
		previousPage = requestedPage - 1
	else:
		previousPage = 1
	if requestedPage < totalPages:
		nextPage = requestedPage + 1
	else:
		nextPage = totalPages
	context = {
		"next_page" : nextPage,
		"previous_page" : previousPage,
		"current_page" : requestedPage,
		"total_pages" : totalPages,
		"files" : printFiles,
	}
	return render(request, "ebc_app/home.html", context)


def searchome(request):
	# return HttpResponse("WWW")
	if request.method == "GET":
		rawTexts = request.GET.get('search_txt')
		rawText = rawTexts.lower()
		searchMethod = request.GET.get('search_criteria')
		if searchMethod == "by_title":
			allFiles = my_upload.objects.filter(file_title__icontains=rawText)
		elif searchMethod == "by_speaker":
			allFiles = my_upload.objects.filter(speaker__name__icontains=rawText)
		else:
			allFiles = my_upload.objects.filter(series__theme__icontains=rawText)
		totalUploads = allFiles.count()
		totalPages = totalUploads / number_per_page
		if totalUploads % number_per_page == 0:
			totalPages = int(totalPages)
		else:
			totalPages += 1
			totalPages = int(totalPages)
		printFiles = allFiles[ : number_per_page]
		if totalPages > 1:
			nextPage = 2
		else:
			nextPage = 1
		context = {
			"next_page" : nextPage,
			"previous_page" : 1,
			"current_page" : 1,
			"total_pages" : totalPages,
			"files" : printFiles,
			"search_text" : rawText,
		}
		return render(request, "ebc_app/home.html", context)


def search_page(request, search_text, page_no):
	rawTexts = search_text
	rawText = rawTexts.lower()
	allFiles = my_upload.objects.filter(file_title__icontains=rawText)
	totalUploads = allFiles.count()
	totalPages = totalUploads / number_per_page
	if totalUploads % number_per_page == 0:
		totalPages = int(totalPages)
	else:
		totalPages += 1
		totalPages = int(totalPages)

	requestedPage = int(page_no)
	currentFile = requestedPage * number_per_page - number_per_page
	endFile = currentFile + number_per_page
	printFiles = allFiles[currentFile : endFile]
	if requestedPage > 1:
		previousPage = requestedPage - 1
	else:
		previousPage = 1
	if requestedPage < totalPages:
		nextPage = requestedPage + 1
	else:
		nextPage = totalPages

	context = {
		"next_page" : nextPage,
		"previous_page" : previousPage,
		"current_page" : requestedPage,
		"total_pages" : totalPages,
		"files" : printFiles,
		"search_text" : rawText,
	}
	return render(request, "ebc_app/home.html", context)
