from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from . import models, forms, madule
from apps.course.models import Course, CourseCategory
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.account.models import Address


class TeacherListView(ListView):
    model = models.Teacher
    queryset = models.Teacher.objects.filter(is_valid=True)
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        return madule.filter_teacher(self.request, queryset)


class TeacherDetailView(DetailView):
    model = models.Teacher
    queryset = models.Teacher.objects.filter(is_valid=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Course.objects.filter(is_publish=True, teacher__id=self.kwargs['pk']).values_list(
            'category').distinct()
        related_teachers = models.Teacher.objects.filter(course__category__in=categories).exclude(
            id=self.kwargs['pk']).distinct()

        context['related_teachers'] = related_teachers
        return context





class FirstStageAdmissionView(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.FirstStageAdmissionForm(instance=self.request.user)
        return render(request, 'teacher/firstـstageـadmission.html', {'form': form})

    def post(self, request):
        form = forms.FirstStageAdmissionForm(request.POST, instance=self.request.user)
        if form.is_valid():
            form.save()
            return redirect('teacher_app:second_stage_admission')

        return render(request, 'teacher/firstـstageـadmission.html', {'form': form})


class SecondStageAdmission(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.SecondStageAdmissionForm()
        return render(request, 'teacher/secondـstageـadmission.html', {'form': form})

    def post(self, request):
        form = forms.SecondStageAdmissionForm(request.POST)
        if form.is_valid:
            try:
                teacher = form.save(commit=False)
                teacher.user = self.request.user
                teacher.save()
                return redirect('teacher_app:third_stage_admission')
            except:
                return redirect('/')
        messages.error(request, 'Please enter the information correctly')
        return render(request, 'teacher/secondـstageـadmission.html', {'form': form})


class ThirdStageAdmission(LoginRequiredMixin, View):
    def get(self, request):
        address = self.request.user.address.all()
        return render(request, 'teacher/thirdـstageـadmission.html', {'address': address})

    def post(self, request):
        address = request.POST.get('address')
        address = Address.objects.get(full_address=address)
        address_user = Address.objects.filter(is_active=True)
        if address_user.exists():
            address_user[0].is_active = False
            address_user[0].save()

        address.is_active = True
        address.save()

        return redirect('teacher_app:Fourth_stage_admission')


class FourthStageAdmission(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.FourthStageAdmissionForm()
        return render(request, 'teacher/fourthـstageـadmission.html', {'form': form})

    def post(self, request):
        form = forms.FourthStageAdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.teacher = self.request.user.teacher
            work.save()
            messages.success(request, "Your job has been registered successfully"
                                      ", if you don't have another job, go to the next step")

        return render(request, 'teacher/fourthـstageـadmission.html', {'form': form})


class FifthStageAdmissionView(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.FifthStageAdmissionForm()
        return render(request, 'teacher/fifthـstageـadmission.html', {'form': form})

    def post(self, request):
        form = forms.FifthStageAdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.teacher = self.request.user.teacher
            skill.save()
            messages.success(request, "Your skill has been registered successfully,"
                                      "if you don't have another skill, go to the next step")

        return render(request, 'teacher/fifthـstageـadmission.html', {'form': form})


class SixthStageAdmissionView(View):
    def get(self, request):
        form = forms.SixthStageAdmissionForm()
        return render(request, 'teacher/sixth_stage_admission.html', {'form': form})

    def post(self, request):
        form = forms.SixthStageAdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            level_education = form.save(commit=False)
            level_education.teacher = self.request.user.teacher
            level_education.save()
            messages.success(request, "Your level education has been registered successfully,"
                                      "if you don't have another level education , go to the next step")
        return render(request, 'teacher/sixth_stage_admission.html', {'form': form})


class TeacherAddedView(TemplateView):
    template_name = 'teacher/teacher_add.html'
