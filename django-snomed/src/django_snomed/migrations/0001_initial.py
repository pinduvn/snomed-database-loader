# Generated by Django 3.0.6 on 2020-06-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextdefinitionF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=18)),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('conceptid', models.CharField(max_length=18)),
                ('languagecode', models.CharField(max_length=2)),
                ('typeid', models.CharField(max_length=18)),
                ('term', models.TextField()),
                ('casesignificanceid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='StatedRelationshipF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=18)),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('sourceid', models.CharField(max_length=18)),
                ('destinationid', models.CharField(max_length=18)),
                ('relationshipgroup', models.CharField(max_length=18)),
                ('typeid', models.CharField(max_length=18)),
                ('characteristictypeid', models.CharField(max_length=18)),
                ('modifierid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='SimplerefsetF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('refsetid', models.CharField(max_length=18)),
                ('referencedcomponentid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='SimplemaprefsetF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('refsetid', models.CharField(max_length=18)),
                ('referencedcomponentid', models.CharField(max_length=18)),
                ('maptarget', models.TextField()),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='RelationshipF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=18)),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('sourceid', models.CharField(max_length=18)),
                ('destinationid', models.CharField(max_length=18)),
                ('relationshipgroup', models.CharField(max_length=18)),
                ('typeid', models.CharField(max_length=18)),
                ('characteristictypeid', models.CharField(max_length=18)),
                ('modifierid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='LangrefsetF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('refsetid', models.CharField(max_length=18)),
                ('referencedcomponentid', models.CharField(max_length=18)),
                ('acceptabilityid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='ExtendedmaprefsetF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('refsetid', models.CharField(max_length=18)),
                ('referencedcomponentid', models.CharField(max_length=18)),
                ('mapgroup', models.SmallIntegerField()),
                ('mappriority', models.SmallIntegerField()),
                ('maprule', models.TextField(blank=True, null=True)),
                ('mapadvice', models.TextField(blank=True, null=True)),
                ('maptarget', models.TextField(blank=True, null=True)),
                ('correlationid', models.CharField(blank=True, max_length=18, null=True)),
                ('mapcategoryid', models.CharField(blank=True, max_length=18, null=True)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='DescriptionF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=18)),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('conceptid', models.CharField(max_length=18)),
                ('languagecode', models.CharField(max_length=2)),
                ('typeid', models.CharField(max_length=18)),
                ('term', models.TextField()),
                ('casesignificanceid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='ConceptF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=18)),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('definitionstatusid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='ComplexmaprefsetF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('refsetid', models.CharField(max_length=18)),
                ('referencedcomponentid', models.CharField(max_length=18)),
                ('mapgroup', models.SmallIntegerField()),
                ('mappriority', models.SmallIntegerField()),
                ('maprule', models.TextField(blank=True, null=True)),
                ('mapadvice', models.TextField(blank=True, null=True)),
                ('maptarget', models.TextField(blank=True, null=True)),
                ('correlationid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='AttributevaluerefsetF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('refsetid', models.CharField(max_length=18)),
                ('referencedcomponentid', models.CharField(max_length=18)),
                ('valueid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
        migrations.CreateModel(
            name='AssociationrefsetF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('effectivetime', models.CharField(max_length=8)),
                ('active', models.CharField(max_length=1)),
                ('moduleid', models.CharField(max_length=18)),
                ('refsetid', models.CharField(max_length=18)),
                ('referencedcomponentid', models.CharField(max_length=18)),
                ('targetcomponentid', models.CharField(max_length=18)),
            ],
            options={
                'unique_together': {('_id', 'effectivetime')},
            },
        ),
    ]
