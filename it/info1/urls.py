from django.urls import path
from info1.views import index_page, create_name, user_name_details, delete_user_name, user_names_user_birth_create, delete_birth, user_info_create, subject_create, delete_info, delete_practice, delete_medicine, delete_doctor, delete_professor, delete_subject
from info1.views import  user_work_create, practice_create, criminal_create, medicine_create, master_create, doctor_create, phd_create, all_page, professor_create, sport_create, delete_work, delete_criminal, delete_master, delete_phd, delete_sport

urlpatterns = [
    path('', index_page, name='index'),
    path('info1/create/', create_name, name='create_name'),
    path('info1/<int:pk>/', user_name_details, name='user_name_details'),
    path('info1/<int:pk>/delete/', delete_user_name, name='delete_user_name'),
    path('info1/<int:pk>/user_births-create', user_names_user_birth_create, name='user_names_user_birth_create'),
    path('info1/<int:pk>/delete_1', delete_birth, name='delete_birth'),
    path('info1/<int:pk>/delete_2', delete_info, name='delete_info'),
    path('info1/<int:pk>/delete_3', delete_work, name='delete_work'),
    path('info1/<int:pk>/delete_4', delete_practice, name='delete_practice'),
    path('info1/<int:pk>/delete_5', delete_criminal, name='delete_criminal'),
    path('info1/<int:pk>/delete_6', delete_medicine, name='delete_medicine'),
    path('info1/<int:pk>/delete_7', delete_master, name='delete_master'),
    path('info1/<int:pk>/delete_8', delete_doctor, name='delete_doctor'),
    path('info1/<int:pk>/delete_9', delete_phd, name='delete_phd'),
    path('info1/<int:pk>/delete_10', delete_professor, name='delete_professor'),
    path('info1/<int:pk>/delete_11', delete_sport, name='delete_sport'),
    path('info1/<int:pk>/delete_12', delete_subject, name='delete_subject'),
    path('info1/<int:pk>/user_infos-create', user_info_create, name='user_info_create'),
    path('info1/<int:pk>/user_works-create', user_work_create, name='user_work_create'),
    path('info1/<int:pk>/practices-create', practice_create, name='practice_create'),
    path('info1/<int:pk>/criminals-create', criminal_create, name='criminal_create'),
    path('info1/<int:pk>/criminals-create', criminal_create, name='criminal_create'),
    path('info1/<int:pk>/medicines-create', medicine_create, name='medicine_create'),
    path('info1/<int:pk>/masters-create', master_create, name='master_create'),
    path('info1/<int:pk>/doctors-create', doctor_create, name='doctor_create'),
    path('info1/<int:pk>/phds-create', phd_create, name='phd_create'),
    path('info1/<int:pk>/professors-create', professor_create, name='professor_create'),
    path('info1/<int:pk>/sports-create', sport_create, name='sport_create'),
    path('info1/<int:pk>/subjects-create', subject_create, name='subject_create'),
    path('all.html', all_page, name='all'),
]

    