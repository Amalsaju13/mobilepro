from django.shortcuts import render,redirect
from owner.forms import MobileForm
from django.views.generic import View
from owner.models import Mobile


# Create your views here.

class AddMobile(View):
    def get(self,request):
        form=MobileForm()
        return render(request,"add_mobile.html",{"form":form})
    def post(self,request):
        form=MobileForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data.get('mobile_name'))
            # print(form.cleaned_data.get('brand'))
            # print(form.cleaned_data.get('price'))
            # print(form.cleaned_data.get('quantity'))
            # print(form.cleaned_data.get('color'))
            # print(form.cleaned_data.get('specification'))
            # print(form.cleaned_data.get('camera'))
            # print(form.cleaned_data.get('ram'))
            # print(form.cleaned_data.get('storage'))
            #
            # qs=Mobile(
            #     mobile_name=form.cleaned_data.get('mobile_name'),
            #     brand=form.cleaned_data.get('brand'),
            #     price=form.cleaned_data.get('price'),
            #     quantity=form.cleaned_data.get('quantity'),
            #     color=form.cleaned_data.get('color'),
            #     specification=form.cleaned_data.get('specification'),
            #     camera=form.cleaned_data.get('camera'),
            #     ram=form.cleaned_data.get('ram'),
            #     storage=form.cleaned_data.get('storage')
            #
            # )
            # qs.save()


            # return render(request,'add_mobile.html',{'msg':'mobile created'})
            return redirect('listmobile')
        else:
            return render(request, "add_mobile.html", {'form': form})

class MobileList(View):
    def get(self,request):
        qs=Mobile.objects.all()
        return render(request,'mobile_html.html',{'mobile':qs})

class MobileDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobile.objects.get(id=kwargs.get("id"))
        return render(request,'mobile_detail.html',{'mobile':qs})

class MobileDeleteView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobile.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("listmobile")

class ChangeMobile(View):
    def get(self,request,*args,**kwargs):
        qs=Mobile.objects.get(id=kwargs.get("id"))
        form=MobileForm(instance=qs)
        return render(request,"mobile_edit.html",{"form":form})

    def post(self,request,*args,**kwargs):
        qs=Mobile.objects.get(id=kwargs.get("id"))
        form=MobileForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
