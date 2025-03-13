from django.shortcuts import render


def home_view(request):

    return render(request, 'jobboard2/index.html')


def blog_view(request):
    return render(request, 'jobboard2/blog.html')

def candidate_view(request):
    return render(request, 'jobboard2/candidate.html')

def jobs_view(request):
    return render(request, 'jobboard2/jobs.html')

def job_detail_view(request):
    return render(request, 'jobboard2/job_details.html')