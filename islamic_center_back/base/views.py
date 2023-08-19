from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from  django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from base.forms import SignUpForm, MainNewsForm, MainNewsFormUz, MainNewsFormEn, TimetableForm, AboutUsRuForm, AboutUsEnForm, AboutUsUzForm
from base.models import MainNews, MainNewsEn, MainNewsUz, Timetable, AboutUsRu, AboutUsEn, AboutUsUz
import logging
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from base.models import Language, News
from base.models import UserDetails



class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            context['lang'] = lang_model.name
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            context['lang'] = langCookie
        
        return context


class RegisterAjax(TemplateView):
    def post(self, request):
        email = request.POST.get('email')
        Username = request.POST.get('Username')
        Password1 = request.POST.get('Password1')
        # Password2 = request.POST.get('Password2')
        Person_FirstName = request.POST.get('Person_FirstName')
        Person_MiddleName = request.POST.get('Person_MiddleName')
        Person_LastName = request.POST.get('Person_LastName')
        phone_number_personal = request.POST.get('phone_number_personal')
        phone_number_home = request.POST.get('phone_number_home')
        Person_MaritalStatus = request.POST.get('Person_MaritalStatus')
        Person_Household = request.POST.get('Person_Household')
        Person_ResidentialStatus = request.POST.get('Person_ResidentialStatus')
        other_res = request.POST.get('other_res')
        Person_Profession = request.POST.get('Person_Profession')
        mem_platinum = request.POST.get('mem_platinum')
        mem_gold = request.POST.get('mem_gold')
        mem_silver = request.POST.get('mem_silver')
        DonationAmount = request.POST.get('DonationAmount')
        Frequency = request.POST.get('Frequency')
        date_picker = request.POST.get('date_picker')

        # Создание пользователя
        user = User.objects.create_user(
            username=Username,
            email=email,
            password=Password1,
            first_name=Person_FirstName,
            last_name=Person_LastName
        )

        # Создание экземпляра модели UserDetails
        user_details = UserDetails(
            user=user,
            email=email,
            username=Username,
            phone_number_personal=phone_number_personal,
            phone_number_work=phone_number_home,
            marital_status=Person_MaritalStatus,
            number_of_children=Person_Household,
            residental_status=Person_ResidentialStatus,
            type_of_work='Full-time',
            type_of_membership='Gold',
            donation_amount=int(DonationAmount),
            donation_frequency='Monthly',
            donation_date='2023-01-01'
        )

        # Сохранение данных
        user_details.save()
        login(request, user)

        return JsonResponse({
            'email': email,
            'Password1': Password1,
            'Username': Username,
            'Person_LastName': Person_LastName,
            'phone_number_personal': phone_number_personal
        })


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = SignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            context['lang'] = lang_model.name
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            context['lang'] = langCookie
        
        return context

    
class Main(TemplateView):
    template_name = 'base/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            try:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language.objects.get(user_id_id=user.id)
                if lang_model.name == "ru":
                    select_news = MainNews.objects.all()
                elif lang_model.name == "uz":
                    select_news = MainNewsUz.objects.all()
                elif lang_model.name == "en":
                    select_news = MainNewsEn.objects.all()
            except Language.DoesNotExist:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language(user_id=user, name="ru")
                lang_model.save()
                select_news = MainNews.objects.all()

            context['news_list'] = select_news
            context['lang'] = lang_model.name
            return context
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            logging.info(langCookie)
            if langCookie is None:
                langCookie = "en"
            if langCookie == "ru":
                select_news = MainNews.objects.all()
            elif langCookie == "uz":
                select_news = MainNewsUz.objects.all()
            elif langCookie == "en":
                select_news = MainNewsEn.objects.all()
            context['news_list'] = select_news
            context['lang'] = langCookie
            return context


