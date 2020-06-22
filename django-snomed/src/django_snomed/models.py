# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssociationrefsetF(models.Model):
    _id = models.UUIDField()
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    refsetid = models.CharField(max_length=18)
    referencedcomponentid = models.CharField(max_length=18)
    targetcomponentid = models.CharField(max_length=18)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        #managed = False
        #db_table = 'associationrefset_f'
        unique_together = (('_id', 'effectivetime'),)


class AttributevaluerefsetF(models.Model):
    _id = models.UUIDField()
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    refsetid = models.CharField(max_length=18)
    referencedcomponentid = models.CharField(max_length=18)
    valueid = models.CharField(max_length=18)


    class Meta:
        #managed = False
        #db_table = 'attributevaluerefset_f'
        unique_together = (('_id', 'effectivetime'),)


class ComplexmaprefsetF(models.Model):
    _id = models.UUIDField()
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    refsetid = models.CharField(max_length=18)
    referencedcomponentid = models.CharField(max_length=18)
    mapgroup = models.SmallIntegerField()
    mappriority = models.SmallIntegerField()
    maprule = models.TextField(blank=True, null=True)
    mapadvice = models.TextField(blank=True, null=True)
    maptarget = models.TextField(blank=True, null=True)
    correlationid = models.CharField(max_length=18)

    class Meta:
        #managed = False
        #db_table = 'complexmaprefset_f'
        unique_together = (('_id', 'effectivetime'),)


class ConceptF(models.Model):
    _id = models.CharField(max_length=18)
    effectivetime = models.DateField()
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    definitionstatusid = models.CharField(max_length=18)

    def __str__(self):
        return '{}'.format(self._id)


    class Meta:
        #managed = False
        #db_table = 'concept_f'
        unique_together = (('_id', 'effectivetime'),)


class DescriptionF(models.Model):
    _id = models.CharField(max_length=18)
    effectivetime = models.DateField()
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    conceptid = models.CharField(max_length=18)
    languagecode = models.CharField(max_length=2)
    typeid = models.CharField(max_length=18)
    term = models.TextField()
    casesignificanceid = models.CharField(max_length=18)

    @property
    def term_reducido (self):
        return self.term[:500]

    @property
    def fecha (self):
        from datetime import datetime
        return datetime.strptime(self.effectivetime, '%y/%m/%d')


    class Meta:
        #managed = False
        #db_table = 'description_f'
        unique_together = (('_id', 'effectivetime'),)


class ExtendedmaprefsetF(models.Model):
    _id = models.UUIDField()
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    refsetid = models.CharField(max_length=18)
    referencedcomponentid = models.CharField(max_length=18)
    mapgroup = models.SmallIntegerField()
    mappriority = models.SmallIntegerField()
    maprule = models.TextField(blank=True, null=True)
    mapadvice = models.TextField(blank=True, null=True)
    maptarget = models.TextField(blank=True, null=True)
    correlationid = models.CharField(max_length=18, blank=True, null=True)
    mapcategoryid = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'extendedmaprefset_f'
        unique_together = (('_id', 'effectivetime'),)


class LangrefsetF(models.Model):
    _id = models.UUIDField()
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    refsetid = models.CharField(max_length=18)
    referencedcomponentid = models.CharField(max_length=18)
    acceptabilityid = models.CharField(max_length=18)

    class Meta:
        #managed = False
        #db_table = 'langrefset_f'
        unique_together = (('_id', 'effectivetime'),)


class RelationshipF(models.Model):
    _id = models.CharField(max_length=18)
    effectivetime = models.DateField()
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    sourceid = models.CharField(max_length=18)
    destinationid = models.CharField(max_length=18)
    relationshipgroup = models.CharField(max_length=18)
    typeid = models.CharField(max_length=18)
    characteristictypeid = models.CharField(max_length=18)
    modifierid = models.CharField(max_length=18)

    class Meta:
        #managed = False
        #db_table = 'relationship_f'
        unique_together = (('_id', 'effectivetime'),)


class SimplemaprefsetF(models.Model):
    _id = models.UUIDField()
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    refsetid = models.CharField(max_length=18)
    referencedcomponentid = models.CharField(max_length=18)
    maptarget = models.TextField()

    class Meta:
        #managed = False
        #db_table = 'simplemaprefset_f'
        unique_together = (('_id', 'effectivetime'),)


class SimplerefsetF(models.Model):
    _id = models.UUIDField()
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    refsetid = models.CharField(max_length=18)
    referencedcomponentid = models.CharField(max_length=18)

    class Meta:
        #managed = False
        #db_table = 'simplerefset_f'
        unique_together = (('_id', 'effectivetime'),)


class StatedRelationshipF(models.Model):
    _id = models.CharField(max_length=18)
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    sourceid = models.CharField(max_length=18)
    destinationid = models.CharField(max_length=18)
    relationshipgroup = models.CharField(max_length=18)
    typeid = models.CharField(max_length=18)
    characteristictypeid = models.CharField(max_length=18)
    modifierid = models.CharField(max_length=18)

    class Meta:
        #managed = False
        #db_table = 'stated_relationship_f'
        unique_together = (('_id', 'effectivetime'),)


class TextdefinitionF(models.Model):
    _id = models.CharField(max_length=18)
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    conceptid = models.CharField(max_length=18)
    languagecode = models.CharField(max_length=2)
    typeid = models.CharField(max_length=18)
    term = models.TextField()
    casesignificanceid = models.CharField(max_length=18)

    class Meta:
        #managed = False
        #db_table = 'textdefinition_f'
        unique_together = (('_id', 'effectivetime'),)

'''
class Concept(models.Model):
    id = models.IntegerField(primary_key=True)
    _id = models.CharField(max_length=18)
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    definitionstatusid = models.CharField(max_length=18)

    def __str__(self):
        return '{}'.format(self._id)


    class Meta:
        managed = False
        db_table = 'view_concept'
        unique_together = (('_id', 'effectivetime'),)


class DescriptionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all().order_by('term')[0:500]

class Description(models.Model):
    id = models.IntegerField(primary_key=True)
    _id = models.CharField(max_length=18)
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    conceptid = models.CharField(max_length=18)
    languagecode = models.CharField(max_length=2)
    typeid = models.CharField(max_length=18)
    term = models.TextField()
    casesignificanceid = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'view_description'
        unique_together = (('_id', 'effectivetime'),)


class Relationship(models.Model):
    id = models.IntegerField(primary_key=True)
    _id = models.CharField(max_length=18)
    effectivetime = models.CharField(max_length=8)
    active = models.CharField(max_length=1)
    moduleid = models.CharField(max_length=18)
    sourceid = models.CharField(max_length=18)
    destinationid = models.CharField(max_length=18)
    relationshipgroup = models.CharField(max_length=18)
    typeid = models.CharField(max_length=18)
    characteristictypeid = models.CharField(max_length=18)
    modifierid = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'view_relationship'
        unique_together = (('_id', 'effectivetime'),)
'''