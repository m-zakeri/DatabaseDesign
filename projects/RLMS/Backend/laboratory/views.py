from django.shortcuts import render
from .models import *

# Create your views here.


def dashboard(request):
    context = {"segment": "dashboard"}
    username = request.user.username
    if Person.objects.filter(user__username=username):
        person = Person.objects.filter(user__username=username)[0].id
        researchs = Research.objects.filter(person_id__id=person).values()
        researchs_team = []
        for research in researchs:
            data = Research.objects.filter(research_code=research["research_code"])
            team = dict()
            team["research"] =research
            team_member = []
            # researchs_team.append(data)
            for i in data:
                member = dict()
                if i.person_id.id != person:
                    name = str(i.person_id)
                    # print("____", name, i.person_id.id)

                    role = "None"
                    student = Student.objects.filter(person_id__id=i.person_id.id)
                    supervisor = Supervisor.objects.filter(person_id__id=i.person_id.id)
                    if supervisor and student:
                        role = "supervisor & student"
                    elif supervisor:
                        role = "supervisor"
                    elif student:
                        role = "student"
                    # print(name, role)
                    member["name"] = name
                    member["role"] = role
                    team_member.append(member)
            team["member"] = team_member
            researchs_team.append(team)
        # print("\n\n\n\n\n\n\n\n\n________", username, *researchs_team, sep="\n")
        context["Researchs"] = researchs
        context["researchs_team"] = researchs_team
        # print("----------------", context["researchs_team"])
    return render(request, "pages/dashboard/dashboard.html", context)


#
# username = "ghazal1"
# data = Person.objects.values()
# print(data)
#
# username = "ghazal"
# data = Person.objects.filter(user__username="ghazal")
# print(data)
# person = Person.objects.filter(user__username="vahid")[0].id
# print(person)
# data = Research.objects.filter(person_id__id=person)
# print(data.values())
# data = Research.objects.filter(research_code="2345")
# team = []
# for i in data:
#     member = dict()
#     if i.person_id.id != person:
#         name = str(i.person_id)
#         # print("____", name, i.person_id.id)
#
#         role = "None"
#         student = Student.objects.filter(person_id__id=i.person_id.id)
#         supervisor = Supervisor.objects.filter(person_id__id=i.person_id.id)
#         if supervisor and student:
#             role = "supervisor & student"
#         elif supervisor:
#             role = "supervisor"
#         elif student:
#             role = "student"
#         print(name, role)
#         member["name"] = name
#         member["role"] = role
#         team.append(member)
#
#
# print(team)
# print(data)