class News(TemplateView):
    template_name = 'base/main_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            try:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language.objects.get(user_id_id=user.id)
                if lang_model.name == "ru":
                    select_news = MainNews.objects.all()
                elif lang_model.name == "uz":
                    select_news = MainNewsUz.objects.all()
                elif lang_model.name == "en":
                    select_news = MainNewsEn.objects.all()
            except Language.DoesNotExist:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language(user_id=user, name="ru")
                lang_model.save()
                select_news = MainNews.objects.all()

            context['news_list'] = select_news
            context['lang'] = lang_model.name
            return context
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            logging.info(langCookie)
            if langCookie is None:
                langCookie = "en"
            if langCookie == "ru":
                select_news = MainNews.objects.all()
            elif langCookie == "uz":
                select_news = MainNewsUz.objects.all()
            elif langCookie == "en":
                select_news = MainNewsEn.objects.all()
            context['news_list'] = select_news
            context['lang'] = langCookie
            return context


class Charity(TemplateView):
    template_name = 'base/charity.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            context['lang'] = lang_model.name
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            context['lang'] = langCookie
        
        return context


class About(TemplateView):
    template_name = 'base/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            try:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language.objects.get(user_id_id=user.id)
                if lang_model.name == "ru":
                    about_us = AboutUsRu.objects.all()
                elif lang_model.name == "uz":
                    about_us = AboutUsUz.objects.all()
                elif lang_model.name == "en":
                    about_us = AboutUsEn.objects.all()
            except Language.DoesNotExist:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language(user_id=user, name="ru")
                lang_model.save()
                about_us = AboutUsRu.objects.all()

            context['about_us'] = about_us
            context['lang'] = lang_model.name
            return context
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            logging.info(langCookie)
            if langCookie is None:
                langCookie = "en"
            if langCookie == "ru":
                about_us = AboutUsRu.objects.all()
            elif langCookie == "uz":
                about_us = AboutUsUz.objects.all()
            elif langCookie == "en":
                about_us = AboutUsEn.objects.all()
            context['about_us'] = about_us
            context['lang'] = langCookie
        return context


