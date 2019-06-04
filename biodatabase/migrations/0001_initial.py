# Generated by Django 2.2.1 on 2019-05-31 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneDbLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('hgnc', models.CharField(blank=True, db_column='HGNC', max_length=255, null=True)),
                ('entrez_gene', models.CharField(blank=True, db_column='Entrez_Gene', max_length=255, null=True)),
                ('ensembl', models.CharField(blank=True, db_column='Ensembl', max_length=255, null=True)),
                ('uniprotkb', models.CharField(blank=True, db_column='UniProtKB', max_length=255, null=True)),
                ('omim', models.CharField(blank=True, db_column='OMIM', max_length=255, null=True)),
                ('hgnc_link', models.CharField(blank=True, db_column='HGNC_link', max_length=255, null=True)),
                ('entrez_gene_link', models.CharField(blank=True, db_column='Entrez Gene_link', max_length=255, null=True)),
                ('ensembl_link', models.CharField(blank=True, db_column='Ensembl_link', max_length=255, null=True)),
                ('uniprotkb_link', models.CharField(blank=True, db_column='UniProtKB_link', max_length=255, null=True)),
                ('omim_link', models.CharField(blank=True, db_column='OMIM_link', max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('summary_entrez', models.CharField(blank=True, max_length=255, null=True)),
                ('summary_genecard', models.CharField(blank=True, max_length=255, null=True)),
                ('summary_uniport', models.CharField(blank=True, max_length=255, null=True)),
                ('summary_tocris', models.CharField(blank=True, db_column='summary_Tocris', max_length=255, null=True)),
                ('summary_civic', models.CharField(blank=True, db_column='summary_CIViC', max_length=255, null=True)),
            ],
            options={
                'db_table': 'gene_db_link',
                'managed': False,
            },
        ),
    ]
