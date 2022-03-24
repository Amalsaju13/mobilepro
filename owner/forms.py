from django import forms
from owner.models import Mobile


# class MobileForm(forms.Form):
#     mobile_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     brand=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     quantity=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     color=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     specification=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     camera=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     ram=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     storage=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data.get("price")
#         quantity=cleaned_data.get("quantity")
#         if price<0:
#             msg="invalid price"
#             self.add_error("price",msg)
#         if quantity<0:
#             msg="invalid quantity"
#             self.add_error("quantity",msg)

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={'class':'form-control'}),
            "brand":forms.TextInput(attrs={'class':'form-control'}),
            "price":forms.NumberInput(attrs={'class':'form-control'}),
            "quantity": forms.NumberInput(attrs={'class': 'form-control'}),
            "color": forms.TextInput(attrs={'class': 'form-control'}),
            "specification": forms.TextInput(attrs={'class': 'form-control'}),
            "camera": forms.TextInput(attrs={'class': 'form-control'}),
            "ram": forms.TextInput(attrs={'class': 'form-control'}),
            "storage": forms.TextInput(attrs={'class': 'form-control'}),
            "image":forms.FileInput(attrs={"class":'form-control'})

        }
