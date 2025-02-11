# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Afp(models.Model):
    id_afp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'afp'


class Bancos(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bancos'


class CajaCompensacion(models.Model):
    id_cajacompensacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'caja_compensacion'


class CargaFamiliar(models.Model):
    id_carga_familiar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')

    class Meta:
        managed = False
        db_table = 'carga_familiar'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombrecomuna = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'comuna'


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    tipo_contrato = models.SmallIntegerField()
    sucursal = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    jornada = models.CharField(max_length=100)
    renta_imponible = models.IntegerField()
    meses_cotizados = models.IntegerField()
    tiene_cargas = models.BooleanField()
    horas_jornada_mensual = models.IntegerField()
    colacion = models.DecimalField(max_digits=10, decimal_places=2)
    movilizacion = models.DecimalField(max_digits=10, decimal_places=2)
    antiguedad = models.IntegerField()
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')
    id_tramo_asignacion_familiar = models.ForeignKey('TramoAsignacionFamiliar', models.DO_NOTHING, db_column='id_tramo_asignacion_familiar')

    class Meta:
        managed = False
        db_table = 'contrato'


class DuenoEmpresa(models.Model):
    id_dueno_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')
    id_genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='id_genero')
    id_estadocivil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='id_estadocivil')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'dueno_empresa'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    razon_social = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    estado_social_trabajador = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    codigo_postal = models.CharField(max_length=45)
    estado_empresa = models.SmallIntegerField()
    factor_mutual = models.FloatField()
    fecha_creacion = models.DateField()
    id_cajacompensacion = models.ForeignKey(CajaCompensacion, models.DO_NOTHING, db_column='id_cajacompensacion')
    id_mutual = models.ForeignKey('Mutual', models.DO_NOTHING, db_column='id_mutual')
    id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pais')
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_giro = models.ForeignKey('Giro', models.DO_NOTHING, db_column='id_giro')

    class Meta:
        managed = False
        db_table = 'empresa'


class EstadoCivil(models.Model):
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'estado_civil'


class FechasContrato(models.Model):
    id_fechas_contrato = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato')

    class Meta:
        managed = False
        db_table = 'fechas_contrato'


class Finiquito(models.Model):
    id_finiquito = models.AutoField(primary_key=True)
    fecha_finiquito = models.DateField()
    monto_total = models.IntegerField()
    finiquito_url = models.CharField(max_length=250)
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')
    id_finiquito_causa = models.ForeignKey('FiniquitoCausa', models.DO_NOTHING, db_column='id_finiquito_causa')

    class Meta:
        managed = False
        db_table = 'finiquito'


class FiniquitoCausa(models.Model):
    id_finiquito_causa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'finiquito_causa'


class Firmadigital(models.Model):
    id_configuracion = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    firma_rut = models.CharField(max_length=12)
    firma_nombre = models.CharField(max_length=100)
    firma_email = models.CharField(max_length=100)
    fecha_firma = models.DateField()

    class Meta:
        managed = False
        db_table = 'firmadigital'


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'genero'


class Giro(models.Model):
    id_giro = models.AutoField(primary_key=True)
    codigo_sii = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'giro'


class HorasExtra(models.Model):
    id_horas_extra = models.AutoField(primary_key=True)
    horas = models.IntegerField()
    fecha = models.DateField()
    porcentaje = models.IntegerField()
    id_horas_extra_tipo = models.ForeignKey('HorasExtraTipo', models.DO_NOTHING, db_column='id_horas_extra_tipo')
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')

    class Meta:
        managed = False
        db_table = 'horas_extra'


class HorasExtraTipo(models.Model):
    id_horas_extra_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'horas_extra_tipo'


class Ips(models.Model):
    id_ips = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ips'


class Isapre(models.Model):
    id_isapre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'isapre'


class LicenciaTipo(models.Model):
    id_licencia_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'licencia_tipo'


class Licencias(models.Model):
    id_licencia = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    tipo_licencia = models.ForeignKey(LicenciaTipo, models.DO_NOTHING, db_column='tipo_licencia')
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')

    class Meta:
        managed = False
        db_table = 'licencias'


class Mutual(models.Model):
    id_mutual = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'mutual'


class PagoContratos(models.Model):
    id_pago_contrato = models.AutoField(primary_key=True)
    cuenta = models.CharField(max_length=45)
    id_pago_modo = models.ForeignKey('PagoModo', models.DO_NOTHING, db_column='id_pago_modo')
    id_pago_tipo = models.ForeignKey('PagoTipo', models.DO_NOTHING, db_column='id_pago_tipo')
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato')
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    class Meta:
        managed = False
        db_table = 'pago_contratos'


class PagoModo(models.Model):
    id_pago_modo = models.AutoField(primary_key=True)
    modo_pago = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pago_modo'


class PagoTipo(models.Model):
    id_pago_tipo = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pago_tipo'


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pais'


class Prevision(models.Model):
    id_prevision = models.AutoField(primary_key=True)
    apv = models.IntegerField()
    sistema_previsional = models.SmallIntegerField()
    sis = models.SmallIntegerField()
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')
    id_afp = models.ForeignKey(Afp, models.DO_NOTHING, db_column='id_afp')
    id_isapre = models.ForeignKey(Isapre, models.DO_NOTHING, db_column='id_isapre')
    id_ips = models.ForeignKey(Ips, models.DO_NOTHING, db_column='id_ips')
    id_sistema_salud = models.ForeignKey('SistemaSalud', models.DO_NOTHING, db_column='id_sistema_salud')

    class Meta:
        managed = False
        db_table = 'prevision'


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'region'


class SistemaSalud(models.Model):
    id_sistema_salud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'sistema_salud'


class Trabajador(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=100)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    discapacidad = models.SmallIntegerField()
    foto_url = models.CharField(max_length=250)
    id_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_estado_civil')
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pais')
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'trabajador'


class TramoAsignacionFamiliar(models.Model):
    id_tramo_asignacion_familiar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tramo_asignacion_familiar'


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre_user = models.CharField(max_length=100)
    contrasena_hashed = models.TextField()
    correo = models.CharField(max_length=45)
    fecha_creacion = models.DateField()
    estado = models.SmallIntegerField()
    id_tipo_user = models.ForeignKey('UserTipo', models.DO_NOTHING, db_column='id_tipo_user')

    class Meta:
        managed = False
        db_table = 'user'


class UserTipo(models.Model):
    id_user_tipo = models.AutoField(primary_key=True)
    nombre_user_tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_tipo'


class Vacaciones(models.Model):
    id_vacaciones = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    dias_totales = models.IntegerField()
    dias_tomados = models.IntegerField()
    dias_disponibles = models.IntegerField()
    id_trabajador = models.ForeignKey(Trabajador, models.DO_NOTHING, db_column='id_trabajador')

    class Meta:
        managed = False
        db_table = 'vacaciones'
