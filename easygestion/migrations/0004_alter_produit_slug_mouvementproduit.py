# Generated by Django 4.2.18 on 2025-02-18 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("easygestion", "0003_produit_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produit",
            name="slug",
            field=models.SlugField(max_length=128, unique=True),
        ),
        migrations.CreateModel(
            name="MouvementProduit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "type_mouvement",
                    models.CharField(
                        choices=[
                            ("entrée", "Entrée"),
                            ("sortie", "Sortie"),
                            ("retour", "Retour"),
                        ],
                        max_length=50,
                    ),
                ),
                ("quantite", models.PositiveIntegerField(default=0)),
                ("stock_restant", models.PositiveIntegerField()),
                ("motif", models.TextField(blank=True, null=True)),
                (
                    "produit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mouvements",
                        to="easygestion.produit",
                    ),
                ),
            ],
        ),
    ]
