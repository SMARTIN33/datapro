# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achat(models.Model):
    id_achat = models.IntegerField(primary_key=True)
    nombre_enfant_client = models.IntegerField(blank=True, null=True)
    id_csp = models.IntegerField(blank=True, null=True)
    id_collecte = models.IntegerField(blank=True, null=True)
    total_achat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Achat'


class Csp(models.Model):
    id_categorie = models.IntegerField(primary_key=True)
    nom_categorie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CSP'


class Client(models.Model):
    id_numero_client = models.IntegerField()
    prenom_client = models.CharField(max_length=255, blank=True, null=True)
    nom_client = models.CharField(max_length=255, blank=True, null=True)
    mail_client = models.CharField(max_length=255, blank=True, null=True)
    date_achat_client = models.DateTimeField(primary_key=True)
    nombre_enfant_client = models.IntegerField(blank=True, null=True)
    id_categorie = models.IntegerField(blank=True, null=True)
    id_collecte = models.CharField(max_length=255, blank=True, null=True)
    id_numero_magasin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Client'


class Collecte(models.Model):
    id_collecte = models.IntegerField(primary_key=True)
    date_achat_client = models.DateTimeField(blank=True, null=True)
    id_numero_magasin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Collecte'


class CollecteProduit(models.Model):
    id_collecte = models.IntegerField(primary_key=True)  # The composite primary key (id_collecte, id_produit, quantite_produit, prix_unitaire_produit) found, that is not supported. The first column is selected.
    id_produit = models.IntegerField()
    quantite_produit = models.IntegerField()
    prix_unitaire_produit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Collecte_produit'
        unique_together = (('id_collecte', 'id_produit', 'quantite_produit', 'prix_unitaire_produit'),)


class DroitUtilisateur(models.Model):
    id_droit_utilisateur = models.IntegerField(primary_key=True)
    role_utilisateur = models.CharField(max_length=255, blank=True, null=True)
    groupe_utilisateur = models.IntegerField(blank=True, null=True)
    description_utilisateur = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Droit_utilisateur'


class Magasin(models.Model):
    id_numero_magasin = models.IntegerField(primary_key=True)
    nom_magasin = models.CharField(max_length=255, blank=True, null=True)
    ville_magasin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Magasin'


class Produit(models.Model):
    id_produit = models.IntegerField(primary_key=True)
    nom_produit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Produit'


class Service(models.Model):
    id_numero_service = models.IntegerField(primary_key=True)
    nom_service = models.CharField(max_length=255, blank=True, null=True)
    type_salarie = models.CharField(max_length=255, blank=True, null=True)
    id_droit_utilisateur = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service'


class Utilisateur(models.Model):
    id_numero_utilisateur = models.IntegerField(primary_key=True)
    mail_utilisateur = models.CharField(max_length=255, blank=True, null=True)
    prenom_utilisateur = models.CharField(max_length=255, blank=True, null=True)
    nom_utilisateur = models.CharField(max_length=255, blank=True, null=True)
    mot_passe_utilisateur = models.CharField(max_length=255, blank=True, null=True)
    type_utilisateur = models.CharField(max_length=255, blank=True, null=True)
    role_utilisateur = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Utilisateur'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    action_flag = models.SmallIntegerField()
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