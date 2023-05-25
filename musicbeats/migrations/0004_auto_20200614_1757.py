

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0003_song_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