class AboutUsEdit(View):
    def post(self, request):
        if request.method == "POST":
            user = User.objects.get(id=request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            if lang_model.name == "ru":
                about_us = AboutUsRu.objects.get(id=1)
                about_us.title = request.POST.get('title')
                about_us.text = request.POST.get('text')
                about_us.save()
            elif lang_model.name == "uz":
                about_us = AboutUsUz.objects.get(id=1)
                about_us.title = request.POST.get('title')
                about_us.text = request.POST.get('text')
                about_us.save()
            elif lang_model.name == "en":
                about_us = AboutUsEn.objects.get(id=1)
                about_us.title = request.POST.get('title')
                about_us.text = request.POST.get('text')
                about_us.save()
            return redirect('about')
        else:
            return redirect('main')


class Contacts(TemplateView):
    template_name = 'base/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            context['lang'] = lang_model.name
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            context['lang'] = langCookie
        
        return context


class Museum(TemplateView):
    template_name = 'base/museum.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            context['lang'] = lang_model.name
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            context['lang'] = langCookie
        
        return context

 
@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class DeleteNews(TemplateView):
    def get(self, request, *args, **kwargs):
        news_id = request.GET['news_id']

        user = User.objects.get(id=request.user.id)
        lang_model = Language.objects.get(user_id_id=user.id)
        if lang_model.name == "ru":
            news = MainNews.objects.get(id=news_id)
        elif lang_model.name == "uz":
            news = MainNewsUz.objects.get(id=news_id)
        elif lang_model.name == "en":
            news = MainNewsEn.objects.get(id=news_id)

        
        news.delete()
        return JsonResponse({'status': 'ok'})


class TimeTable(TemplateView, View):
    template_name = 'base/timetable.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            try:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language.objects.get(user_id_id=user.id)
                select_timetable = Timetable.objects.all()
            except Language.DoesNotExist:
                user = User.objects.get(id=self.request.user.id)
                lang_model = Language(user_id=user, name="ru")
                lang_model.save()
                select_timetable = Timetable.objects.all()

            context['timetable_list'] = select_timetable
            context['lang'] = lang_model.name
            return context
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            logging.info(langCookie)
            if langCookie is None:
                langCookie = "en"
            select_timetable = Timetable.objects.all()
            context['timetable_list'] = select_timetable
            context['lang'] = langCookie
            return context
        


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class AddTimetable(TemplateView):
    template_name = 'base/addtimetable.html'

    def post(self, request, *args, **kwargs):        
        form = TimetableForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect('timetable')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            context['lang'] = lang_model.name
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            context['lang'] = langCookie
        
        return context



@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class EditTimetable(View):
    def post(self, request, *args, **kwargs):
        timetable_id = request.POST['timetable_id']
        date =  request.POST['date']
        timeSunrise =  request.POST['timeSunrise']
        timeSunset = request.POST['timeSunset']
        timeSatar = request.POST['timeSatar']
        timeFajr = request.POST['timeFajr']
        timeZuhr = request.POST['timeZuhr']
        timeAsr = request.POST['timeAsr']
        timetable = Timetable.objects.get(timetable_id=timetable_id)
        form = TimetableForm(request.POST, request.FILES, instance=timetable)

        if Timetable.objects.filter(timetable_id=timetable_id).exists():
            try:
                timetable.date = date
                timetable.time_sunrise = timeSunrise
                timetable.time_sunset = timeSunset
                timetable.time_satar = timeSatar
                timetable.time_fajr = timeFajr
                timetable.time_zuhr = timeZuhr
                timetable.time_asr = timeAsr
                timetable.save()

                return JsonResponse({'status': 'ok'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        return HttpResponse('ok')
    

@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class DeleteTimetable(TemplateView):
    def get(self, request, *args, **kwargs):
        timetable_id = request.GET['timetable_id']

        timetable = Timetable.objects.get(timetable_id=timetable_id)

        
        timetable.delete()
        return JsonResponse({'status': 'ok'})


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class AddNews(FormView):
    template_name = 'base/addnews.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        lang_model = Language.objects.get(user_id_id=user.id)
        if lang_model.name == "ru":
            form = MainNewsForm(request.POST, request.FILES)
        elif lang_model.name == "uz":
            form = MainNewsFormUz(request.POST, request.FILES)
        elif lang_model.name == "en":
            form = MainNewsFormEn(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('news')
        return render(request, 'base/addnews.html', {'form': form, 'lang': lang_model.name})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            lang_model = Language.objects.get(user_id_id=user.id)
            context['lang'] = lang_model.name
        else:
            langCookie = self.request.COOKIES.get('langCookie')
            context['lang'] = langCookie
        
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = User.objects.get(id=self.request.user.id)
    #     lang_model = Language.objects.get(user_id_id=user.id)
    #     context['lang'] = lang_model.name
    #     return context
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        lang_model = Language.objects.get(user_id_id=user.id)
        if lang_model.name == "ru":
            form = MainNewsForm()
        elif lang_model.name == "uz":
            form = MainNewsFormUz()
        elif lang_model.name == "en":
            form = MainNewsFormEn()
        
        if request.user.is_authenticated:
            lang_model = Language.objects.get(user_id_id=user.id)
            return render(request, 'base/addnews.html', {'form': form, 'lang': lang_model.name})
        else:
            return render(request, 'base/addnews.html', {'form': form, 'lang': request.COOKIES.get('langCookie')})


class SetLanguage(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                lang = request.GET['lang']
                user = User.objects.get(id=request.user.id)
                lang_model = Language.objects.get(user_id_id=user.id)
                lang_model.name = lang
                lang_model.save()
                return JsonResponse({'status': 'ok'})
            except Language.DoesNotExist:
                try:
                    user = User.objects.get(id=request.user.id)
                    lang_model = Language(user_id=user, name=lang)
                    lang_model.save()
                    return JsonResponse({'status': 'ok'})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': str(e)})
                finally:
                    return JsonResponse({'status': 'nothing'})
        else:
            return JsonResponse({'status': 'nothing'})


class GetLanguage(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                user = User.objects.get(id=request.user.id)
                lang = Language.objects.get(user_id_id=user.id)
                return JsonResponse({'status': 'ok', 'lang': lang.name})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:
            langCookie = request.COOKIES.get('langCookie')
            return JsonResponse({'status': 'ok', 'lang': langCookie})
