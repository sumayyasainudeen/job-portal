from jobPortalApp import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('software',views.software,name='software'),
    path('js_signin_page',views.js_signin_page,name='js_signin_page'),
    path('js_signup_page',views.js_signup_page,name='js_signup_page'),
    path('jobseeker_signup',views.jobseeker_signup,name='jobseeker_signup'),
    path('jobseeker_signin',views.jobseeker_signin,name='jobseeker_signin'),
    path('signout',views.signout,name='signout'),
    path('resume_upload_page',views.resume_upload_page,name='resume_upload_page'),
    path('myjobs',views.myjobs,name='myjobs'),
    path('message',views.message,name='message'),
    path('notifications',views.notifications,name='notifications'),

    path('em_signin_page',views.em_signin_page,name='em_signin_page'),
    path('em_signup_page',views.em_signup_page,name='em_signup_page'),
    path('employer_signup',views.employer_signup,name='employer_signup'),
    path('employer_signin',views.employer_signin,name='employer_signin'),
    path('emp_home',views.emp_home,name='emp_home'),
    path('post_job_page',views.post_job_page,name='post_job_page'),
    path('create_company',views.create_company,name='create_company'),
    path('postedjobs',views.postedjobs,name='postedjobs'),
    path('editjob',views.editjob,name='editjob'),
]