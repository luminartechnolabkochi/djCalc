from django.shortcuts import render

from django.views.generic import View

from operation.forms import ResgisterationForm,BmiForm
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



       
   


