from django import forms
from django.core import validators

class formArticulo(forms.Form):

    title = forms.CharField(
        label = "Titulo",
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete el titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El Titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$','El titulo esta mal formado', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Content",
        required = True,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Mete el contenido',
                'class':'content_form_article',
                'id':'content_form'
            }
        ),
        validators=[
            validators.MinLengthValidator(3, 'El contenido es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$','El contenido esta mal formado', 'invalid_content')
        ]
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
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete el nombre',
                'class':'content_form_category'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El nombre de categoria es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$','El nombre de categoria esta mal formado','invalid_name_category')
        ]
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
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete el name',
                'class':'name_form_subcate'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El nombre de la SubCategoria es damasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$','el nombre de la subcategoria esta mal formado','invalid_name_subcateg')
        ]
    )

    description = forms.CharField(
        label = "description",
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete la description',
                'class':'descrip_form_subcate'
            }
        )
    )


pais_options = [
        ('Afganistan','Afganistan'),
        ('Argelia','Argelia'),
        ('Andorra','Andorra'),
        ('Angilla','Angilla'),
        ('Antartida','Antartida'),
        ('Antigua y Barbuda','Antigua y Barbuda'),
        ('Argentina','Argentina'),
        ('Armenia','Armenia'),
        ('Aruba','Aruba'),
        ('Australia','Australia'),
        ('Austria','Austria'),
        ('Azerbaiyan','Azerbaiyan'),
        ('Bahamas','Bahamas'),
        ('Bahrein','Bahrein'),
        ('Bangladesh','Bangladesh'),
        ('Barbados','Barbados'),
        ('Belgica','Belgica'),
        ('Belice','Belice'),
        ('Benin','Benin'),
        ('Bermudas','Bermudas'),
        ('Butan','Butan'),
        ('Bolivia','Bolivia'),
        ('Bosnia-Herzegovina','Bosnia-Herzegovina'),
        ('Botsuana','Botsuana'),
        ('Brasil','Brasil'),
        ('Brunei Darussalam','Brunei Darussalam'),
        ('Bulgania','Bulgaria'),
        ('Burkina Faso','Burkina Faso'),
        ('Burundi','Burundi'),
        ('Camboya','Camboya'),
        ('Camerún','Camerún'),
        ('Canadá','Canadá'),
        ('Cabo Verde','Cabo Verde'),
        ('Islas Caimán','Islas Caimán'),
        ('República Centroafricana','República Centroafricana'),
        ('Chad','Chad'),
        ('Chile','Chile'),
        ('China','China'),
        ('Isla Navidad','Isla de Navidad'),
        ('Islas Cocos','Islas Cocos'),
        ('Colobia','Colombia'),
        ('Comores','Comores'),
        ('República Democrática del Congo','República Democrática del Congo'),
        ('República del Congo','República del Congo'),
        ('Islas Cook','Islas Cook'),
        ('Costa Rica','Costa Rica'),
        ('Costa de Marfil','Costa de Marfil'),
        ('Croacia','Croacia'),
        ('Cuba','Cuba'),
        ('Chipre','Chipre'),
        ('Republica Checa','Republica Checa'),
        ('Dinamarca','Dinamarca'),
        ('Djibouti','Djibouti'),
        ('Dominicana, República','Dominicana, República'),
        ('Timor Oriental','Timor Oriental'),
        ('Ecuador','Ecuador'),
        ('Egipto','Egipto'),
        ('El Salvador','El Salvador'),
        ('Guinea Ecuatorial','Guinea Ecuatorial'),
        ('Eritrea','Eritrea'),
        ('Estonia','Estonia'),
        ('Etiopia','Etiopia'),
        ('Islas Malvinas','Islas Malvinas'),
        ('Islas Feroe','Islas Feroe'),
        ('Fiyi','Fiyi'),
        ('Finlandia','Finlandia'),
        ('Francia','Francia'),
        ('Guyana Francesa','Guyana Francesa'),
        ('Polinesia Francesa','Polinesia Francesa'),
        ('Tierras Australes y Fran','Tierras Australes y Fran'),
        ('Gabón','Gabón'),
        ('Gambia','Gambia'),
        ('Georgia','Georgia'),
        ('Alemania','Alemania'),
        ('Ghana','Ghana'),
        ('Gibraltar','Gibraltar'),
        ('Grecia','Grecia'),
        ('Groenlandia','Groenlandia'),
        ('Granada','Granada'),
        ('Guadalupe','Guadalupe'),
        ('Guam','Guam'),
        ('Guadalupe','Guatemala'),
        ('República Guinea','República Guinea'),
        ('Guinea Bissau','Guinea Bissau'),
        ('Guayana','Guyana'),
        ('Haiti','Haiti'),
        ('Honduras','Honduras'),
        ('Hong Kong','Hong Kong'),
        ('Hungría','Hungría'),
        ('Islandia','Islandia'),
        ('India','India'),
        ('Infonesia','Indonesia'),
        ('Irán','Irán'),
        ('Iraq','Iraq'),
        ('Irlanda','Irlanda'),
        ('Israel','Israel'),
        ('Italia','Italia'),
        ('Jamaica','Jamaica'),
        ('Japón','Japón'),
        ('Jordania','Jordania'),
        ('Kazajstán','Kazajstán'),
        ('Kenia','Kenia'),
        ('Kiribati','Kiribati'),
        ('Corea del Norte','Corea del Norte'),
        ('Corea del Sur','Corea del Sur'),
        ('Kosovo','Kosovo'),
        ('Kuwait','Kuwait'),
        ('Kirguistán','Kirguistán'),
        ('Laos','Laos'),
        ('Letonia','Letonia'),
        ('Líbano','Líbano'),
        ('Lesotho','Lesotho'),
        ('Liberia','Liberia'),
        ('Libia','Libia'),
        ('Liechtenstein','Liechtenstein'),
        ('Lituania','Lituania'),
        ('Luxemburgo','Luxemburgo')
    ]



class formPersona(forms.Form):

    apellidos = forms.CharField(
        label = "Apellidos",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete los apellidos',
                'class':'apellidos_form_persona'
            }
        )
    )

    nombres = forms.CharField(
        label = "Nombres",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete los nombres',
                'class':'nombres_form_persona'
            }
        )
    )

    pais = forms.TypedChoiceField(
        label = "Pais",
        choices = pais_options,
        required = True
    )

    provincia = forms.CharField(
        label = "Provincia",
        max_length = 60,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholher':'Mete la provincia',
                'class':'provincia_form_persona'
            }
        )
    )

    direccion = forms.CharField(
        label = "Direccion",
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete la direccion',
                'class':'direccion_form_persona'
            }
        )
    )

    correo = forms.EmailField(
         label = "Correo electronico",
         max_length=150,
         widget= forms.EmailInput(
             attrs={
                 'placeholder':'Mete el correo electronico',
                 'class':'correo_form_persona'
             }
         )
    )
    

    telefono = forms.CharField(
        label = "Telefono",
        widget = forms.TextInput(
            attrs={
                'placeholder':'Mete el telefono',
                'class':'telefono_form_persona'
            }
        )
    )

    profesion = forms.CharField(
        label = "Profesion",
        max_length=250,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete tu titulo profesional',
                'class':'profesion_class_persona'
            }
        )
    )

    certificado = forms.CharField(
        label = "Certificado",
        widget = forms.TextInput(
            attrs={
                'placeholder':'Mete tu certificado',
                'class':'certificado_class_persona'
            }
        )
    )

