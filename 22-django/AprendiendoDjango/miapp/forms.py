from django import forms

class formArticulo(forms.Form):

    title = forms.CharField(
        label = "Titulo",
        max_length=200,
        required=True
    )

    content = forms.CharField(
        label = "Content",
        widget=forms.Textarea,
        required=True
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "Publicado?",
        choices = public_options,
        required=True
                
    )

class formCategory(forms.Form):

    name = forms.CharField(
        label = "Nombre",
        max_length=150,
        required=True
    )

    description = forms.CharField(
        label="Descripcion",
        max_length=250,
        required=True
    )

class formSubCate(forms.Form):

    name = forms.CharField(
        label = "Nombre",
        max_length=250,
        required=True
    )

    description = forms.CharField(
        label = "description",
        max_length=200,
        required=True
    )        