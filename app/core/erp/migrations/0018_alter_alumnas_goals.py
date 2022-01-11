# Generated by Django 3.2.8 on 2022-01-10 20:04

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0017_auto_20220110_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnas',
            name='goals',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('flexibility', 'Flexibilidad'), ('strength', 'Fuerza'), ('relax', 'Relajación'), ('posture', 'Postura disminución del estrés'), ('others', 'Otros')], max_length=41),
        ),
    ]