from django import forms
from .models import Problem, Solution, Comment

class ProblemForm(forms.ModelForm):
    LEVEL = [
        ('브론즈', '브론즈'), 
        ('실버', '실버'),
        ('골드', '골드'), 
        ('플레티넘', '플레티넘')
        ]

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '제목',

                }
            ),
        )
    problem_url = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'url',

                }
            ),
        )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '내용',

                }
            ),
        )
    input = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '입력',

                }
            ),
        ) 
    output = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '출력',

                }
            ),
        )     
    constraint = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '제한사항',

                }
            ),
        )     
 
    level = forms.CharField(
        widget=forms.Select(
            attrs={
                'class': 'form-control'
                },
            choices=LEVEL,
            ),
        )  

    type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '타입',
                
                }
            ),
        )   
    class Meta:
        model = Problem
        exclude = ('user', 'like_users',)




class SolutionForm(forms.ModelForm):
    hint = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '힌트',
                
                }
            ),
        )  
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '코드',
                
                }
            ),
        )  
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '설명',
                
                }
            ),
        )  
    class Meta:
        model = Solution
        exclude = ('problem', 'user', 'like_users',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('solution', 'user', 'like_users',)