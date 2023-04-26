from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from info1.models import User_name, User_birth, User_info, User_work, Practice, Criminal, Medicine, Master, Doctor, Phd, Professor, Sport, Subject
from info1.forms import CreateNameForm, CreateBirthForm, CreateInfoForm, CreateWorkForm, CreatePracticeForm, CreateCriminalForm, CreateMedicineForm, CreateMasterForm, CreateDoctorForm ,CreatePhdForm, CreateProfessorForm, CreateSportForm, CreateSubjectForm


def index_page(request):
    if request.user.is_authenticated:
        user_names = User_name.objects.filter(owner_id=request.user.id)
        return render(request, 'info1/index.html', {'user_names': user_names, 'user': request.user})
    else:
        return redirect('/auth/login/')


def create_name(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateNameForm()
            return render(request, 'info1/create-name.html', {'form': form})
        if request.method == 'POST':
            form = CreateNameForm(request.POST)
            if form.is_valid():
                firstname = form.data.get('firstname')
                secondname = form.data.get('secondname')
                user_name = User_name(firstname=firstname, secondname=secondname, owner_id=request.user.id)
                user_name.save()
                return redirect('/')
            else:
                return render(request, 'info1/create-name.html', {'form': form})
    else:
        return redirect('/auth/login/')


def user_name_details(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        user_births = User_birth.objects.filter(user_name_id=pk).order_by('-created_at')
        user_infos = User_info.objects.filter(user_name_id=pk).order_by
        user_works = User_work.objects.filter(user_name_id=pk).order_by
        practices = Practice.objects.filter(user_name_id=pk).order_by
        criminals = Criminal.objects.filter(user_name_id=pk).order_by
        medicines = Medicine.objects.filter(user_name_id=pk).order_by
        masters = Master.objects.filter(user_name_id=pk).order_by
        doctors = Doctor.objects.filter(user_name_id=pk).order_by
        phds = Phd.objects.filter(user_name_id=pk).order_by
        professors = Professor.objects.filter(user_name_id=pk).order_by
        sports = Sport.objects.filter(user_name_id=pk).order_by
        subjects = Subject.objects.filter(user_name_id=pk).order_by
        form = CreateBirthForm()
        form1 = CreateInfoForm()
        form2 = CreateWorkForm()
        form3 = CreatePracticeForm()
        form4 = CreateCriminalForm()
        form5 = CreateMedicineForm()
        form6 = CreateMasterForm()
        form7 = CreateDoctorForm()
        form8 = CreatePhdForm()
        form9 = CreateProfessorForm()
        form10 = CreateSportForm()
        form11 = CreateSubjectForm()
        return render(request, 'info1/user-name-details.html', {'user_name': user_name, 'user_births':user_births, 'user_infos':user_infos, 'user_works':user_works, 'practices':practices,
             'criminals':criminals, 'medicines':medicines, 'masters':masters, 'doctors':doctors, 'phds':phds, 'professors':professors, 'sports':sports, 'subjects':subjects,
            'form':form, 'form1':form1, 'form2':form2,'form3':form3, 'form4':form4, 'form5':form5, 'form6':form6, 'form7':form7, 'form8':form8, 'form9':form9, 'form10':form10, 'form11':form11})
    else:
        return redirect('/auth/login/')
    
def user_names_user_birth_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateBirthForm(request.POST)
            if form.is_valid():
                date_of_birth = form.data.get('date_of_birth')
                place_of_birth = form.data.get('place_of_birth')
                user_birth = User_birth(date_of_birth=date_of_birth, place_of_birth=place_of_birth, id=user_name.id, user_name=user_name )
                user_birth.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def user_info_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateInfoForm(request.POST)
            if form.is_valid():
                specialization = form.data.get('specialization')
                orga_of_education = form.data.get('orga_of_education')
                year_of_graduation = form.data.get('year_of_graduation')
                user_info = User_info(
                    id=user_name.id,  # устанавливаем id равным id user_name
                    specialization=specialization,
                    orga_of_education=orga_of_education,
                    year_of_graduation=year_of_graduation,
                    user_name=user_name  # устанавливаем связь с user_name
                )
                user_info.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')



def delete_birth(request, pk):
    if request.user.is_authenticated:
        user_birth = User_birth.objects.get(id=pk)
        user_name = User_name.objects.get(id=user_birth.user_name.id)
        if user_name.owner.id == request.user.id:
            user_birth.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')


def delete_user_name(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if user_name.owner.id == request.user.id:
            user_name.delete()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_info(request, pk):
    if request.user.is_authenticated:
            user_info = User_info.objects.get(id=pk)
            user_name = User_name.objects.get(id=user_info.user_name.id)
            if user_name.owner.id == request.user.id:
                user_info.delete()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
    else:
        return redirect('/auth/login/')

    
def user_work_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateWorkForm(request.POST)
            if form.is_valid():
                address = form.data.get('address')
                organization = form.data.get('organization')
                user_work = User_work(address=address,organization=organization, id=user_name.id, user_name=user_name)
                user_work.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_work(request, pk):
    if request.user.is_authenticated:
        user_work = User_work.objects.get(id=pk)
        user_name = User_name.objects.get(id=user_work.user_name.id)
        if user_name.owner.id == request.user.id:
            user_work.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def practice_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreatePracticeForm(request.POST)
            if form.is_valid():
                experience = form.data.get('experience')
                practice = Practice(experience=experience, id=user_name.id, user_name=user_name)
                practice.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_practice(request, pk):
    if request.user.is_authenticated:
        practice = Practice.objects.get(id=pk)
        user_name = User_name.objects.get(id=practice.user_name.id)
        if user_name.owner.id == request.user.id:
            practice.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def criminal_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateCriminalForm(request.POST)
            if form.is_valid():
                criminal_record = form.data.get('criminal_record')
                criminal = Criminal(criminal_record=criminal_record, id=user_name.id, user_name=user_name)
                criminal.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_criminal(request, pk):
    if request.user.is_authenticated:
        criminal = Criminal.objects.get(id=pk)
        user_name = User_name.objects.get(id=criminal.user_name.id)
        if user_name.owner.id == request.user.id:
            criminal.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def medicine_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateMedicineForm(request.POST)
            if form.is_valid():
                medicine_number = form.data.get('medicine_number')
                medicine_date = form.data.get('medicine_date')
                medicine = Medicine(medicine_number=medicine_number, medicine_date=medicine_date, id=user_name.id, user_name=user_name)
                medicine.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')

def delete_medicine(request, pk):
    if request.user.is_authenticated:
        medicine = Medicine.objects.get(id=pk)
        user_name = User_name.objects.get(id=medicine.user_name.id)
        if user_name.owner.id == request.user.id:
            medicine.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')

def master_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateMasterForm(request.POST)
            if form.is_valid():
                master_degree = form.data.get('master_degree')
                master = Master(master_degree=master_degree, id=user_name.id, user_name=user_name)
                master.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_master(request, pk):
    if request.user.is_authenticated:
        master = Master.objects.get(id=pk)
        user_name = User_name.objects.get(id=master.user_name.id)
        if user_name.owner.id == request.user.id:
            master.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def doctor_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateDoctorForm(request.POST)
            if form.is_valid():
                doctor_profile = form.data.get('doctor_profile')
                doctor = Doctor(doctor_profile=doctor_profile, id=user_name.id, user_name=user_name)
                doctor.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_doctor(request, pk):
    if request.user.is_authenticated:
        doctor = Doctor.objects.get(id=pk)
        user_name = User_name.objects.get(id=doctor.user_name.id)
        if user_name.owner.id == request.user.id:
            doctor.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def phd_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreatePhdForm(request.POST)
            if form.is_valid():
                phd_record = form.data.get('phd_record')
                phd = Phd(phd_record=phd_record, id=user_name.id, user_name=user_name)
                phd.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_phd(request, pk):
    if request.user.is_authenticated:
        phd = Phd.objects.get(id=pk)
        user_name = User_name.objects.get(id=phd.user_name.id)
        if user_name.owner.id == request.user.id:
            phd.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    

def professor_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateProfessorForm(request.POST)
            if form.is_valid():
                docent_professor = form.data.get('docent_professor')
                professor = Professor(docent_professor=docent_professor, id=user_name.id, user_name=user_name)
                professor.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_professor(request, pk):
    if request.user.is_authenticated:
        professor = Professor.objects.get(id=pk)
        user_name = User_name.objects.get(id=professor.user_name.id)
        if user_name.owner.id == request.user.id:
            professor.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')

def sport_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateSportForm(request.POST)
            if form.is_valid():
                sport_degree = form.data.get('sport_degree')
                sport = Sport(sport_degree=sport_degree, id=user_name.id, user_name=user_name)
                sport.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_sport(request, pk):
    if request.user.is_authenticated:
        sport = Sport.objects.get(id=pk)
        user_name = User_name.objects.get(id=sport.user_name.id)
        if user_name.owner.id == request.user.id:
            sport.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def subject_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateSubjectForm(request.POST)
            if form.is_valid():
                subject_of_teaching = form.data.get('subject_of_teaching')
                subject = Subject(subject_of_teaching=subject_of_teaching, id=user_name.id, user_name=user_name)
                subject.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_subject(request, pk):
    if request.user.is_authenticated:
        subject = Subject.objects.get(id=pk)
        user_name = User_name.objects.get(id=subject.user_name.id)
        if user_name.owner.id == request.user.id:
            subject.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def all_page(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            users = User.objects.all()
            user_names = User_name.objects.all()
            user_births = User_birth.objects.select_related('user_name').all()
            User_infos = User_info.objects.select_related('user_name').all()
            Practices = Practice.objects.select_related('user_name').all()
            Criminals = Criminal.objects.select_related('user_name').all()
            Medicines = Medicine.objects.select_related('user_name').all()
            Masters = Master.objects.select_related('user_name').all()
            Doctors = Doctor.objects.select_related('user_name').all()
            Phds = Phd.objects.select_related('user_name').all()
            Professors = Professor.objects.select_related('user_name').all()
            Sports = Sport.objects.select_related('user_name').all()
            Subjects = Subject.objects.select_related('user_name').all()
            User_works = User_work.objects.select_related('user_name').all()

            return render(request, 'info1/all.html', {'user_names': user_names, 'users': users, 'user_births':user_births, 'User_infos':User_infos, 'Practices':Practices,'Criminals': Criminals, 'Medicines': Medicines, 'Masters':Masters, 'Doctors':Doctors, 'Phds':Phds, 'Professors':Professors, 'Sports':Sports,'Subjects':Subjects, 'User_works':User_works})
    else:
        return redirect('/auth/login/')
    


    
