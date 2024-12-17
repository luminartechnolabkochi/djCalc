from django.shortcuts import render

from django.views.generic import View

from operation.forms import ResgisterationForm,BmiForm,MilageForm,CalorieForm
# Create your views here.


# url:localhost:8000/addition/
# method:get,post


class AdditionView(View):


    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")#"10"

        num2=form_data.get("num2")#"20"

        result=int(num1)+int(num2)

        print(result)

        data={
            "output":result
        }

        return render(request,"add.html",data)

# django forms



class SubtractionView(View):


    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")#"10"

        num2=form_data.get("num2")#"20"

        result=int(num1)+int(num2)

        print(result)

        data={
            "output":result
        }

        return render(request,"add.html",data)



class SignUpView(View):


    def get(self,request,*args,**kwargs):

        form_instance=ResgisterationForm()

        context={
            "form":form_instance
        }



        return render(request,"register.html",context)
    


class BmiView(View):


    def get(self,request,*args,**kwargs):

        form_instance=BmiForm()

        context={
            "form":form_instance
        }
       
        return render(request,"bmi.html",context)
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BmiForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data #{"height":165,"weight":68}

            height=data.get("height")

            weight=data.get("weight")

            BMI=weight/(height/100)**2

            print(BMI)

        return render(request,"bmi.html",{"form":form_instance,"result":BMI})



       
class MilageView(View):


    def get(self,request,*args,**kwargs):


        form_instance=MilageForm()

        context={
            "form":form_instance
        }

        return render(request,"milage.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=MilageForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            distance=data.get("distance")

            consumption=data.get("consumption")

            milage=distance/consumption

        return  render(request,"milage.html",{"form":form_instance,"result":milage})



class CalorieView(View):

    def get(self,request,*args,**kwargs):

        form_instance=CalorieForm()

        context={
            "form":form_instance
        }

        return render(request,"calorie.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=CalorieForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            print(data)#{'weight': 65, 'height': 165, 'age': 32, 'gender': 'male', 'activity': '1.2'}
            """
            The Basal Metabolic Rate (BMR)=

                10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for (man)

                10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) - 161 for ​(woman)

                To determin​e your total daily calorie needs, multiply your BMR by the appropriate activity factor, as follows:
            """
            weight=data.get("weight")

            height=data.get("height")

            age=data.get("age")

            gender=data.get("gender")

            activity=data.get("activity")

            if gender=="male":

                BMR=10*weight+6.25*height-5*age+5
            else:
                BMR=10*weight+6.25*height-5*age-161

            calorie=BMR*float(activity)

        return render(request,"calorie.html",{"form":form_instance,"bmr":BMR,"calorie":calorie})




