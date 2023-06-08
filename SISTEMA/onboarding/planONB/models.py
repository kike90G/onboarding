# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ontactitud(models.Model):
    actitudid = models.AutoField(db_column='actitudId', primary_key=True)  # Field name made lowercase.
    will = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ONTActitud'
        verbose_name = ('Actitud')
        verbose_name_plural = ('Actitud')

    def __str__(self):
        return self.descripcion


class Ontactividad(models.Model):
    actividadid = models.AutoField(db_column='actividadId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    habilidadid = models.ForeignKey('Onthabilidad', models.DO_NOTHING, db_column='habilidadId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTActividad'
        verbose_name = ('Actividad')
        verbose_name_plural = ('Actividad')


class Ontasignacion(models.Model):
    asignacionid = models.AutoField(db_column='asignacionId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    departamentoid = models.ForeignKey('Ontdepartamento', models.DO_NOTHING, db_column='departamentoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTAsignacion'
        verbose_name = ('Asignacion')
        verbose_name_plural = ('Asignacion')


class Ontcumple(models.Model):
    cumpleid = models.AutoField(db_column='cumpleId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    porcentaje = models.IntegerField(blank=True, null=True)
    tipoid = models.ForeignKey('Onttipo', models.DO_NOTHING, db_column='tipoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTCumple'
        verbose_name = ('Cumple')
        verbose_name_plural = ('Cumple')


class Ontcumpleactitud(models.Model):
    cumpleid = models.IntegerField(db_column='cumpleId', blank=True, null=True)  # Field name made lowercase.
    evaluacionid = models.IntegerField(db_column='evaluacionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTCumpleActitud'
        verbose_name = ('Cumple Actitud')
        verbose_name_plural = ('Cumple Actitud')


class Ontcumpleactividad(models.Model):
    cumpleid = models.IntegerField(db_column='cumpleId', blank=True, null=True)  # Field name made lowercase.
    evaluacionid = models.IntegerField(db_column='evaluacionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTCumpleActividad'
        verbose_name = ('Cumple Actividad')
        verbose_name_plural = ('Cumple Actividad')


class Ontdepartamento(models.Model):
    departamentoid = models.AutoField(db_column='departamentoId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ONTDepartamento'
        verbose_name = ('Departamento')
        verbose_name_plural = ('Departamento')


class Ontempleado(models.Model):
    empleadoid = models.AutoField(db_column='empleadoId', primary_key=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='primerNombre', max_length=100)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='primerApellido', max_length=100)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='segundoApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statusid = models.ForeignKey('Ontstatusempleado', models.DO_NOTHING, db_column='statusId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTEmpleado'
        verbose_name = ('Empleado')
        verbose_name_plural = ('Empleado')


class Onthabilidad(models.Model):
    habilidadid = models.AutoField(db_column='habilidadId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ONTHabilidad'
        verbose_name = ('Habilidad')
        verbose_name_plural = ('Habilidad')


class Ontnivel(models.Model):
    nivelid = models.AutoField(db_column='nivelId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ONTNivel'
        verbose_name = ('Nivel')
        verbose_name_plural = ('Nivel')


class Ontplan(models.Model):
    planid = models.AutoField(db_column='planId', primary_key=True)  # Field name made lowercase.
    empleadoid = models.ForeignKey(Ontempleado, models.DO_NOTHING, db_column='empleadoId')  # Field name made lowercase.
    puestoid = models.ForeignKey('Ontpuesto', models.DO_NOTHING, db_column='puestoId')  # Field name made lowercase.
    tipoevaluacion = models.IntegerField(db_column='tipoEvaluacion')  # Field name made lowercase.
    resultado = models.IntegerField()
    numevaluacion = models.IntegerField(db_column='numEvaluacion')  # Field name made lowercase.
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'ONTPlan'
        verbose_name = ('Plan')
        verbose_name_plural = ('Plan')


class Ontplanactitud(models.Model):
    planid = models.IntegerField(db_column='planId', blank=True, null=True)  # Field name made lowercase.
    actitudid = models.IntegerField(db_column='actitudId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTPlanActitud'
        verbose_name = ('Plan Actitud')
        verbose_name_plural = ('Plan Actitud')


class Ontplanactividad(models.Model):
    plantid = models.IntegerField(db_column='plantId', blank=True, null=True)  # Field name made lowercase.
    actividadid = models.IntegerField(db_column='actividadId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTPlanActividad'
        verbose_name = ('Plan Actividad')
        verbose_name_plural = ('Plan Actividad')


class Ontpuesto(models.Model):
    puestoid = models.AutoField(db_column='puestoId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    statusid = models.ForeignKey('Ontstatuspuesto', models.DO_NOTHING, db_column='statusId')  # Field name made lowercase.
    asignacionid = models.ForeignKey(Ontasignacion, models.DO_NOTHING, db_column='asignacionId')  # Field name made lowercase.
    nivelid = models.ForeignKey(Ontnivel, models.DO_NOTHING, db_column='nivelId')  # Field name made lowercase.
    actitudid = models.IntegerField(db_column='actitudId')  # Field name made lowercase.
    habilidadid = models.IntegerField(db_column='habilidadId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONTPuesto'
        verbose_name = ('Puesto')
        verbose_name_plural = ('Puesto')

class Ontstatusempleado(models.Model):
    statusid = models.AutoField(db_column='statusId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ONTStatusEmpleado'
        verbose_name = ('Status Empleado')
        verbose_name_plural = ('Status Empleado')


class Ontstatuspuesto(models.Model):
    statusid = models.AutoField(db_column='statusId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ONTStatusPuesto'
        verbose_name = ('Status puesto')
        verbose_name_plural = ('Status puesto')


class Onttipo(models.Model):
    tipoid = models.AutoField(db_column='tipoId', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ONTTipo'
        verbose_name = ('Tipo')
        verbose_name_plural = ('Tipo')

    def __str__(self):
        return self.descripcion
    

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
