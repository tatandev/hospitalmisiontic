from django.contrib import admin
from .models.paciente import Paciente
from .models.familiar import Familiar
from .models.enfermero import Enfermero
from .models.medico import Medico
from .models.user import User
from .models.auxiliar import Auxiliar
from .models.sugerencias import Sugerencias
from .models.diagnosticos import Diagnostico
from .models.signos_vitales import Signos_vitales

admin.site.register(User)
admin.site.register(Familiar)
admin.site.register(Enfermero)
admin.site.register(Medico)
admin.site.register(Auxiliar)
admin.site.register(Sugerencias)
admin.site.register(Diagnostico)
admin.site.register(Signos_vitales)
admin.site.register(Paciente)