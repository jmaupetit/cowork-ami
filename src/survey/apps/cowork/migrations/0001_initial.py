# Generated by Django 3.1.7 on 2021-03-08 21:30

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=100, verbose_name="Prénom")),
                ("last_name", models.CharField(max_length=100, verbose_name="Nom")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        choices=[
                            ("AUT", "Authezat"),
                            ("AYD", "Aydat"),
                            ("BUS", "Busséol"),
                            ("CHA", "Chanonat"),
                            ("COR", "Corent"),
                            ("COU", "Cournols"),
                            ("LAP", "Laps"),
                            ("LRB", "La Roche-Blanche"),
                            ("LRN", "La Roche-Noire"),
                            ("LSA", "La Sauvetat"),
                            ("LMV", "Les Martres-de-Veyre"),
                            ("LCR", "Le Crest"),
                            ("MAN", "Manglieu"),
                            ("MIR", "Mirefleurs"),
                            ("OLL", "Olloix"),
                            ("ORC", "Orcet"),
                            ("PIG", "Pignols"),
                            ("SAT", "Saint-Amant-Tallende"),
                            ("SGA", "Saint-Georges-Sur-Allier"),
                            ("SMA", "Saint-Maurice-Sur-Allier"),
                            ("SSD", "Saint-Sandoux"),
                            ("SST", "Saint-Saturnin"),
                            ("SAL", "Sallèdes"),
                            ("TAL", "Tallende"),
                            ("VMT", "Veyre-Monton"),
                            ("VLC", "Vic-Le-Comte"),
                            ("YEB", "Yronde-et-Buron"),
                        ],
                        help_text="Indiquez la commune de votre résidence principale",
                        max_length=3,
                        verbose_name="Commune",
                    ),
                ),
                (
                    "has_accepted_data_policy",
                    models.BooleanField(
                        default=False,
                        verbose_name="J'accepte la potitique de gestion des données du présent questionnaire",
                    ),
                ),
                (
                    "desired_role",
                    models.CharField(
                        choices=[
                            ("ASO", "Membre fondateur"),
                            ("PMT", "Résident (bureau permanent)"),
                            ("NMD", "Nomade (à la journée ou demi-journée)"),
                            ("WAT", "Sympatisant"),
                        ],
                        default="WAT",
                        help_text="Veuillez préciser votre niveau d'implication dans le projet",
                        max_length=3,
                        verbose_name="Role désiré",
                    ),
                ),
                (
                    "max_monthly_bill",
                    models.IntegerField(
                        choices=[
                            (1, "moins de 100 euros"),
                            (2, "entre 100 et 200 euros"),
                            (3, "entre 200 et 300 euros"),
                            (4, "plus de 300 euros"),
                        ],
                        default=1,
                        help_text="Veuillez indiquer quel montant maximal votre entreprise peut dépenser pour votre hébergement",
                        verbose_name="Budget mensuel maximal",
                    ),
                ),
                (
                    "has_validated_email",
                    models.BooleanField(
                        default=False,
                        editable=False,
                        verbose_name="A validé son adresse email",
                    ),
                ),
            ],
            options={
                "verbose_name": "Candidature",
                "verbose_name_plural": "Candidatures",
                "ordering": ("last_name", "first_name"),
            },
        ),
    ]