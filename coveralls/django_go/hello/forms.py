from django import forms

from hello.models import Staff, Supp1, Supp2, JobTitles


# class DepartmentsForm(forms.ModelForm):
#     #форма прямого ввода
#     class Meta:
#         model = Departments
#         fields = ("department", )


# ------------------------------------------------------------------------------------------
# пример выборки из 2 баз в одну по id
# ------------------------------------------------------------------------------------------
class PopularForm(forms.ModelForm):
    # форма выбора из бд часть отображения
    job = forms.ModelChoiceField(queryset=Supp1.objects.all(),
                                 empty_label="first")
    job1 = forms.ModelChoiceField(queryset=Supp2.objects.all(),
                                      empty_label="second")
    # popular = forms.ModelMultipleChoiceField(queryset=Staff.objects.all())
    class Meta:
        # часть передачи данных что - куда
        model = JobTitles
        fields = ("job", 'job1')