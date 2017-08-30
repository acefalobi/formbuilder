from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import *
from .models import *

from datetime import datetime, timedelta


# Create your views here.
def landing_page(request):
    return HttpResponseRedirect('/dashboard')


@login_required()
def dashboard(request):
    user = request.user
    user_forms = user.form_set.order_by('-publishedDate')

    user_forms_submission_count = []

    for user_form in user_forms:
        user_forms_submission_count.append(user_form.formsubmission_set.count())

    variables = {
        'user_forms_submission_count': user_forms_submission_count,
        'user_forms': user_forms,
        'dashboard': True,
    }

    return render(request, "dashboard.html", variables)


def login_redirection_page(request):
    return HttpResponseRedirect('/login')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            if user:
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponseRedirect('/register')
    else:
        form = RegistrationForm()

    variables = {
        'form': form
    }
    return render(request, "registration/register.html", variables)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required()
def form_new(request):
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            form_to_create = form_save(request, form, False)
            return HttpResponseRedirect('/forms/' + form_to_create.id)

    else:
        form = FormForm()

    variables = {
        'form': form
    }

    return render(request, "form_new.html", variables)


@login_required()
def form_edit(request, form_id):
    form_to_edit = get_object_or_404(Form, id=form_id)

    if form_to_edit.user.username == request.user.username:
        if request.method == 'POST':
            form = FormForm(request.POST)
            if form.is_valid():
                form_save(request, form, form_id)
                return HttpResponseRedirect('/forms/' + form_id)

        else:
            form = FormForm({
                'title': form_to_edit.title,
                'jsonForm': form_to_edit.jsonForm
            })
    else:
        raise Http404('Form does not exist')

    variables = {
        'form': form
    }

    return render(request, "form_edit.html", variables)


def form_save(request, form, form_id):
    if form_id:
        form_to_save = Form.objects.get(id=form_id)
    else:
        form_to_save = Form.objects.create(user=request.user)

    form_to_save.title = form.cleaned_data['title']
    form_to_save.jsonForm = form.cleaned_data['jsonForm']

    form_to_save.save()

    return form_to_save


@login_required()
def form_delete(request, form_id):
    form_to_delete = get_object_or_404(Form, id=form_id)

    if form_to_delete.user.username == request.user.username:
        if request.method == 'GET':
            form_to_delete.delete()
            return HttpResponseRedirect('/dashboard')
    else:
        raise Http404('Form does not exist')


def form_view(request, form_id):
    try:
        form_to_view = Form.objects.get(id=form_id)
    except ObjectDoesNotExist:
        raise Http404('Form does not exist')

    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            form_submission_save(request, form, form_to_view)
            return HttpResponseRedirect('/forms/submit/success')

    else:
        form = FormSubmissionForm()

    variables = {
        'form': form,
        'form_to_view': form_to_view
    }

    return render(request, 'form_view.html', variables)


def form_submission_save(request, form, form_to_submit):
    submission_to_save = FormSubmission.objects.create(form=form_to_submit)
    submission_to_save.jsonSubmission = form.cleaned_data['jsonFormSubmission']

    submission_to_save.save()

    return submission_to_save


@login_required()
def form_submissions(request, form_id):
    form_to_view = get_object_or_404(Form, id=form_id)

    if form_to_view.user.username != request.user.username:
        raise Http404('Form does not exist')

    submissions = form_to_view.formsubmission_set.order_by("-publishedDate")

    variables = {
        'form_to_view': form_to_view,
        'submissions': submissions
    }

    return render(request, 'form_submissions.html', variables)


@login_required()
def form_download_submissions(request, form_id):
    form_to_download = get_object_or_404(Form, id=form_id)

    if form_to_download.user.username != request.user.username:
        raise Http404('Form does not exist')

    # submissions = form_to_download.formsubmission_set.order_by("-publishedDate")

    # for submission in submissions:
    #

    return HttpResponseRedirect('/dashboard')


def form_submit_success(request):
    return render(request, "form_submit_success.html")
